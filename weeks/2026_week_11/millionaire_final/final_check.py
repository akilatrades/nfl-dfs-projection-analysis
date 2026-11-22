"""Test the best screened stacks with fewer skill players from one offense."""

import csv
import json

import numpy as np

from simulate import (
    FIELD_SIZE, GAMES, ROOT, SEED, FieldBuilder, comparisons, load_inputs,
    outcome_stats, tournament, validate,
)


def main():
    pool = load_inputs()
    with (ROOT / "final_updates.csv").open() as handle:
        for update in csv.DictReader(handle):
            p = pool[int(update["id"])]
            assert p["name"] == update["name"] and p["mean"] == float(update["previous_mean"])
            p["mean"] = float(update["new_mean"])
            totals = GAMES[p["game"]][1]
            totals[p["team"]] = float(update["team_total"])
            GAMES[p["game"]] = (sum(totals.values()), totals)
    initial = comparisons(pool)
    names = (143, 253, 328, 370, 431, 441, 463, 544, 545, 547)
    lineups = {f"original {i}": initial[f"original {i}"] for i in names}
    variants = {
        "Young, Coleman and Eagles": (441, [22, 109], [21, 108]),
        "Young and Egbuka": (441, [52, 109], [61, 108]),
        "Young, Javonte and LaPorta": (441, [22, 86, 109], [18, 88, 105]),
        "Young, Javonte and Kelce": (441, [22, 86], [18, 87]),
        "Young, Coker and Pickens": (441, [20, 22, 73, 86], [21, 50, 72, 88]),
        "Young, Javonte and Coleman": (441, [20, 22, 109], [18, 21, 105]),
        "Young, Tuten and Egbuka": (441, [22, 52], [25, 61]),
        "Young, Pollard and Godwin": (441, [73, 86, 109], [80, 88, 104]),
        "Young, Pollard and Egbuka": (441, [73, 86, 109], [61, 88, 121]),
        "McCarthy and Egbuka": (545, [64], [61]),
        "McCarthy, Egbuka and Tuten": (545, [22, 64, 105], [25, 61, 108]),
        "McCarthy, Meyers and Broncos": (545, [64, 105], [71, 101]),
        "McCarthy and Parker Washington": (545, [21, 64, 105], [29, 53, 122]),
        "McCarthy, Javonte and LaPorta": (547, [22, 86], [18, 88]),
        "McCarthy, Hubbard and Coleman": (547, [22], [21]),
        "McCarthy, Hubbard and Pickens": (547, [22, 104], [50, 105]),
        "McCarthy, Hubbard and Javonte": (547, [22, 104], [18, 122]),
        "McCarthy, Hubbard and Warren": (547, [22, 104], [23, 105]),
        "McCarthy, Hubbard and Egbuka": (547, [52], [61]),
        "McCarthy, Hubbard and Parker": (547, [22, 104], [53, 105]),
        "McCarthy, Hubbard and Meyers": (547, [22, 73, 104], [21, 71, 108]),
    }
    # All replacements refer to player IDs in the frozen input table. Both
    # duplicate and opponent-DST restrictions are checked before simulation.
    for name, (i, remove, add) in variants.items():
        ids = set(initial[f"original {i}"])
        assert set(remove) <= ids
        selection = sorted((ids - set(remove)) | set(add))
        validate(selection, pool)
        lineups[name] = selection

    draws = 24000
    result = dict(draws=draws, stress_draws=16000, field_size_with_entry=FIELD_SIZE+1,
                  final_projection_board="November 22, 11:59 AM ET",
                  candidates=outcome_stats(pool, lineups), fields={})
    for k, (label, salary, pairing) in enumerate([
        ("replicate", 47500, 0.), ("near_cap", 49400, .16)
    ]):
        builder = FieldBuilder(pool, SEED + 200 + k, 112, True, salary, pairing)
        builder.fit()
        if k:
            builder.floor = 124
        field = builder.draw(FIELD_SIZE, 70000)
        assert all(validate(row.tolist(), pool) for row in field[::130])
        marginal = np.bincount(field.ravel(), minlength=len(pool)) / len(field) * 100
        record = dict(min_salary=salary, min_projection=builder.floor,
                      extra_probability_own_qb_rb_pair=pairing,
                      mean_field_salary=round(float(builder.salary[field].sum(axis=1).mean()), 2),
                      mean_field_projection=round(float(builder.mean[field].sum(axis=1).mean()), 2),
                      realized_ownership={p["name"]: round(float(v), 2) for p, v in zip(pool, marginal)})
        print("Final checks", label, len(lineups), flush=True)
        record["results"] = tournament(pool, lineups, field, draws, SEED+211)
        if k:
            record["run_pass_tradeoff_and_role_stress"] = tournament(
                pool, lineups, field, result["stress_draws"], SEED+217, stress=True, script_stress=True)
            # Likely had a Friday groin absence and no official game designation.
            # Both contenders face identical simulated players in this stress.
            reduced_role = [dict(p) for p in pool]
            next(p for p in reduced_role if p["name"] == "Isaiah Likely")["mean"] *= .75
            pair = {n: lineups[n] for n in ("original 253", "original 547")}
            record["likely_quarter_role_loss"] = tournament(
                reduced_role, pair, field, result["stress_draws"], SEED+219)
        result["fields"][label] = record
    (ROOT / "final_check.json").write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
