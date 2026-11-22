"""Week 11 scenario research. Public means, analyst distributions, synthetic fields.

This is not a calibrated contest-profit model. Run from any working directory.
"""

import argparse
import json
import time
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

ROOT = Path(__file__).resolve().parent
SEED = 20261122
GAMES = {
    "ARI_KC": (40.5, {"KC": 28., "ARI": 12.5}),
    "BAL_CAR": (43.5, {"CAR": 23.25, "BAL": 20.25}),
    "BUF_MIA": (44.5, {"BUF": 30.5, "MIA": 14.}),
    "CHI_NO": (48.5, {"CHI": 30., "NO": 18.5}),
    "PHI_PIT": (37.5, {"PIT": 20.5, "PHI": 17.}),
    "DET_TB": (47.5, {"DET": 25.5, "TB": 22.}),
    "DAL_TEN": (54.5, {"DAL": 31., "TEN": 23.5}),
    "LAC_NYJ": (41.5, {"LAC": 22.25, "NYJ": 19.25}),
    "JAX_NYG": (45.5, {"JAX": 25.75, "NYG": 19.75}),
    "DEN_LV": (41.5, {"DEN": 26., "LV": 15.5}),
}


def dump(name, obj):
    (ROOT / name).write_text(json.dumps(obj, indent=2) + "\n")


def validate(roster, pool):
    assert len(roster) == len(set(roster)) == 9
    ps = [pool[i] for i in roster]
    ct = Counter(p["pos"] for p in ps)
    assert ct["QB"] == ct["DST"] == 1
    assert 2 <= ct["RB"] <= 3 and 3 <= ct["WR"] <= 4 and 1 <= ct["TE"] <= 2
    assert sum(p["salary"] for p in ps) <= 50000
    assert all(p["eligible"] and p["game"] in GAMES for p in ps)
    dst = next(p for p in ps if p["pos"] == "DST")
    assert all(p["team"] != dst["opp"] for p in ps if p["pos"] != "DST")
    return True


def generate_candidates(pool):
    n = len(pool)
    rng = np.random.default_rng(SEED)
    positions = {s: np.array([p["pos"] == s for p in pool], float) for s in ["QB", "RB", "WR", "TE", "DST"]}
    salary = np.array([p["salary"] for p in pool])
    mu = np.array([p["mean"] for p in pool])
    base_rows = [np.ones(n), salary]
    lows, highs = [9, 47000], [9, 50000]
    for pos, lo, hi in [("QB", 1, 1), ("DST", 1, 1), ("RB", 2, 3), ("WR", 3, 4), ("TE", 1, 2)]:
        base_rows.append(positions[pos]); lows.append(lo); highs.append(hi)
    for team in sorted({p["team"] for p in pool}):
        off = np.array([p["team"] == team and p["pos"] != "DST" for p in pool], float)
        base_rows.append(off); lows.append(0); highs.append(3)
    for game in GAMES:
        row = np.array([p["game"] == game and p["pos"] != "DST" for p in pool], float)
        base_rows.append(row); lows.append(0); highs.append(4)
    for j, p in enumerate(pool):
        if p["pos"] == "DST":
            row = np.array([q["team"] == p["opp"] and q["pos"] != "DST" for q in pool], float)
            row[j] = 8
            base_rows.append(row); lows.append(0); highs.append(8)
    thin = np.array([p["pos"] == "WR" and p["mean"] < 9.5 for p in pool], float)
    base_rows.append(thin); lows.append(0); highs.append(1)
    candidates = {}
    for qi, q in enumerate(pool):
        if q["pos"] != "QB":
            continue
        stack = np.array([p["team"] == q["team"] and p["pos"] in ["WR", "TE"] for p in pool], float)
        back = np.array([p["team"] == q["opp"] and p["pos"] != "DST" for p in pool], float)
        if not stack.any():
            continue
        for partners in [1, 2]:
            for tes in [1, 2]:
                for profile in ["median", "spags", "lower_source", "upside", "perturb", "no_emmett", "gibbs", "cook", "no_thin", "role_quality", "no_tate", "no_coleman", "lower_owned"]:
                    rows = list(base_rows) + [stack, positions["TE"]]
                    lo, hi = list(lows) + [partners, tes], list(highs) + [partners, tes]
                    lower = np.zeros(n); upper = np.ones(n)
                    lower[qi] = 1
                    if profile == "no_thin":
                        upper[thin > .5] = 0
                    if profile in ["role_quality", "no_tate", "no_coleman", "lower_owned"]:
                        for k,p in enumerate(pool):
                            if p["pos"] == "TE" and p["mean"] < 9.: upper[k] = 0
                            if p["name"] in ["Darren Waller", "Ja'Kobi Lane"]: upper[k] = 0
                            if profile == "no_tate" and p["name"] == "Carnell Tate": upper[k] = 0
                            if profile == "no_coleman" and p["name"] == "Jonah Coleman": upper[k] = 0
                    if profile == "lower_owned":
                        objective = mu - .05 * np.array([p["candidate_ownership_weight"] for p in pool])
                    elif profile == "spags":
                        objective = np.array([p.get("spags", p["mean"]) for p in pool])
                    elif profile == "lower_source":
                        objective = np.array([min(p.get("spags", p["mean"]), p.get("fsc", p["mean"]), p.get("ftn", p["mean"])) for p in pool])
                    elif profile == "upside":
                        objective = mu + np.array([1.3 * (p["pass_td"] + p["rush_td"]) + (.7 if p["pos"] in ["WR", "TE"] else 0) for p in pool])
                    elif profile == "perturb":
                        objective = mu + rng.normal(0, 1.6, n)
                    else:
                        objective = mu.copy()
                    if profile in ["no_emmett", "gibbs", "cook"]:
                        target = {"no_emmett": "Emmett Johnson", "gibbs": "Jahmyr Gibbs", "cook": "James Cook III"}[profile]
                        k = next(i for i, p in enumerate(pool) if p["name"] == target)
                        if profile == "no_emmett": upper[k] = 0
                        else: lower[k] = 1
                    # Alternate profiles explicitly compare a credible run-back, never a global requirement.
                    if profile == "upside":
                        rows.append(back); lo.append(1); hi.append(3)
                    out = milp(-objective, integrality=np.ones(n), bounds=Bounds(lower, upper), constraints=LinearConstraint(np.array(rows), lo, hi), options={"time_limit": 2.0, "mip_rel_gap": .001})
                    if out.x is None:
                        continue
                    roster = tuple(np.flatnonzero(out.x > .5).tolist())
                    validate(roster, pool)
                    if roster not in candidates:
                        candidates[roster] = {"ids": list(roster), "family": q["name"], "partners": partners, "tes": tes, "profiles": []}
                    candidates[roster]["profiles"].append(profile)
    # A portfolio alternative removes Ayomanor rather than sharing the same cheap WR.
    recipes = [
        ["Cam Ward", "Jahmyr Gibbs", "Emmett Johnson", "Jonah Coleman", "Carnell Tate", "Emeka Egbuka", "Jakobi Meyers", "Sam LaPorta", "Jets"],
        ["Cam Ward", "Jahmyr Gibbs", "Emmett Johnson", "Jonah Coleman", "Elic Ayomanor", "George Pickens", "Jakobi Meyers", "Sam LaPorta", "Jets"],
    ]
    by_name = {p['name']:i for i,p in enumerate(pool)}
    for names in recipes:
        roster = tuple(sorted(by_name[name] for name in names))
        validate(roster,pool)
        if roster not in candidates:
            candidates[roster] = {'ids':list(roster),'family':'Cam Ward','partners':1,'tes':1,'profiles':['portfolio_alternative']}
    result = list(candidates.values())
    for i, c in enumerate(result): c["candidate_id"] = i
    return result


def simulate(pool, draws, seed=SEED + 1, variance_scale=1.0):
    """Shared team TD counts allocated once to recipients plus an unrostered residual.

    QB gets the same team passing TD count. Non-TD score is a correlated gamma
    approximation that includes yardage/PPR/bonuses; it is not a play-by-play model.
    All means, TD rates, lognormal loadings and gamma shapes are explicit assumptions.
    """
    rng = np.random.default_rng(seed)
    scores = np.zeros((draws, len(pool)), np.float32)
    td = np.zeros_like(scores)
    teams = sorted({p["team"] for p in pool})
    game_factor = {g: np.exp(rng.normal(-.5 * (.20 * variance_scale) ** 2, .20 * variance_scale, draws)) for g in GAMES}
    meta = {}
    for team in teams:
        pp = [i for i, p in enumerate(pool) if p["team"] == team and p["pos"] != "DST"]
        if not pp: continue
        game = pool[pp[0]]["game"]
        total = GAMES[game][1][team]
        passing_mean = total * .8 / 7 * .65
        rushing_mean = total * .8 / 7 * .35
        team_factor = np.exp(rng.normal(-.5 * (.22 * variance_scale) ** 2, .22 * variance_scale, draws))
        factor = game_factor[game] * team_factor
        pass_idx = [i for i in pp if pool[i]["pass_td"] > 0]
        rush_idx = [i for i in pp if pool[i]["rush_td"] > 0]
        actual_rates = {}
        totals = {}
        for mode, inds, rate in [("pass_td", pass_idx, passing_mean), ("rush_td", rush_idx, rushing_mean)]:
            raw = np.array([pool[i][mode] for i in inds])
            # Leave >=10% of TD expectation for players outside this curated pool.
            raw *= min(1., .9 * rate / max(raw.sum(), 1e-9))
            count = rng.poisson(rate * factor)
            totals[mode] = count.copy()
            remain = count.copy(); remaining_rate = rate
            for i, lam in zip(inds, raw):
                alloc = rng.binomial(remain, min(float(lam / remaining_rate), 1.))
                remain -= alloc; remaining_rate -= lam
                td[:, i] += 6 * alloc
                actual_rates.setdefault(i, 0.)
                actual_rates[i] += 6 * float(lam)
            assert np.all(remain >= 0)
        for i in pp:
            p = pool[i]
            expected_td = actual_rates.get(i, 0.)
            if p["pos"] == "QB":
                td[:, i] += 4 * totals["pass_td"]
                expected_td += 4 * passing_mean
            nondtd = max(p["mean"] - expected_td, .5)
            shape = {"QB": 8., "RB": 5., "WR": 3., "TE": 2.5}[p["pos"]] / variance_scale ** 2
            production = rng.gamma(shape, nondtd / shape, draws) * factor
            # Genuine zero-production events for pass catchers, not always-positive outputs.
            if p["pos"] in ["WR", "TE"]:
                zero_p = .015 if p["mean"] >= 13 else .04 if p["mean"] >= 9 else .10
                production *= (rng.random(draws) >= zero_p) / (1 - zero_p)
            scores[:, i] = production + td[:, i]
            meta[p["name"]] = {"mean_target": p["mean"], "expected_td_points": expected_td, "non_td_mean": nondtd}
    for i, p in enumerate(pool):
        if p["pos"] != "DST": continue
        # Centered sack/turnover/TD mixture, plus points-allowed uncertainty.
        base = rng.poisson(2.5, draws) + 2 * rng.poisson(1.0, draws) + 6 * rng.binomial(1, .12, draws) + rng.normal(0, 2.0 * variance_scale, draws)
        scores[:, i] = base - 5.22 + p["mean"]
    return scores, meta


def evaluate_candidates(pool, candidates, scores):
    ids = np.array([c["ids"] for c in candidates])
    vals = np.zeros((len(scores), len(candidates)), np.float32)
    for slot in range(9): vals += scores[:, ids[:, slot]]
    metrics = []
    for j, c in enumerate(candidates):
        ps = [pool[i] for i in c["ids"]]
        v = vals[:, j]
        stress = sum(p["mean"] * (.75 if p["name"] == "Emmett Johnson" else .80 if p["name"] in ["Carnell Tate", "Dawson Knox", "Brevyn Spann-Ford", "Elic Ayomanor"] else 1) for p in ps)
        qteam = next(p["team"] for p in ps if p["pos"] == "QB")
        qb_exit = sum(p["mean"] * (.15 if p["pos"] == "QB" else .65 if p["team"] == qteam and p["pos"] in ["WR", "TE"] else .9 if p["team"] == qteam and p["pos"] == "RB" else 1) for p in ps)
        metrics.append({**c, "names": [p["name"] for p in ps], "salary": sum(p["salary"] for p in ps), "projection": round(sum(p["mean"] for p in ps), 3), "sim_mean": round(float(v.mean()), 3), **{f"p{k}": round(float(np.percentile(v, k)), 2) for k in [10, 50, 90, 95, 99]}, **{f"p_gt_{k}": round(float(np.mean(v >= k)), 6) for k in [160, 180, 200, 220]}, "ownership_sum": round(sum(p["own"] for p in ps), 2), "role_stress_mean": round(stress, 3), "qb_exit_stress_mean": round(qb_exit, 3), "thin_receivers": [p["name"] for p in ps if p["pos"] == "WR" and p["mean"] < 9.5]})
    return metrics


def generate_field(pool, count, rng, temperature=1.0, fitted_weights=None, min_projection=None):
    """Plausible legal lineups, not a reconstructed DraftKings opponent field.

    Salary rejection and stacking induce differences between requested popularity
    weights and realized marginals. Save both; never call the input weights actual
    ownership or use an independence product as a duplicate probability.
    """
    n = len(pool)
    pos = {s: np.array([i for i, p in enumerate(pool) if p["pos"] == s]) for s in ["QB", "RB", "WR", "TE", "DST"]}
    weights = (np.array([max(p["own"], .5) for p in pool]) ** temperature if fitted_weights is None else fitted_weights)
    salaries = np.array([p["salary"] for p in pool])
    means = np.array([p["mean"] for p in pool])
    rosters = []
    attempts = 0
    while len(rosters) < count:
        attempts += 1
        chosen = []
        q = int(rng.choice(pos["QB"], p=weights[pos["QB"]] / weights[pos["QB"]].sum()))
        chosen.append(q)
        # RB/WR/TE flex mix is an assumption and is varied in the field sensitivity.
        counts = {"RB": 2, "WR": 3, "TE": 1, "DST": 1}
        flex = rng.choice(["RB", "WR", "TE"], p=[.45, .35, .20]); counts[flex] += 1
        stack_ids = np.array([i for i, p in enumerate(pool) if p["team"] == pool[q]["team"] and p["pos"] in ["WR", "TE"]])
        nstack = min(len(stack_ids), int(rng.choice([0, 1, 2], p=[.12, .65, .23])))
        if nstack:
            picked = rng.choice(stack_ids, nstack, replace=False, p=weights[stack_ids] / weights[stack_ids].sum()).tolist()
            for i in picked: counts[pool[i]["pos"]] -= 1
            if min(counts.values()) < 0: continue
            chosen += picked
        if rng.random() < .5:
            avail = np.array([i for i, p in enumerate(pool) if p["team"] == pool[q]["opp"] and p["pos"] in ["RB", "WR", "TE"] and counts[p["pos"]] > 0])
            if len(avail):
                i = int(rng.choice(avail, p=weights[avail] / weights[avail].sum()))
                chosen.append(i); counts[pool[i]["pos"]] -= 1
        # Preserve the extreme chalk branch without requiring it in every entry.
        emmett = next(i for i, p in enumerate(pool) if p["name"] == "Emmett Johnson")
        if counts["RB"] and emmett not in chosen and rng.random() < .20:
            chosen.append(emmett); counts["RB"] -= 1
        for s, cnt in counts.items():
            avail = np.array([i for i in pos[s] if i not in chosen])
            if cnt: chosen += rng.choice(avail, cnt, replace=False, p=weights[avail] / weights[avail].sum()).tolist()
        if salaries[chosen].sum() < 47500 or salaries[chosen].sum() > 50000: continue
        if min_projection is not None and means[chosen].sum() < min_projection: continue
        ps = [pool[i] for i in chosen]
        d = next(p for p in ps if p["pos"] == "DST")
        if any(p["team"] == d["opp"] for p in ps if p["pos"] != "DST"): continue
        if max(Counter(p["team"] for p in ps if p["pos"] != "DST").values()) > 3: continue
        roster = sorted(chosen)
        validate(roster, pool)
        rosters.append(roster)
        if len(rosters) % 4000 == 0: print("field", len(rosters), "attempts", attempts, flush=True)
    field = np.array(rosters, dtype=np.int32)
    marginal = np.bincount(field.ravel(), minlength=n) / count * 100
    return field, {"attempts": attempts, "temperature": temperature, "marginals": [{"name": p["name"], "input_weight": p["own"], "realized_pct": round(float(marginal[i]), 2)} for i, p in enumerate(pool)]}


def fit_field_weights(pool, temperature):
    """Match synthetic marginal exposures to assumed targets, not historical outcomes."""
    weights = np.array([max(p["own"], .5) for p in pool]) ** temperature
    targets = np.array([p["own"] for p in pool], float)
    for pos, total in [("QB", 100.), ("DST", 100.), ("RB", 245.), ("WR", 335.), ("TE", 120.)]:
        known = np.array([p["pos"] == pos and "published_ownership" in p for p in pool])
        unknown = np.array([p["pos"] == pos and "published_ownership" not in p for p in pool])
        targets[unknown] *= max(total - targets[known].sum(), 1.) / targets[unknown].sum()
    history = []
    for iteration in range(5):
        f, audit = generate_field(pool, 2500, np.random.default_rng(SEED + 50 + iteration), fitted_weights=weights)
        actual = np.bincount(f.ravel(), minlength=len(pool)) / len(f) * 100
        history.append({"iteration": iteration, "max_target_error_pp": float(np.max(np.abs(actual - targets)))})
        weights *= np.clip(targets / np.maximum(actual, .3), .4, 2.5) ** .65
        print("field exposure fit", iteration, round(history[-1]["max_target_error_pp"], 2), flush=True)
    return weights, targets, history


def field_evaluate(pool, finalists, field, draws, seed):
    rng = np.random.default_rng(seed)
    counters = {size: {c["candidate_id"]: dict(first_share=0., top1=0, top10=0, beat_fraction=0.) for c in finalists} for size in [5882, 12254]}
    ci = np.array([c["ids"] for c in finalists])
    corr_data = []
    for start in range(0, draws, 200):
        m = min(200, draws - start)
        scores, _ = simulate(pool, m, seed=int(rng.integers(1, 2**31)))
        fs = np.zeros((m, len(field)), np.float32)
        cs = np.zeros((m, len(finalists)), np.float32)
        for j in range(9):
            fs += scores[:, field[:, j]]
            cs += scores[:, ci[:, j]]
        corr_data.append(cs)
        for size in counters:
            subset = fs[:, :size - 1]
            mx = subset.max(axis=1)
            for j, c in enumerate(finalists):
                v = cs[:, j]
                greater = np.sum(subset > v[:, None] + .0001, axis=1)
                equal = np.sum(np.abs(subset - v[:, None]) <= .0001, axis=1)
                z = counters[size][c["candidate_id"]]
                z["first_share"] += float(np.sum(np.where(greater == 0, 1 / (equal + 1), 0)))
                z["top1"] += int(np.sum(greater < max(1, size // 100)))
                z["top10"] += int(np.sum(greater < max(1, size // 10)))
                z["beat_fraction"] += float(np.sum(1 - greater / (size - 1)))
        if (start + m) % 2000 == 0: print("field scenarios", start + m, flush=True)
    for size, entries in counters.items():
        for cid, z in entries.items():
            for k in z: z[k] = round(z[k] / draws, 7)
    corr = np.corrcoef(np.concatenate(corr_data), rowvar=False)
    duplicates = {c["candidate_id"]: sum(tuple(r) == tuple(sorted(c["ids"])) for r in field.tolist()) for c in finalists}
    return {"draws": draws, "field_sizes": counters, "candidate_order": [c["candidate_id"] for c in finalists], "score_correlation": corr.round(4).tolist(), "exact_matches_in_synthetic_field": duplicates}


def main():
    args = argparse.ArgumentParser()
    args.add_argument("--draws", type=int, default=150000)
    args.add_argument("--field-draws", type=int, default=6000)
    args.add_argument("--phase", choices=["screen", "field", "all"], default="all")
    a = args.parse_args()
    start = time.time()
    pool = json.loads((ROOT / "inputs.json").read_text())
    if a.phase in ["screen", "all"]:
        candidates = generate_candidates(pool)
        dump("candidates.json", candidates)
        print("legal candidates", len(candidates), flush=True)
        scores, meta = simulate(pool, a.draws)
        metrics = evaluate_candidates(pool, candidates, scores)
        dump("simulation_metrics.json", metrics)
        dump("model_components.json", meta)
        # A held-out seed separates candidate screening from the field comparison.
        top = sorted(metrics, key=lambda x: x["p_gt_200"], reverse=True)
        for row in top[:16]: print(row["candidate_id"], row["family"], row["tes"], row["salary"], row["projection"], row["p95"], row["p_gt_200"], row["names"], flush=True)
        finalists = []
        for family in sorted({r["family"] for r in metrics}):
            for tes in [1, 2]:
                subset = [r for r in top if r["family"] == family and r["tes"] == tes]
                if subset: finalists.append(subset[0])
        for r in top:
            if r["candidate_id"] not in {c["candidate_id"] for c in finalists}: finalists.append(r)
            if len(finalists) >= 38: break
        ids = {c['candidate_id'] for c in finalists}
        for c in metrics:
            if set(c['profiles']) & {'role_quality','no_tate','no_coleman','lower_owned'} and c['candidate_id'] not in ids and c['projection'] >= 137:
                finalists.append(c); ids.add(c['candidate_id'])
        dump("finalists.json", finalists)
        maxerr = max(abs(float(scores[:, i].mean()) - p["mean"]) for i, p in enumerate(pool))
        assert maxerr < .6, f"Mean mismatch: {maxerr}"
        dump("verification.json", {"all_rosters_legal": True, "max_sim_mean_error": maxerr, "seed": SEED, "screen_draws": a.draws, "candidate_count": len(candidates), "source_model": "public median forecasts, analyst conditional score scenarios"})
    if a.phase in ["field", "all"]:
        finalists = json.loads((ROOT / "finalists.json").read_text())
        for temp, label in [(1.0, "base"), (.7, "flatter")]:
            weights, targets, fit_history = fit_field_weights(pool, temp)
            field, meta = generate_field(pool, 12253, np.random.default_rng(SEED + (3 if label == "base" else 4)), temp, fitted_weights=weights)
            meta["fit_history"] = fit_history
            meta["targets"] = targets.tolist()
            np.save(ROOT / f"field_{label}.npy", field)
            dump(f"field_{label}_audit.json", meta)
            result = field_evaluate(pool, finalists, field, a.field_draws, SEED + 10)
            dump(f"field_{label}_results.json", result)
    print("seconds", round(time.time() - start, 1), flush=True)


if __name__ == "__main__":
    main()
