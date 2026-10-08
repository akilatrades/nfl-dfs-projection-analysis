"""Build the analyst-selected 4,000–6,000-entry research recommendation."""

import hashlib
import json
from pathlib import Path

import pandas as pd

from run_week5_research import scenario_pool
from src.optimizer import assign_slots, optimize_lineup
from src.projections import add_model_projections


def main():
    root = Path(__file__).resolve().parent
    week = root / "weeks/2026_week_05"
    out = week / "single_entry"
    profile = json.loads((out / "profile.json").read_text())
    inputs = pd.read_csv(week / "projection_inputs.csv")
    pool, _ = scenario_pool(inputs)
    exclusions = tuple(profile["held_players"] + profile["field_build_holds"])
    summaries, lineups = [], []
    for quarterback in profile["quarterbacks"]:
        team = pool.loc[pool.player.eq(quarterback), "team"].iloc[0]
        changed = inputs.copy()
        changed.loc[
            changed.player.eq(quarterback),
            ["pass_attempts", "pass_td", "prob_300_pass"],
        ] *= 0.8
        changed.loc[
            changed.team.eq(team) & changed.position.isin(["RB", "WR", "TE"]),
            ["targets", "rec_td", "prob_100_rec"],
        ] *= 0.8
        passing_stress = add_model_projections(changed).set_index("player")
        for stack_size in [1, 2]:
            lineup = assign_slots(
                optimize_lineup(
                    pool,
                    ["joint_downside"],
                    quarterback=quarterback,
                    bring_back=True,
                    min_stack=stack_size,
                    exclude=exclusions,
                )
            )
            candidate = quarterback.lower().replace(" ", "_")
            candidate += f"_stack{stack_size}_bringback"
            lineup.insert(0, "candidate_id", candidate)
            lineups.append(lineup)
            summaries.append(
                {
                    "candidate_id": candidate,
                    "salary": int(lineup.salary.sum()),
                    "projection": lineup.model_projection.sum(),
                    "joint_workload_stress": lineup.joint_downside.sum(),
                    "qb_team_passing_down_20pct": passing_stress.loc[
                        lineup.player, "model_projection"
                    ].sum(),
                }
            )
    comparison = pd.DataFrame(summaries)
    comparison.to_csv(out / "field_comparison.csv", index=False, float_format="%.4f")
    export = [
        "candidate_id",
        "slot",
        "player",
        "position",
        "team",
        "opponent",
        "salary",
        "kickoff_utc",
        "model_projection",
        "joint_downside",
        "condition",
    ]
    all_lineups = pd.concat(lineups)[export]
    all_lineups.to_csv(out / "field_lineups.csv", index=False, float_format="%.4f")
    selected_id = profile["recommended_candidate"]
    selected = all_lineups.loc[all_lineups.candidate_id.eq(selected_id)]
    if len(selected) != 9 or selected.player.nunique() != 9:
        raise ValueError("The selected candidate must be one complete lineup.")
    selected.to_csv(out / "recommended_lineup.csv", index=False, float_format="%.4f")
    manifest = {
        "status": "provisional_analyst_recommendation_not_submitted",
        "field_size_target": profile["field_size_target"],
        "selected_candidate": selected_id,
        "selection": "Analyst choice; field size does not enter the scoring model",
        "objective": "joint workload stress within declared construction constraints",
        "passing_stress": "Separate diagnostic, not combined or probability weighted",
        "candidate_specifications": len(comparison),
        "sha256": {},
    }
    for path in [
        out / "profile.json",
        week / "projection_inputs.csv",
        Path(__file__),
        root / "run_week5_research.py",
        root / "src/optimizer.py",
        root / "src/projections.py",
        out / "field_comparison.csv",
        out / "field_lineups.csv",
        out / "recommended_lineup.csv",
    ]:
        manifest["sha256"][str(path.relative_to(root))] = hashlib.sha256(
            path.read_bytes()
        ).hexdigest()
    (out / "field_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(comparison.to_string(index=False))
    print(selected[["slot", "player", "salary"]].to_string(index=False))


if __name__ == "__main__":
    main()
