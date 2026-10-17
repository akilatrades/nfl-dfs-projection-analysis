"""Week 6 (October 18, 2026) single-entry research.

Inputs come from public football stats through Week 5 (nflverse weekly
data) shrunk toward position baselines by src/input_model.py, lines from the
nflverse schedule file, and salaries from published articles (see
weeks/2026_week_06/sources.md). The scenarios below are the Week 6 news
items that could change a player's role; each is applied as a multiplier on
the affected volume inputs, as in Week 5.

    python run_week6_research.py
"""

import hashlib
import json
from pathlib import Path

import pandas as pd

from src.optimizer import assign_slots, optimize_lineup
from src.projections import add_model_projections

WEEK = Path("weeks/2026_week_06")
VOLUME_RB = [
    "rush_attempts",
    "targets",
    "rush_td",
    "rec_td",
    "prob_100_rush",
    "prob_100_rec",
]
VOLUME_WR = ["targets", "rec_td", "prob_100_rec"]
VOLUME_QB = ["pass_attempts", "pass_td", "rush_attempts", "rush_td", "prob_300_pass"]

# (players affected, columns, multiplier). Written before any lineup was built.
SCENARIOS = {
    "williams_sits": (
        ["Caleb Williams"],
        VOLUME_QB,
        0.0,
    ),  # questionable; Bears offense without him
    "jackson_plays": (
        ["Tyler Huntley"],
        VOLUME_QB,
        0.0,
    ),  # Huntley only has a role if Jackson is out
    "dowdle_back": (["Jaylen Warren"], VOLUME_RB, 0.75),
    "corum_share": (["Kyren Williams"], VOLUME_RB, 0.85),
    "olave_returns": (["DeVaughn Vele"], VOLUME_WR, 0.7),
    "barkley_back": (["Dameon Pierce"], VOLUME_RB, 0.4),
    "worthy_no_bump": (
        ["Xavier Worthy"],
        VOLUME_WR,
        0.8,
    ),  # Rice out already in the baseline usage? no: usage is through Week 5 with Rice; this removes the assumed bump
    "stevenson_no_bump": (["Rhamondre Stevenson"], VOLUME_RB, 0.85),
}


def scenario_pool(inputs):
    pool = add_model_projections(inputs)
    names = []
    for name, (players, columns, k) in SCENARIOS.items():
        adjusted = inputs.copy()
        mask = adjusted.player.isin(players)
        adjusted.loc[mask, columns] = adjusted.loc[mask, columns] * k
        pool[name] = add_model_projections(adjusted).model_projection
        names.append(name)
    pool["joint_downside"] = pool[names].min(axis=1)
    return pool, names


def main():
    inputs = pd.read_csv(WEEK / "projection_inputs.csv")
    pool, scenarios = scenario_pool(inputs)
    pool.to_csv(WEEK / "player_projections.csv", index=False, float_format="%.4f")
    objectives = {
        "mean": ["model_projection"],
        "individual_stress": scenarios,
        "joint_stress": ["joint_downside"],
    }
    quarterbacks = [
        "Josh Allen",
        "Matthew Stafford",
        "Caleb Williams",
        "Drake Maye",
        "Tyler Shough",
        "Bryce Young",
        "Kirk Cousins",
    ]
    summaries, lineups = [], []
    for qb in quarterbacks:
        for objective, columns in objectives.items():
            try:
                lineup = assign_slots(optimize_lineup(pool, columns, quarterback=qb))
            except Exception as error:  # noqa: BLE001 - report infeasible builds
                print(f"{qb} / {objective}: {error}")
                continue
            cid = qb.lower().replace(" ", "_") + "_" + objective
            lineup.insert(0, "candidate_id", cid)
            lineups.append(lineup)
            summaries.append(
                {
                    "candidate_id": cid,
                    "quarterback": qb,
                    "objective": objective,
                    "salary": int(lineup.salary.sum()),
                    "projection": round(float(lineup.model_projection.sum()), 2),
                    "worst_individual_stress": round(
                        float(lineup[scenarios].sum().min()), 2
                    ),
                    "joint_stress": round(float(lineup.joint_downside.sum()), 2),
                    "players": " | ".join(lineup.player),
                }
            )
    summary = pd.DataFrame(summaries).sort_values("projection", ascending=False)
    summary.to_csv(WEEK / "candidate_comparison.csv", index=False)
    pd.concat(lineups).to_csv(
        WEEK / "candidate_lineups.csv", index=False, float_format="%.4f"
    )
    digest = hashlib.sha256((WEEK / "projection_inputs.csv").read_bytes()).hexdigest()[
        :16
    ]
    (WEEK / "run_manifest.json").write_text(
        json.dumps(
            {
                "inputs_sha256_16": digest,
                "scenarios": list(SCENARIOS),
                "quarterbacks": quarterbacks,
                "generated": "2026-10-17",
            },
            indent=2,
        )
        + "\n"
    )
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
