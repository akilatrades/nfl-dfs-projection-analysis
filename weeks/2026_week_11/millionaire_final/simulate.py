"""Pre-lock Week 11 Millionaire comparison, using frozen public inputs."""

import csv
import json
import sys
from pathlib import Path

import numpy as np
from scipy.sparse import csr_matrix
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))
from run import GAMES, simulate, validate

SEED = 11222026
FIELD_SIZE = 147057
POSITIONS = ("QB", "RB", "WR", "TE", "DST")
FLEX_MIX = (.52, .39, .09)


def load_inputs():
    with (ROOT / "inputs.csv").open() as handle:
        pool = list(csv.DictReader(handle))
    for i, p in enumerate(pool):
        assert i == int(p["id"])
        p.update(id=i, eligible=True, salary=int(p["salary"]))
        for key in ("mean", "pass_td", "rush_td", "own", "millionaire_own", "cover_own"):
            p[key] = float(p[key]) if p[key] else None
        if p["team_total"]:
            GAMES[p["game"]][1][p["team"]] = float(p["team_total"])
    for game, (_, totals) in list(GAMES.items()):
        GAMES[game] = (sum(totals.values()), totals)
    return pool


def comparisons(pool):
    earlier = json.loads((ROOT.parent / "candidates.json").read_text())
    lineups = {}
    for item in earlier:
        lineups[f"original {item['candidate_id']}"] = item["ids"]
    changes = {
        "Meyers": ([65], [71]),
        "Douglas": ([65], [69]),
        "Godwin and Steelers": ([65, 105], [80, 104]),
        "Meyers and Panthers": ([65, 105], [71, 106]),
        "Egbuka, Strange and Eagles": ([65, 88, 105], [61, 89, 108]),
        "Egbuka, Pickens and Eagles": ([65, 18, 105], [61, 50, 108]),
        "Pickens and Jaguars": ([18, 105], [50, 103]),
        "Pickens and McConkey": ([18, 65], [50, 78]),
        "Lamb, Otton and Jets": ([18, 88, 105], [48, 91, 109]),
        "Washington and Egbuka": ([18, 65], [53, 61]),
        "Coleman and Egbuka": ([18, 65], [21, 61]),
        "Coleman, Egbuka and Steelers": ([18, 65, 105], [21, 61, 104]),
        "Egbuka, LaPorta and Giants": ([65, 105], [61, 121]),
        "Godwin and Kelce": ([65, 88], [80, 87]),
        "Meyers, Kelce and Eagles": ([65, 88, 105], [71, 87, 108]),
        "Chimere Dike and Sutton": ([73, 65], [130, 76]),
    }
    baseline = set(earlier[253]["ids"])
    for name, (remove, add) in changes.items():
        lineups[name] = sorted((baseline - set(remove)) | set(add))
    lineups.update({
        "Detroit and Javonte": [8, 17, 18, 21, 49, 61, 73, 88, 108],
        "Detroit and Tate": [8, 17, 22, 29, 49, 52, 61, 88, 108],
        "Detroit and Gibbs": [8, 16, 17, 50, 52, 61, 73, 88, 121],
        "Detroit and Pickens": [8, 17, 21, 49, 50, 61, 73, 88, 104],
        "Detroit and Pollard": [8, 17, 21, 22, 49, 61, 73, 88, 103],
        "Detroit and Nabers": [8, 17, 21, 49, 51, 61, 73, 88, 109],
    })
    for ids in lineups.values():
        validate(ids, pool)
    seen = set()
    unique = {}
    for name, ids in lineups.items():
        key = tuple(sorted(ids))
        if key not in seen:
            unique[name] = list(key)
            seen.add(key)
    return unique


def distribution(pool, contest, expected_salary=49.15):
    own = np.array([p["own"] if contest else p["cover_own"] for p in pool])
    target = own.copy()
    # Preserve the available contest forecasts and published fallback on the roster.
    fixed = np.array([p["millionaire_own"] is not None
                      or p["id"] in (6, 16, 18, 65, 88, 105) for p in pool])
    price = np.array([p["salary"] / 1000 for p in pool])
    residual = []
    for pos, total in zip(POSITIONS, (100, 252, 339, 109, 100)):
        mask = np.array([p["pos"] == pos for p in pool])
        scale = (total - own[mask & fixed].sum()) / own[mask & ~fixed].sum()
        target[mask & ~fixed] *= scale
        residual.append(mask & ~fixed)

    # The mixed public marginals imply more than $50k. Adjust other players
    # within position until their expected roster salary is feasible.
    def affordable(tilt):
        adjusted = target.copy()
        for mask in residual:
            w = target[mask] * np.exp(tilt * (price[mask] - price[mask].mean()))
            adjusted[mask] = w * target[mask].sum() / w.sum()
        return adjusted

    tilt = brentq(lambda v: np.dot(affordable(v), price) / 100 - expected_salary, -3, 3)
    return affordable(tilt)


class FieldBuilder:
    def __init__(self, pool, seed, floor, contest, salary_floor=47500, rb_pair=0.):
        self.pool = pool
        self.rng = np.random.default_rng(seed)
        self.floor = floor
        self.salary_floor = salary_floor
        self.rb_pair = rb_pair
        self.target = distribution(pool, contest, 49.7 if salary_floor >= 49400 else 49.15)
        self.weights = self.target.copy()
        self.position = np.array([p["pos"] for p in pool])
        self.salary = np.array([p["salary"] for p in pool])
        self.mean = np.array([p["mean"] for p in pool])
        team_ids = {s: i for i, s in enumerate(sorted({p["team"] for p in pool}))}
        self.team = np.array([team_ids[p["team"]] for p in pool])
        self.opp = np.array([team_ids[p["opp"]] for p in pool])
        self.by_pos = {s: np.flatnonzero(self.position == s) for s in POSITIONS}
        self.history = []

    def pick(self, ids, n):
        w = self.weights[ids]
        return self.rng.choice(ids, size=n, p=w / w.sum())

    def proposals(self, n):
        # Fixed slots: QB, two RBs, three WRs, TE, flex, DST.
        roster = np.empty((n, 9), dtype=np.int32)
        slots = ("QB", "RB", "RB", "WR", "WR", "WR", "TE", None, "DST")
        for j, pos in enumerate(slots):
            if pos:
                roster[:, j] = self.pick(self.by_pos[pos], n)
        flex = self.rng.choice(["RB", "WR", "TE"], n, p=FLEX_MIX)
        for pos in ("RB", "WR", "TE"):
            mask = flex == pos
            roster[mask, 7] = self.pick(self.by_pos[pos], mask.sum())

        stack = self.rng.choice([0, 1, 2], n, p=[.12, .57, .31])
        bring = self.rng.random(n) < .47
        for qb in self.by_pos["QB"]:
            qmask = roster[:, 0] == qb
            if self.rb_pair:
                chosen_rows = np.flatnonzero(qmask & (self.rng.random(n) < self.rb_pair))
                backs = np.flatnonzero((self.team == self.team[qb]) & (self.position == "RB"))
                if len(backs) and len(chosen_rows):
                    roster[chosen_rows, 2] = self.pick(backs, len(chosen_rows))
            catchers = np.flatnonzero((self.team == self.team[qb]) &
                                      np.isin(self.position, ("WR", "TE")))
            first = np.flatnonzero(qmask & (stack > 0))
            if len(catchers) and len(first):
                chosen = self.pick(catchers, len(first))
                first_slot = np.where(self.position[chosen] == "TE", 6, 3)
                roster[first, first_slot] = chosen
                second = first[stack[first] == 2]
                # Sample the second catcher independently, reject duplicate players later.
                previous = roster[second, 6]
                for te_taken in (True, False):
                    rows = second[(self.team[previous] == self.team[qb]) == te_taken]
                    available = catchers[self.position[catchers] == "WR"] if te_taken else catchers
                    if len(rows) and len(available):
                        chosen = self.pick(available, len(rows))
                        second_slot = np.where(self.position[chosen] == "TE", 6, 4)
                        roster[rows, second_slot] = chosen
            rows = np.flatnonzero(qmask & bring)
            opponent = np.flatnonzero((self.team == self.opp[qb]) &
                                      np.isin(self.position, ("RB", "WR")))
            if len(rows) and len(opponent):
                chosen = self.pick(opponent, len(rows))
                roster[rows, np.where(self.position[chosen] == "RB", 1, 5)] = chosen

        salary = self.salary[roster].sum(axis=1)
        offensive_teams = self.team[roster[:, :8]]
        ordered_teams = np.sort(offensive_teams, axis=1)
        valid = ((salary >= self.salary_floor) & (salary <= 50000) &
                 (self.mean[roster].sum(axis=1) >= self.floor) &
                 (offensive_teams != self.opp[roster[:, 8], None]).all(axis=1) &
                 (ordered_teams[:, 4:] != ordered_teams[:, :-4]).all(axis=1))
        roster = np.sort(roster[valid], axis=1)
        return roster[(np.diff(roster, axis=1) != 0).all(axis=1)]

    def draw(self, n, batch):
        output = []
        remaining = n
        while remaining:
            proposal = self.proposals(batch)
            keep = proposal[:remaining]
            if len(keep):
                output.append(keep)
                remaining -= len(keep)
        return np.concatenate(output)

    def fit(self):
        for _ in range(10):
            sample = self.draw(9000, 40000)
            actual = np.bincount(sample.ravel(), minlength=len(self.pool)) / len(sample) * 100
            self.history.append(round(float(np.max(np.abs(self.target - actual))), 2))
            self.weights *= np.clip(self.target / np.maximum(actual, .15), .45, 2.3) ** .78


def outcome_stats(pool, lineups, count=100000):
    ids = np.array(list(lineups.values()))
    scores, _ = simulate(pool, count, SEED + 31)
    stats = {}
    for name, ix in zip(lineups, ids):
        values = scores[:, ix].sum(axis=1)
        q = np.quantile(values, [.5, .95, .99])
        stats[name] = dict(roster=[pool[i]["name"] for i in ix],
                           salary=sum(pool[i]["salary"] for i in ix),
                           projected=round(sum(pool[i]["mean"] for i in ix), 2),
                           median=round(float(q[0]), 2),
                           p95=round(float(q[1]), 2), p99=round(float(q[2]), 2),
                           pct_200=round(float(np.mean(values >= 200) * 100), 3))
    return stats


def tournament(pool, lineups, field, draws, seed, stress=False, script_stress=False):
    ids = np.array(list(lineups.values()))
    # All entries receive the same realized player performances on each slate.
    # Scores in integer DK hundredths avoid floating-order tie errors.
    matrix = csr_matrix((np.ones(field.size, dtype=np.int32), field.ravel(),
                         np.arange(0, field.size + 1, 9, dtype=np.int32)),
                        shape=(len(field), len(pool)))
    score, _ = simulate(pool, draws, seed)
    if script_stress:
        # A mean-preserving sensitivity for passing vs. rushing game scripts.
        # Opposite multipliers test the cost of needing a team's RB and QB together.
        rng = np.random.default_rng(seed + 1)
        for team in sorted({p["team"] for p in pool}):
            tilt = (.40 * np.tanh(rng.normal(size=draws))).astype(np.float32)
            for p in pool:
                if p["team"] == team and p["pos"] != "DST":
                    sign = -1 if p["pos"] == "RB" else 1
                    score[:, p["id"]] *= 1 + sign * tilt
    if stress:
        factors = np.ones(len(pool))
        for p in pool:
            if p["team"] in ("CHI", "NO") and p["pos"] in ("QB", "WR", "TE"):
                factors[p["id"]] = .90
            if p["name"] == "Carnell Tate":
                factors[p["id"]] = .80
            if p["name"] == "Emmett Johnson":
                factors[p["id"]] = .90
        score *= factors.astype(np.float32)
    score = np.rint(score * 100).astype(np.int32)
    ranks = np.array([1, 15, 147, 1470])
    counts = np.zeros((len(ids), len(ranks)), dtype=int)
    split = np.zeros(len(ids))
    for block in range(0, draws, 48):
        batch = score[block:block + 48]
        candidate = batch[:, ids].sum(axis=2)
        games = (matrix @ np.ascontiguousarray(batch.T)).T.copy()
        games.partition(len(field) - ranks, axis=1)
        cutoffs = games[:, len(field) - ranks]
        counts += (candidate[:, :, None] >= cutoffs[:, None, :]).sum(axis=0)
        match = candidate == cutoffs[:, :1]
        alone = candidate > cutoffs[:, :1]
        tied = (games == cutoffs[:, :1]).sum(axis=1)
        split += (alone + match / (1 + tied[:, None])).sum(axis=0)
    # A sorted row has a unique byte key for an exact nine-player lineup.
    row_type = np.dtype((np.void, field.dtype.itemsize * field.shape[1]))
    field_keys = np.ascontiguousarray(field).view(row_type).ravel()
    keys, frequencies = np.unique(field_keys, return_counts=True)
    duplicate_counts = {k.tobytes(): int(n) for k, n in zip(keys, frequencies)}
    return {name: {**{f"top_{r}": int(c) for r, c in zip(ranks, row)},
                   "split_first_equivalent": round(float(s), 3),
                   "exact_opponent_copies": duplicate_counts.get(np.sort(ix).astype(field.dtype).tobytes(), 0)}
            for name, ix, row, s in zip(lineups, ids, counts, split)}


def main():
    pool = load_inputs()
    lineups = comparisons(pool)
    screen_draws, final_draws = 6000, 24000
    result = dict(seed=SEED, screening_draws=screen_draws, draws_per_field=final_draws,
                  screened_lineups=len(lineups), standalone_draws=100000,
                  opposing_entries=FIELD_SIZE, pool=len(pool), games=GAMES,
                  candidates={}, fields={})
    fields, screens = {}, {}
    for idx, (name, floor, use_contest) in enumerate([
        ("millionaire", 112, True), ("projection_conscious", 130, False)
    ]):
        builder = FieldBuilder(pool, SEED + idx, 112, use_contest)
        builder.fit()
        builder.floor = floor
        field = builder.draw(FIELD_SIZE, 65000)
        assert all(validate(ids.tolist(), pool) for ids in field[::91])
        print(name, "generated", len(field), "opponents", flush=True)
        realized = np.bincount(field.ravel(), minlength=len(pool)) / len(field) * 100
        metrics = tournament(pool, lineups, field, screen_draws, SEED + 45)
        record = dict(min_projection=floor, calibration_history=builder.history,
                      mean_field_projection=round(float(builder.mean[field].sum(axis=1).mean()), 2),
                      mean_salary=round(float(builder.salary[field].sum(axis=1).mean()), 2),
                      target_and_realized_ownership={p["name"]: [round(float(t), 2), round(float(r), 2)]
                                                     for p, t, r in zip(pool, builder.target, realized)},
                      screening_top_147=sorted(
                          [(k, v["top_147"], v["top_15"]) for k, v in metrics.items()],
                          key=lambda x: (-x[1], -x[2]))[:15])
        fields[name], screens[name] = field, metrics
        result["fields"][name] = record
        print(name, sorted([(v["top_147"], k) for k, v in metrics.items()], reverse=True)[:10], flush=True)
    # Including the incumbent and core alternatives independent of screening
    # keeps their paired comparisons intact. All final outcomes have a new seed.
    finalists = {k for k in lineups if not k.startswith("original ")}
    finalists.update(f"original {i}" for i in (47, 71, 79, 123, 253, 328, 632, 633))
    for screen in screens.values():
        order = sorted(lineups, key=lambda k: (screen[k]["top_147"], screen[k]["top_15"]), reverse=True)
        finalists.update(order[:12])
    finalists = {n: ids for n, ids in lineups.items() if n in finalists}
    result["candidates"] = outcome_stats(pool, finalists)
    for label, sample in fields.items():
        print("Independent validation", label, len(finalists), flush=True)
        result["fields"][label]["results"] = tournament(pool, finalists, sample, final_draws, SEED + 67)
    result["stress_draws"] = 12000
    result["fields"]["millionaire"]["role_and_weather_stress"] = tournament(
        pool, finalists, fields["millionaire"], result["stress_draws"], SEED + 71, True)
    (ROOT / "results.json").write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
