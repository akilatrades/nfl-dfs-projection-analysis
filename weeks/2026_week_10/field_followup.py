"""Compare football-screened alternatives and a stronger hypothetical opponent field."""

import json

import numpy as np

from run import ROOT, SEED, dump, field_evaluate, generate_field


def main():
    pool = json.loads((ROOT / "inputs.json").read_text())
    rows = json.loads((ROOT / "simulation_metrics.json").read_text())
    finalists = []
    for family in ["Brock Purdy", "Dak Prescott", "Tyler Shough", "Michael Penix Jr.", "Drew Lock"]:
        for tes in [1, 2]:
            for no_thin in [False, True]:
                subset = [r for r in rows if r["family"] == family and r["tes"] == tes and (not no_thin or not r["thin_receivers"])]
                if subset:
                    best = max(subset, key=lambda r: r["p_gt_200"])
                    if best["candidate_id"] not in [c["candidate_id"] for c in finalists]: finalists.append(best)
    # Preserve the explicit Bijan versus CMC and one-catcher versus two-catcher comparisons.
    for family, must, avoid in [("Brock Purdy", "Bijan Robinson", "Laquon Treadwell"),
                                ("Tyler Shough", "Travis Kelce", "Laquon Treadwell")]:
        subset = [r for r in rows if r["family"] == family and must in r["names"] and avoid not in r["names"]]
        if subset:
            best = max(subset, key=lambda r: r["p_gt_200"])
            if best["candidate_id"] not in [c["candidate_id"] for c in finalists]: finalists.append(best)
    out = {}
    for label in ["base", "flatter"]:
        field = np.load(ROOT / f"field_{label}.npy")
        out[label] = field_evaluate(pool, finalists, field, 10000, SEED + 10)
    # This deliberately raises opposing projection quality. Ownership will differ;
    # audit it rather than describing it as a faithful copy of either real contest.
    field, audit = generate_field(pool, 12253, np.random.default_rng(SEED + 300), min_projection=130.)
    np.save(ROOT / "field_stronger.npy", field)
    dump("field_stronger_audit.json", audit)
    out["stronger"] = field_evaluate(pool, finalists, field, 10000, SEED + 10)
    dump("field_followup_results.json", out)
    print("field followup complete", flush=True)


if __name__ == "__main__":
    main()
