"""Compare single-entry constructions; field size is an analyst label, not EV."""

import hashlib
import json
from pathlib import Path

import pandas as pd

from run_week5_research import scenario_pool
from src.optimizer import assign_slots, optimize_lineup
from src.projections import add_model_projections


def main():
    root = Path(__file__).resolve().parent
    out = root / "weeks/2026_week_05/single_entry_2026-10-09"
    inputs = pd.read_csv(out / "projection_inputs.csv")
    profile = json.loads((out / "profile.json").read_text())
    pool, _ = scenario_pool(inputs)
    changed = inputs.copy()
    changed.loc[
        changed.position.eq("RB"),
        [
            "rush_attempts",
            "targets",
            "rush_td",
            "rec_td",
            "prob_100_rush",
            "prob_100_rec",
        ],
    ] *= 0.8
    pool["rb_workload_down20"] = add_model_projections(changed).model_projection
    summaries, lineups, infeasible = [], [], []
    for qb in profile["quarterbacks"]:
        team = pool.loc[pool.player.eq(qb), "team"].iloc[0]
        changed = inputs.copy()
        changed.loc[
            changed.player.eq(qb), ["pass_attempts", "pass_td", "prob_300_pass"]
        ] *= 0.8
        changed.loc[
            changed.team.eq(team) & changed.position.isin(["RB", "WR", "TE"]),
            ["targets", "rec_td", "prob_100_rec"],
        ] *= 0.8
        pool["qb_passing_down20"] = add_model_projections(changed).model_projection
        scenarios = [
            "model_projection",
            "joint_downside",
            "rb_workload_down20",
            "qb_passing_down20",
        ]
        specs = [
            (style, objective, stack, back, ())
            for style, stack, back in [("compact", 1, False), ("game", 2, True)]
            for objective in ["mean", "balanced"]
        ]
        specs.append(("gibbs", "mean", 1, False, ("Jahmyr Gibbs",)))
        if qb == "Jared Goff":
            specs.append(
                (
                    "two_wr",
                    "mean",
                    2,
                    True,
                    ("Amon-Ra St. Brown", "Jameson Williams"),
                )
            )
        variants = [(*spec, te_cap) for spec in specs for te_cap in [1, 2]]
        for style, objective, stack, back, locks, te_cap in variants:
            candidate = qb.lower().replace(" ", "_").replace(".", "")
            candidate += f"_{style}_{objective}_te{te_cap}"
            try:
                result = optimize_lineup(
                    pool,
                    ["model_projection"] if objective == "mean" else scenarios,
                    quarterback=qb,
                    min_stack=stack,
                    bring_back=back,
                    locks=locks,
                    exclude=tuple(profile["holds"]),
                    max_tight_ends=te_cap,
                )
            except ValueError as exc:
                if "problem is infeasible" not in str(exc):
                    raise
                infeasible.append({"candidate_id": candidate, "reason": str(exc)})
                continue
            lineup = assign_slots(result)
            lineup.insert(0, "candidate_id", candidate)
            lineups.append(lineup)
            summaries.append(
                {
                    "candidate_id": candidate,
                    "salary": int(lineup.salary.sum()),
                    **{c: lineup[c].sum() for c in scenarios},
                    "worst_tested_scenario": lineup[scenarios].sum().min(),
                    "players": " | ".join(lineup.player),
                }
            )
    summary = pd.DataFrame(summaries)
    summary.to_csv(out / "comparison.csv", index=False, float_format="%.4f")
    exported = pd.concat(lineups)[
        [
            "candidate_id",
            "slot",
            "player",
            "position",
            "team",
            "opponent",
            "salary",
            "kickoff_utc",
            *scenarios,
            "condition",
        ]
    ]
    exported.to_csv(out / "lineups.csv", index=False, float_format="%.4f")
    selected = []
    for band in profile["field_bands"]:
        if not band.get("selected_candidate"):
            continue
        lineup = exported.loc[
            exported.candidate_id.eq(band["selected_candidate"])
        ].copy()
        if len(lineup) != 9:
            raise ValueError("Selected candidate not found or incomplete")
        lineup.insert(0, "field_band", band["label"])
        selected.append(lineup)
    if selected:
        pd.concat(selected).to_csv(
            out / "recommended_lineups.csv", index=False, float_format="%.4f"
        )
    manifest = {
        "status": "provisional_pre_final_injury_reports",
        "candidate_specifications": len(summary) + len(infeasible),
        "feasible_specifications": len(summary),
        "infeasible_specifications": infeasible,
        "unique_rosters": summary.players.nunique(),
        "field_size_model": "None; field bands express analyst preferences",
        "scenarios": "Deterministic sensitivities; no assigned probabilities",
        "ownership_and_payout_model": "None",
        "sha256": {},
    }
    for path in [
        out / "projection_inputs.csv",
        out / "input_changes.json",
        out / "profile.json",
        Path(__file__),
        root / "run_week5_research.py",
        root / "src/optimizer.py",
        root / "src/projections.py",
        out / "comparison.csv",
        out / "lineups.csv",
        *([out / "recommended_lineups.csv"] if selected else []),
    ]:
        manifest["sha256"][str(path.relative_to(root))] = hashlib.sha256(
            path.read_bytes()
        ).hexdigest()
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(summary.drop(columns="players").to_string(index=False))


if __name__ == "__main__":
    main()
