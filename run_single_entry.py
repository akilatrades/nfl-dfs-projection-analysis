"""Compare provisional builds for the selected single-entry contest profile."""

import hashlib
import json
from pathlib import Path

import pandas as pd

from run_week5_research import scenario_pool
from src.optimizer import assign_slots, optimize_lineup


def main():
    root = Path(__file__).resolve().parent
    week = root / "weeks/2026_week_05"
    out = week / "single_entry"
    profile_path = out / "profile.json"
    profile = json.loads(profile_path.read_text())
    pool, scenarios = scenario_pool(pd.read_csv(week / "projection_inputs.csv"))
    objectives = {
        "mean": ["model_projection"],
        "individual_stress": scenarios,
        "joint_stress": ["joint_downside"],
    }
    summaries, lineups = [], []
    for quarterback in profile["quarterbacks"]:
        for objective, columns in objectives.items():
            lineup = assign_slots(
                optimize_lineup(
                    pool,
                    columns,
                    quarterback=quarterback,
                    exclude=tuple(profile["held_players"]),
                )
            )
            candidate = quarterback.lower().replace(" ", "_") + "_" + objective
            lineup.insert(0, "candidate_id", candidate)
            lineups.append(lineup)
            summaries.append(
                {
                    "candidate_id": candidate,
                    "quarterback": quarterback,
                    "objective": objective,
                    "salary": int(lineup.salary.sum()),
                    "projection": lineup.model_projection.sum(),
                    "worst_individual_stress": lineup[scenarios].sum().min(),
                    "joint_stress": lineup.joint_downside.sum(),
                    "players": " | ".join(lineup.player),
                }
            )
    summary = pd.DataFrame(summaries)
    summary.to_csv(out / "comparison.csv", index=False, float_format="%.4f")
    export = [
        "candidate_id",
        "slot",
        "player",
        "salary",
        *scenarios,
        "joint_downside",
        "condition",
    ]
    pd.concat(lineups)[export].to_csv(
        out / "lineups.csv", index=False, float_format="%.4f"
    )
    manifest = {
        "status": "research_only_no_final_entry",
        "entry_fee_usd": profile["entry_fee_usd"],
        "entry_limit": 1,
        "field_size": profile["field_size"],
        "candidate_specifications": len(summary),
        "selection": "compare_objectives_no_automatic_final_lineup",
        "sha256": {},
    }
    for path in [
        profile_path,
        week / "projection_inputs.csv",
        Path(__file__),
        root / "run_week5_research.py",
        root / "src/optimizer.py",
        root / "src/projections.py",
    ]:
        manifest["sha256"][str(path.relative_to(root))] = hashlib.sha256(
            path.read_bytes()
        ).hexdigest()
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(summary.drop(columns="players").to_string(index=False))


if __name__ == "__main__":
    main()
