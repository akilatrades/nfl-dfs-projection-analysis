"""Reproduce provisional Week 5 builds from explicitly manual football priors."""

import json
import hashlib
from pathlib import Path

import pandas as pd

from src.optimizer import assign_slots, optimize_lineup
from src.projections import add_model_projections


def scenario_pool(inputs):
    pool = add_model_projections(inputs)
    cases = {
        "gibbs_volume_down": (inputs.player.eq("Jahmyr Gibbs"), ["rush_attempts", "targets", "rush_td", "rec_td", "prob_100_rush", "prob_100_rec"], 0.8),
        "dowdle_returns": (inputs.player.eq("Jaylen Warren"), ["rush_attempts", "targets", "rush_td", "rec_td", "prob_100_rush", "prob_100_rec"], 0.75),
        "cin_receivers_return": (inputs.player.isin(["Mitch Tinsley", "Dohnte Meyers"]), ["targets", "rec_td", "prob_100_rec"], 0.6),
        "bagent_volume_down": (inputs.player.eq("Tyson Bagent"), ["pass_attempts", "pass_td", "rush_attempts", "rush_td", "prob_300_pass"], 0.8),
        "wilson_committee": (inputs.player.eq("Emanuel Wilson"), ["rush_attempts", "targets", "rush_td", "rec_td", "prob_100_rush", "prob_100_rec"], 0.75),
        "diggs_limited": (inputs.player.eq("Stefon Diggs"), ["targets", "rec_td", "prob_100_rec"], 0.7),
    }
    for name, (mask, columns, factor) in cases.items():
        changed = inputs.copy()
        changed.loc[mask, columns] *= factor
        if name == "cin_receivers_return":
            changed.loc[changed.player.eq("Chase Brown"), ["targets", "rec_td", "prob_100_rec"]] *= 0.8
        pool[name] = add_model_projections(changed).model_projection
    # Simultaneous stress is reported separately; it is not assigned a probability.
    pool["joint_downside"] = pool.model_projection + sum(
        pool[name] - pool.model_projection for name in cases
    )
    return pool, ["model_projection", *cases]


def main():
    week = Path(__file__).resolve().parent / "weeks/2026_week_05"
    pool, scenarios = scenario_pool(pd.read_csv(week / "projection_inputs.csv"))
    pool.to_csv(week / "player_projections.csv", index=False, float_format="%.4f")
    export_columns = ["slot", "player", "position", "team", "opponent", "salary", "kickoff_utc", *scenarios, "joint_downside", "condition"]
    summaries, lineups = [], []
    for qb in pool.loc[pool.position.eq("QB"), "player"]:
        for mode in ["mean", "stress"]:
            for bring_back in [False, True]:
                cols = ["model_projection"] if mode == "mean" else scenarios
                lineup = optimize_lineup(pool, cols, quarterback=qb, bring_back=bring_back)
                objective = lineup.attrs["objective"]
                candidate = f"{qb.lower().replace(' ', '_')}_{mode}_{'bringback' if bring_back else 'optional'}"
                lineup = assign_slots(lineup)
                lineup.insert(0, "candidate_id", candidate)
                lineups.append(lineup)
                totals = lineup[scenarios].sum()
                summaries.append(dict(candidate_id=candidate,quarterback=qb,objective=mode,bring_back_required=bring_back,salary=int(lineup.salary.sum()),base_projection=totals.model_projection,worst_tested_scenario=totals.min(),joint_downside=lineup.joint_downside.sum(),objective_value=objective,**{c:totals[c] for c in scenarios[1:]},players=" | ".join(lineup.player)))
    summary = pd.DataFrame(summaries).sort_values(["worst_tested_scenario", "base_projection"], ascending=False)
    summary.to_csv(week / "candidate_comparison.csv", index=False, float_format="%.4f")
    pd.concat(lineups)[["candidate_id", *export_columns]].to_csv(week / "candidate_lineups.csv", index=False, float_format="%.4f")
    leader_id = summary.iloc[0].candidate_id
    leader = next(l for l in lineups if l.candidate_id.iloc[0] == leader_id)
    leader[["candidate_id", *export_columns]].to_csv(week / "provisional_lineup.csv", index=False, float_format="%.4f")
    # Re-optimize instead of prescribing an invalid one-for-one salary swap.
    changes = {
        "no_bagent": ("Tyson Bagent",),
        "no_cin_backup_receivers": ("Mitch Tinsley", "Dohnte Meyers"),
        "no_warren": ("Jaylen Warren",),
        "no_gibbs": ("Jahmyr Gibbs",),
        "no_emanuel_wilson": ("Emanuel Wilson",),
        "no_diggs": ("Stefon Diggs",),
    }
    contingencies = []
    for name, excluded in changes.items():
        lineup = assign_slots(optimize_lineup(pool, scenarios, exclude=excluded))
        lineup.insert(0, "contingency", name)
        contingencies.append(lineup)
    pd.concat(contingencies)[["contingency", *export_columns]].to_csv(week / "contingency_lineups.csv", index=False, float_format="%.4f")
    gibbs = assign_slots(optimize_lineup(pool, scenarios, locks=("Jahmyr Gibbs",)))
    gibbs[export_columns].to_csv(week / "gibbs_alternative.csv", index=False, float_format="%.4f")
    manifest = {"as_of":"2026-10-08", "slate":"2026-10-11 DraftKings Sunday afternoon research pool", "status":"PROVISIONAL_NOT_CONTEST_VERIFIED", "pool_size":len(pool), "candidates":len(summary), "projection_type":"manual analyst assumptions converted by existing scoring model", "source_projection_imported":False, "ownership_model_used":False, "simulation_used":False, "solver":"SciPy HiGHS MILP; zero relative gap; only status=0 accepted", "selection":"maximum worst separately tested scenario among QB families; optional bring-back", "scenarios":scenarios, "selected_candidate":leader_id, "missing":["official contest salary export and player IDs", "complete slate player pool", "verified final roles and inactives", "actual contest size and payouts", "calibrated joint outcome and ownership model"]}
    root = week.parents[1]
    manifest["sha256"] = {
        str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in [week / "projection_inputs.csv", root / "run_week5_research.py", root / "src/optimizer.py", root / "src/projections.py"]
    }
    (week / "run_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(summary[["candidate_id", "salary", "base_projection", "worst_tested_scenario"]].head(8).to_string(index=False))
    print(leader[["slot", "player", "salary", "model_projection"]].to_string(index=False))


if __name__ == "__main__":
    main()
