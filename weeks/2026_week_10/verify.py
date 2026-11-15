"""Validate the frozen slate, actual roster rules and deterministic score machinery."""

import hashlib
import json
from collections import Counter

import numpy as np
import scipy

from run import GAMES, ROOT, SEED, dump, simulate, validate


def main():
    pool = json.loads((ROOT / "inputs.json").read_text())
    candidates = json.loads((ROOT / "candidates.json").read_text())
    recommendation = json.loads((ROOT / "recommendations.json").read_text())
    assert len(pool) == len({p["name"] for p in pool}) == 102
    assert sum(p["pos"] == "QB" for p in pool) == 20
    assert len({p["game"] for p in pool}) == len(GAMES) == 10
    assert all(p["salary"] > 0 and p["salary"] % 100 == 0 for p in pool)
    assert not {"Jordan Addison", "Kenneth Walker III", "Puka Nacua", "Mike Evans"} & {p["name"] for p in pool}
    for c in candidates:
        validate(c["ids"], pool)
        ps = [pool[i] for i in c["ids"]]
        qb = next(p for p in ps if p["pos"] == "QB")
        assert qb["name"] == c["family"]
        assert sum(p["team"] == qb["team"] and p["pos"] in ["WR", "TE"] for p in ps) == c["partners"]
        assert max(Counter(p["team"] for p in ps if p["pos"] != "DST").values()) <= 3
        assert max(Counter(p["game"] for p in ps if p["pos"] != "DST").values()) <= 4
    for e in recommendation["lineups"]:
        assert e["entry_fee"] == 12
        assert e["max_entries"] in [5882, 12254]
        ids = [p["id"] for p in e["players"]]
        validate(ids, pool)
        slots = Counter(p["slot"] for p in e["players"])
        assert slots == {"QB": 1, "RB": 2, "WR": 3, "TE": 1, "FLEX": 1, "DST": 1}
        for p in e["players"]:
            assert p["slot"] == p["pos"] or p["slot"] == "FLEX" and p["pos"] in ["RB", "WR", "TE"]
        assert e["salary"] == sum(p["salary"] for p in e["players"]) == 50000
    assert recommendation["portfolio"]["shared_players"] == ["Emmett Johnson", "Tyler Warren"]
    assert len({c["family"] for c in recommendation["conditional_score_simulation"]}) == 2
    sanity = json.loads((ROOT / "simulation_sanity.json").read_text())
    assert sanity["mean_max_abs_error"] < .65
    x, _ = simulate(pool, 64, SEED + 900)
    y, _ = simulate(pool, 64, SEED + 900)
    assert np.array_equal(x, y) and np.isfinite(x).all()
    result = {"passed": True, "players": len(pool), "legal_candidates": len(candidates),
              "selected_salary_checks": True, "selected_slot_checks": True,
              "main_slate_only": True, "known_out_exclusions": True,
              "qb_pairing_and_concentration_checks": True,
              "deterministic_seed_check": True,
              "independent_mean_sanity_error": sanity["mean_max_abs_error"],
              "numpy_version": np.__version__, "scipy_version": scipy.__version__}
    dump("verification.json", result)
    # Refresh hashes after formatting without rewriting the pre-lock decision timestamp.
    manifest = json.loads((ROOT / "manifest.json").read_text())
    files = list(manifest["sha256"])
    for f in ["field_followup.py", "verify.py", "README.md", "lessons_applied.md", "sources.md", "lineups.csv"]:
        if f not in files: files.append(f)
    manifest["sha256"] = {f: hashlib.sha256((ROOT / f).read_bytes()).hexdigest() for f in files}
    manifest["verification"] = result
    dump("manifest.json", manifest)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
