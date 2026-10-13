"""Week 5 Sunday process correction after Week 3/4 reviews.

Run: python run_week5_process_review.py
Requires the existing Sunday 48-player scenario and scipy optimizer.

A pre-lock decision comparison, NOT an inferred top-23k winning lineup,
calibrated joint ceiling distribution, contest EV, or DK upload file.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pandas as pd

from run_week5_sunday import sunday_inputs, football_scenarios, HELD
from src.optimizer import optimize_lineup, assign_slots
from src.projections import add_model_projections

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "weeks/2026_week_05/sunday_2026-10-11/process_review_2026-10-11"
# More conservative than morning's opening estimates; these are subjective,
# scenario priors, not statistical injury or weather adjustments.
CONSERVATIVE_CHANGES = {
    "Romeo Doubs": {
        "targets": 5.5,
        "rec_td": 0.27,
        "condition": "5.5 target baseline; Week 4 nine targets and 2 TD not guaranteed; upside scenario retains 7.5",
    },
    "Braelon Allen": {
        "rush_attempts": 16.0,
        "targets": 3.2,
        "rush_td": 0.38,
        "rec_td": 0.065,
        "prob_100_rush": 0.10,
        "condition": "Hall out, but Jets low-total rainy game: conservative workload sensitivity",
    },
}
PRIMARY_EXCLUSIONS = tuple(
    dict.fromkeys([*HELD, "Romeo Doubs", "Braelon Allen", "Woody Marks"])
)
# The named cases prevent a choice driven by a single generic max-mean run.
# max_te=2 is examined against max_te=1 for a direct construction comparison.
SPECS = [
    dict(
        id="brissett_two_supported_receivers",
        qb="Jacoby Brissett",
        locks=("Michael Wilson", "Trey McBride"),
        azmin=2,
        azmax=3,
    ),
    dict(
        id="goff_amonra_laporta",
        qb="Jared Goff",
        locks=("Amon-Ra St. Brown", "Sam LaPorta"),
        azmin=2,
        azmax=3,
    ),
    dict(
        id="maye_gibbs_with_henry",
        qb="Drake Maye",
        locks=("Jahmyr Gibbs", "Hunter Henry"),
        azmin=1,
        azmax=2,
    ),
    dict(
        id="love_watson",
        qb="Jordan Love",
        locks=("Christian Watson",),
        azmin=1,
        azmax=2,
    ),
    dict(
        id="maye_doubs_control",
        qb="Drake Maye",
        locks=("Romeo Doubs",),
        azmin=1,
        azmax=2,
        allow_doubs=True,
    ),
]
PUBLISHED_OWNERSHIP_SNAPSHOT = {
    # Oct 10 Fantasy Alarm, competing vendors differ substantially.
    "Jahmyr Gibbs": 33.5,
    "Michael Wilson": 33.1,
    "Trey McBride": 31.3,
    "D'Andre Swift": 30.8,
    "Braelon Allen": 27.1,
    "Amon-Ra St. Brown": 24.8,
    "Chase Brown": 22.1,
}


def revised_inputs() -> pd.DataFrame:
    players = sunday_inputs().copy()
    for name, fields in CONSERVATIVE_CHANGES.items():
        where = players.player.eq(name)
        if where.sum() != 1:
            raise ValueError("Missing single named player: " + name)
        for field, new_value in fields.items():
            players.loc[where, field] = new_value
    return players


def evaluate():
    inp = revised_inputs()
    pool = add_model_projections(inp)
    summary = []
    lineups = []
    for spec in SPECS:
        excluded = tuple(
            n
            for n in PRIMARY_EXCLUSIONS
            if not (n == "Romeo Doubs" and spec.get("allow_doubs", False))
        )
        for max_te in (1, 2):
            label = spec["id"] + "_te" + str(max_te)
            try:
                optimum = optimize_lineup(
                    pool,
                    ["model_projection"],
                    quarterback=spec["qb"],
                    locks=spec["locks"],
                    min_stack=1,
                    bring_back=False,
                    exclude=excluded,
                    max_tight_ends=max_te,
                    team_group_bounds=(("ARI", "DET"), spec["azmin"], spec["azmax"]),
                )
            except ValueError as e:
                if "infeasible" in str(e).lower():
                    summary.append(
                        {
                            "candidate": label,
                            "status": "infeasible",
                            "reason": str(e),
                        }
                    )
                    continue
                raise
            lineup = assign_slots(optimum)
            if len(lineup) != 9 or lineup.salary.sum() > 50000:
                raise AssertionError("Invalid lineup size or salary")
            if not set(spec["locks"]).issubset(set(lineup.player)):
                raise AssertionError("Locked player absent")
            score_scenarios = football_scenarios(inp, spec["qb"])
            # Sensitivity for unsupported claims of extra targets/carries:
            role_down = inp.copy()
            for player in ("Romeo Doubs", "Braelon Allen"):
                mask = role_down.player.eq(player)
                if player == "Romeo Doubs":
                    role_down.loc[mask, ["targets", "rec_td", "prob_100_rec"]] *= 0.75
                else:
                    role_down.loc[
                        mask,
                        [
                            "rush_attempts",
                            "rush_td",
                            "targets",
                            "rec_td",
                            "prob_100_rush",
                        ],
                    ] *= 0.75
            score_scenarios["uncertain_role_down25"] = (
                add_model_projections(role_down).set_index("player").model_projection
            )
            row = dict(
                candidate=label,
                status="provisional",
                salary=int(lineup.salary.sum()),
                wr_below_6_targets=int(
                    (lineup.position.eq("WR") & (lineup.targets < 6)).sum()
                ),
                chalk_count=int(
                    lineup.player.isin(PUBLISHED_OWNERSHIP_SNAPSHOT.keys()).sum()
                ),
                arizona_detroit_count=int(lineup.team.isin(["ARI", "DET"]).sum()),
                speculative_count=int(lineup.role_risk.sum()),
                source_ownership_snapshot="Fantasy Alarm Oct 10; not contest specific",
            )
            for key, series in score_scenarios.items():
                row[key] = round(float(series.loc[lineup.player].sum()), 4)
            row["worst_separate_stress"] = round(
                min(row[name] for name in score_scenarios), 4
            )
            summary.append(row)
            for _, p in lineup.iterrows():
                lineups.append(
                    dict(
                        candidate=label,
                        slot=p.slot,
                        player=p.player,
                        team=p.team,
                        salary=int(p.salary),
                        individual_manual_mean=round(float(p.model_projection), 4),
                        expected_targets=float(p.targets),
                        expected_carries=float(p.rush_attempts),
                        condition=p.condition,
                    )
                )
    return inp, pool, pd.DataFrame(summary), pd.DataFrame(lineups)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    inp, pool, scores, lineups = evaluate()
    inp.to_csv(OUT / "review_inputs.csv", index=False)
    scores.to_csv(OUT / "comparison.csv", index=False, float_format="%.4f")
    lineups.to_csv(OUT / "candidate_lineups.csv", index=False, float_format="%.4f")
    manifest = {
        "as_of": "2026-10-11 Sunday pre-final-inactives",
        "origin": "Oct 9 inputs -> Oct 10 refresh -> Oct 11 48-player pool -> process correction",
        "input_count": len(inp),
        "contest": "$5, about 23k single-entry, exact contest ID unavailable",
        "evidence": "Dated source vs manual football scenarios separated",
        "objectives": "Mean within candidate constraints; no contest payout EV or P99",
        "ownership_model": "Dated third-party snapshots; unverified field-specific ownership",
        "scenario_semantics": "Separate deterministic stresses; NOT quantile/floor/probability",
        "salary_file_verified": False,
        "final_inactives_verified": False,
        "run_provenance": "Local script outputs generated when run, never assumed",
    }
    for path in [
        ROOT / "run_week5_process_review.py",
        OUT / "review_inputs.csv",
        OUT / "comparison.csv",
        OUT / "candidate_lineups.csv",
    ]:
        manifest.setdefault("sha256", {})[str(path.relative_to(ROOT))] = hashlib.sha256(
            path.read_bytes()
        ).hexdigest()
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(scores.to_string(index=False))


if __name__ == "__main__":
    main()
