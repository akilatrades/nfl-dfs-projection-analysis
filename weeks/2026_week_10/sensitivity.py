"""Held-out assumption checks, not fitted probabilities of adverse news."""

import copy
import json

import numpy as np

from run import ROOT, SEED, dump, evaluate_candidates, simulate, validate


def main():
    pool = json.loads((ROOT / "inputs.json").read_text())
    candidates = json.loads((ROOT / "candidates.json").read_text())
    result = {}
    for label in ["lower_forecasts", "role_uncertainty", "less_variance"]:
        altered = copy.deepcopy(pool)
        for p in altered:
            if label == "lower_forecasts":
                p["mean"] = min(p[k] for k in ["mean", "spags", "fsc", "ftn"] if k in p)
            elif label == "role_uncertainty":
                # These are deliberately adverse analyst alternatives, not measured odds.
                factor = {"Emmett Johnson": .75, "Laquon Treadwell": .75,
                          "Jakobi Meyers": .8, "Deebo Samuel Sr.": .8,
                          "Keenan Allen": .8, "DJ Moore": .8,
                          "George Kittle": .85, "Colby Parkinson": .85,
                          "Tyler Warren": .85}.get(p["name"], 1.)
                p["mean"] *= factor
        scores, _ = simulate(altered, 75000, SEED + 100, .8 if label == "less_variance" else 1.)
        mm = evaluate_candidates(altered, candidates, scores)
        result[label] = [{k: c[k] for k in ["candidate_id", "projection", "p95", "p99", "p_gt_200"]} for c in mm]
    # Explicit correlation and distribution sanity checks on a separate seed.
    scores, _ = simulate(pool, 100000, SEED + 200)
    ids = {p["name"]: i for i, p in enumerate(pool)}
    correlation_pairs = [("Brock Purdy", "George Kittle"), ("Brock Purdy", "Christian McCaffrey"),
                         ("Tyler Shough", "Chris Olave"), ("Dak Prescott", "CeeDee Lamb"),
                         ("Dak Prescott", "George Pickens"), ("Emmett Johnson", "Bijan Robinson")]
    sanity = {"mean_max_abs_error": max(abs(float(scores[:, i].mean()) - p["mean"]) for i, p in enumerate(pool)),
              "pair_correlations": {f"{a} / {b}": round(float(np.corrcoef(scores[:, ids[a]], scores[:, ids[b]])[0, 1]), 4) for a, b in correlation_pairs},
              "all_candidate_rosters_legal": all(validate(c["ids"], pool) for c in candidates),
              "all_numeric_finite": bool(np.isfinite(scores).all()),
              "negative_offense_count": int(np.sum(scores[:, [i for i, p in enumerate(pool) if p["pos"] != "DST"]] < 0)),
              "note": "Offense lacks interceptions/lost-fumble negatives; PPR/yardage/bonuses are approximated in non-TD scores. Injury-exit stresses have no probability weight."}
    assert sanity["all_numeric_finite"] and sanity["mean_max_abs_error"] < .65
    dump("sensitivity_results.json", result)
    dump("simulation_sanity.json", sanity)
    print(json.dumps(sanity, indent=2))


if __name__ == "__main__":
    main()
