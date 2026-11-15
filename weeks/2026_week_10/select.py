"""Freeze recommendations separately from actual entered rosters and compare alternatives."""

import copy
import csv
import hashlib
import json
from datetime import datetime, timezone

import numpy as np

from run import ROOT, SEED, dump, evaluate_candidates, field_evaluate, simulate, validate


def main():
    pool = json.loads((ROOT / "inputs.json").read_text())
    lookup = {p["name"]: i for i, p in enumerate(pool)}
    specs = [
        ("fair_catch_60k", 5882, [
            ("QB", "Tyler Shough"), ("RB", "Chuba Hubbard"), ("RB", "Emmett Johnson"),
            ("WR", "Chris Olave"), ("WR", "Justin Jefferson"), ("WR", "Drake London"),
            ("TE", "Tyler Warren"), ("FLEX", "Travis Kelce"), ("DST", "Colts")]),
        ("fair_catch_125k", 12254, [
            ("QB", "Dak Prescott"), ("RB", "Bijan Robinson"), ("RB", "Emmett Johnson"),
            ("WR", "George Pickens"), ("WR", "Jakobi Meyers"), ("WR", "Wan'Dale Robinson"),
            ("TE", "Tyler Warren"), ("FLEX", "CeeDee Lamb"), ("DST", "Browns")]),
    ]
    entries, candidates = [], []
    for label, size, slots in specs:
        ids = sorted(lookup[name] for _, name in slots)
        validate(ids, pool)
        q = next(pool[i] for i in ids if pool[i]["pos"] == "QB")
        rows = [dict(slot=slot, **pool[lookup[name]]) for slot, name in slots]
        entries.append({"contest": label, "entry_fee": 12, "max_entries": size,
                        "status": "recommended; user entry not confirmed",
                        "salary": sum(r["salary"] for r in rows), "players": rows})
        candidates.append({"candidate_id": label, "ids": ids, "family": q["name"],
                           "partners": sum(pool[i]["team"] == q["team"] and pool[i]["pos"] in ["WR", "TE"] for i in ids),
                           "tes": sum(pool[i]["pos"] == "TE" for i in ids), "profiles": ["football_review"]})
    scores, _ = simulate(pool, 200000, SEED + 500)
    metrics = evaluate_candidates(pool, candidates, scores)
    stress = {}
    for label in ["lower_forecasts", "role_uncertainty", "less_variance"]:
        altered = copy.deepcopy(pool)
        for p in altered:
            if label == "lower_forecasts": p["mean"] = min(p[k] for k in ["mean", "spags", "fsc", "ftn"] if k in p)
            if label == "role_uncertainty":
                p["mean"] *= {"Emmett Johnson": .75, "Laquon Treadwell": .75, "Jakobi Meyers": .8,
                              "Deebo Samuel Sr.": .8, "Keenan Allen": .8, "DJ Moore": .8,
                              "George Kittle": .85, "Colby Parkinson": .85, "Tyler Warren": .85}.get(p["name"], 1.)
        ss, _ = simulate(altered, 75000, SEED + 100, .8 if label == "less_variance" else 1.)
        stress[label] = evaluate_candidates(altered, candidates, ss)
    totals = np.array([scores[:, c["ids"]].sum(1) for c in candidates])
    shared = sorted(set(candidates[0]["ids"]) & set(candidates[1]["ids"]))
    record = {"frozen_at_utc": datetime.now(timezone.utc).isoformat(), "slate_date": "2026-11-15",
              "main_slate_lock": "2026-11-15T12:00:00-06:00", "lineups": entries,
              "conditional_score_simulation": metrics, "stress_tests": stress,
              "portfolio": {"shared_players": [pool[i]["name"] for i in shared],
                            "score_correlation": float(np.corrcoef(totals)[0, 1]),
                            "p_either_200": float(np.mean(totals.max(0) >= 200)),
                            "note": "Score threshold probability, not contest profit or cash probability."},
              "salary_verification": "Published boards agree on selected salaries; official contest draft-group/player-ID export unavailable (public endpoint returned HTTP 403).",
              "selection_note": "Football-reviewed alternatives to the simulation-only leaders. Larger field uses credible DAL double stack and four WRs; smaller field uses NO-CAR and KC-ATL correlations with Warren/Kelce. No guarantee of uniqueness or calibrated win probability."}
    dump("recommendations.json", record)
    field = {}
    for label in ["base", "flatter", "stronger"]:
        path = ROOT / f"field_{label}.npy"
        if path.exists(): field[label] = field_evaluate(pool, candidates, np.load(path), 10000, SEED + 10)
    dump("recommendation_field_results.json", field)
    with (ROOT / "lineups.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["contest", "slot", "player", "team", "opponent", "salary", "projection", "ownership_estimate", "ownership_source"])
        w.writeheader()
        for entry in entries:
            for p in entry["players"]:
                w.writerow(dict(contest=entry["contest"], slot=p["slot"], player=p["name"], team=p["team"], opponent=p["opp"], salary=p["salary"], projection=p["mean"], ownership_estimate=p["own"], ownership_source=p["own_source"]))
    files = ["inputs.json", "candidates.json", "simulation_metrics.json", "sensitivity_results.json", "run.py", "sensitivity.py", "select.py", "recommendations.json"]
    dump("manifest.json", {"slate": "2026 Week 10 main", "seed": SEED,
         "pool_size": len(pool), "games": 10, "starting_qbs": 20,
         "candidate_count": len(json.loads((ROOT / "candidates.json").read_text())),
         "screen_draws": 150000, "final_validation_draws": 200000,
         "sensitivity_draws_per_variant": 75000, "field_scenarios_per_assumption": 10000,
         "field_note": "Same outcomes reused across field assumptions; do not add these as independent draws.",
         "sha256": {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in files}})
    print(json.dumps({"metrics": metrics, "portfolio": record["portfolio"]}, indent=2))


if __name__ == "__main__":
    main()
