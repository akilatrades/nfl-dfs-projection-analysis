"""Week 5 Sunday: final conditional score model for two entered lineups.

Requires numpy, scipy and scikit-learn.
Run: python score_model.py
Model is illustrative, not calibrated to DFS payouts, ownership or opponents.
"""

import json, csv
from pathlib import Path
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import LeaveOneOut

OUT = Path(__file__).resolve().parent
N, SEED = 180000, 20261011
rng = np.random.default_rng(SEED)
# Elo histories transcribed from nflanalytic.com Week 3-4 pregame ratings
# Each tuple: away Elo, home Elo, actual home victory, week.
elo_games = [
    (1409, 1436, 1, 4),
    (1455, 1538, 0, 4),
    (1483, 1437, 0, 4),
    (1596, 1520, 0, 4),
    (1581, 1562, 0, 4),
    (1571, 1659, 0, 4),
    (1371, 1565, 1, 4),
    (1305, 1561, 1, 4),
    (1396, 1614, 1, 4),
    (1609, 1614, 1, 4),
    (1571, 1443, 0, 4),
    (1453, 1681, 1, 4),
    (1560, 1431, 1, 4),
    (1454, 1434, 0, 4),
    (1413, 1524, 0, 3),
    (1443, 1426, 1, 3),
    (1532, 1511, 1, 3),
    (1551, 1436, 1, 3),
    (1551, 1415, 0, 3),
    (1462, 1651, 1, 3),
    (1604, 1563, 1, 3),
    (1380, 1552, 1, 3),
    (1697, 1427, 1, 3),
    (1315, 1426, 1, 3),
    (1416, 1607, 1, 3),
    (1599, 1451, 0, 3),
    (1551, 1465, 0, 3),
    (1416, 1461, 0, 3),
    (1595, 1595, 1, 3),
]
X = np.array([[(h - a) / 100] for a, h, w, week in elo_games])
y = np.array([w for a, h, w, week in elo_games])
loocv = np.zeros(len(y))
for train, test in LeaveOneOut().split(X):
    reg = LogisticRegression(C=1.5, max_iter=400, solver="lbfgs").fit(
        X[train], y[train]
    )
    loocv[test] = reg.predict_proba(X[test])[:, 1]
brier = float(np.mean((loocv - y) ** 2))
base_brier = float(np.mean((float(y.mean()) - y) ** 2))
full = LogisticRegression(C=1.5, max_iter=400, solver="lbfgs").fit(X, y)
ELO = {
    "DET": 0.64,
    "CHI": 0.54,
    "CIN": 0.59,
    "MIN": 0.73,
    "NE": 0.76,
    "DEN": 0.63,
    "SEA": 0.64,
}
# Oct 8 public EPA/play: (offense EPA/play, defense EPA/play)
EPA = {
    "DET": (0.051, 0.047),
    "ARI": (-0.013, 0.027),
    "GB": (0.008, 0.031),
    "CHI": (0.053, -0.006),
    "CIN": (0.017, 0.029),
    "MIA": (-0.046, 0.051),
    "MIN": (-0.072, -0.090),
    "NO": (-0.038, 0.017),
    "LV": (-0.056, -0.024),
    "NE": (0.007, -0.031),
    "SF": (0.104, 0.016),
    "SEA": (0.014, -0.080),
    "DEN": (0.003, -0.027),
    "LAC": (-0.055, -0.029),
}
# Market totals/spreads from dated, mixed-source reports; DEN-LAC and SF-SEA
# spread/total use rounded scenario assumptions, not verified closing lines.
GAMES = {
    "CHI-GB": ("CHI", "GB", 45.5, 1.5),
    "CIN-MIA": ("CIN", "MIA", 44.5, 7.0),
    "MIN-NO": ("MIN", "NO", 42.5, 1.5),
    "LV-NE": ("NE", "LV", 44.8, 3.5),
    "DET-ARI": ("DET", "ARI", 54.5, 5.5),
    "SF-SEA": ("SF", "SEA", 46.5, 0.0),
    "DEN-LAC": ("DEN", "LAC", 42.0, 3.5),
}
# Previous Week 5 mean projections (public+analyst midpoint), not fitted data.
# Newer players use one public prior only (no fabricated second estimate).
# name -> (team,position,mean DK pts, conditional receiving TD share)
P = {
    "Jordan Love": ("GB", "QB", 18.047, 0),
    "Jared Goff": ("DET", "QB", 19.5245, 0),
    "Chase Brown": ("CIN", "RB", 16.7645, 0),
    "D'Andre Swift": ("CHI", "RB", 16.1915, 0),
    "Aaron Jones Sr.": ("MIN", "RB", 15.6, 0),
    "Michael Wilson": ("ARI", "WR", 15.694, 0.25),
    "Christian Watson": ("GB", "WR", 15.0425, 0.29),
    "Jameson Williams": ("DET", "WR", 12.135, 0.22),
    "Hunter Henry": ("NE", "TE", 8.755, 0.20),
    "Trey McBride": ("ARI", "TE", 16.146, 0.30),
    "Amon-Ra St. Brown": ("DET", "WR", 18.17, 0.32),
    "Luther Burden III": ("CHI", "WR", 14.7, 0.25),
    "Tre Tucker": ("LV", "WR", 11.1, 0.25),
    "Sam LaPorta": ("DET", "TE", 12.27, 0.20),
    "George Kittle": ("SF", "TE", 14.059, 0.28),
    "Chargers DST": ("LAC", "DST", 5.44, 0),
}
LINEUPS = {
    "5_dollar_23k": [
        "Jordan Love",
        "Chase Brown",
        "D'Andre Swift",
        "Michael Wilson",
        "Christian Watson",
        "Jameson Williams",
        "Hunter Henry",
        "Trey McBride",
        "Chargers DST",
    ],
    "3_dollar_7k": [
        "Jared Goff",
        "Chase Brown",
        "Aaron Jones Sr.",
        "Amon-Ra St. Brown",
        "Luther Burden III",
        "Tre Tucker",
        "Sam LaPorta",
        "George Kittle",
        "Chargers DST",
    ],
}
PASS_BASE = {
    "DET": 0.65,
    "ARI": 0.72,
    "GB": 0.68,
    "CHI": 0.50,
    "CIN": 0.61,
    "MIA": 0.59,
    "MIN": 0.50,
    "NO": 0.58,
    "NE": 0.63,
    "LV": 0.66,
    "SF": 0.62,
    "SEA": 0.60,
    "DEN": 0.59,
    "LAC": 0.59,
}
RB_RUSH = {"Chase Brown": 0.52, "D'Andre Swift": 0.67, "Aaron Jones Sr.": 0.48}
RB_CATCH = {"Chase Brown": 0.08, "D'Andre Swift": 0.06, "Aaron Jones Sr.": 0.07}
QB_RUSH = {"Jordan Love": 0.06, "Jared Goff": 0.025}
MARKET = {}
TEAM = {}
for game, (fav, dog, total, spread) in GAMES.items():
    MARKET[fav] = (total + spread) / 2
    MARKET[dog] = (total - spread) / 2
    shared_pace = rng.gamma(12, 1 / 12, size=N)
    for t, opp in ((fav, dog), (dog, fav)):
        individual_jitter = rng.lognormal(-0.5 * 0.13**2, 0.13, size=N)
        lam = max(0.1, (MARKET[t] - 4.5) / 6.95)
        td = rng.poisson(lam * shared_pace * individual_jitter)
        ppass = np.clip(PASS_BASE[t] + rng.normal(0, 0.09, N), 0.15, 0.90)
        pass_td = rng.binomial(td, ppass)
        TEAM[t] = {
            "td": td,
            "pass": pass_td,
            "rush": td - pass_td,
            "pace": shared_pace,
            "z": rng.standard_normal(N),
            "lambda_td": lam,
        }
TDS = {name: np.zeros(N, dtype=np.int16) for name in P}
QBRUSH = {name: np.zeros(N, dtype=np.int16) for name in QB_RUSH}
# Team passing/rushing TDs allocated without double counting a scored touchdown.
for t in TEAM:
    members = {
        name: sh
        for name, (team, pos, mean, sh) in P.items()
        if team == t and pos in ("WR", "TE")
    }
    members.update({name: sh for name, sh in RB_CATCH.items() if P[name][0] == t})
    rem = TEAM[t]["pass"].copy()
    used = 0.0
    for name, share in members.items():
        assert used + share <= 1.00001
        assigned = rng.binomial(rem, min(1.0, share / (1.0 - used)))
        TDS[name] += assigned
        rem -= assigned
        used += share
    rem = TEAM[t]["rush"].copy()
    for name, share in QB_RUSH.items():
        if P[name][0] == t:
            assigned = rng.binomial(rem, share)
            QBRUSH[name] += assigned
            rem -= assigned
    for name, share in RB_RUSH.items():
        if P[name][0] == t:
            role = rng.beta(share * 26, (1 - share) * 26, size=N)
            assigned = rng.binomial(rem, role)
            TDS[name] += assigned
            rem -= assigned
SCORES = {}
for name, (team, pos, mean, share) in P.items():
    if pos == "DST":
        jitter = rng.normal(0, 4.25, N)
        SCORES[name] = np.clip(
            mean + jitter - (TEAM["DEN"]["td"] - TEAM["DEN"]["lambda_td"]), -4, 28
        )
        continue
    lam = TEAM[team]["lambda_td"]
    pass_share = PASS_BASE[team]
    if pos == "QB":
        expected_td_credits = (
            4 * lam * pass_share + 6 * lam * (1 - pass_share) * QB_RUSH[name]
        )
    elif pos == "RB":
        expected_td_credits = (
            6 * lam * ((1 - pass_share) * RB_RUSH[name] + pass_share * RB_CATCH[name])
        )
    else:
        expected_td_credits = 6 * lam * pass_share * share
    base = max(1.5, mean - expected_td_credits)
    sig = {"QB": 0.31, "RB": 0.42, "WR": 0.52, "TE": 0.48}[pos]
    z = (
        0.27 * rng.standard_normal(N)
        + 0.27 * TEAM[team]["z"]
        + 0.28 * (TEAM[team]["pace"] - 1) * 3
        + 0.82 * rng.standard_normal(N)
    )
    non_td = base * np.exp(sig * z - 0.5 * sig**2)
    score = (
        non_td + 4 * TEAM[team]["pass"] + 6 * QBRUSH[name]
        if pos == "QB"
        else non_td + 6 * TDS[name]
    )
    SCORES[name] = np.maximum(0, score)
L = {k: sum(SCORES[n] for n in roster) for k, roster in LINEUPS.items()}
SCENARIOS = {
    "baseline": np.ones(N, dtype=bool),
    "det_pass_3plus": TEAM["DET"]["pass"] >= 3,
    "det_pass_0or1": TEAM["DET"]["pass"] <= 1,
    "ari_pass_3plus": TEAM["ARI"]["pass"] >= 3,
    "ari_pass_0or1": TEAM["ARI"]["pass"] <= 1,
    "gb_pass_3plus": TEAM["GB"]["pass"] >= 3,
    "gb_pass_0or1": TEAM["GB"]["pass"] <= 1,
    "det_and_ari_pass_3plus": (TEAM["DET"]["pass"] >= 3) & (TEAM["ARI"]["pass"] >= 3),
}


def metrics(v):
    return {
        "mean": round(float(np.mean(v)), 2),
        "p10": round(float(np.quantile(v, 0.1)), 2),
        "median": round(float(np.quantile(v, 0.5)), 2),
        "p90": round(float(np.quantile(v, 0.9)), 2),
        "p95": round(float(np.quantile(v, 0.95)), 2),
        "p99": round(float(np.quantile(v, 0.99)), 2),
        "p150": round(float(np.mean(v >= 150)), 4),
        "p170": round(float(np.mean(v >= 170)), 4),
        "p190": round(float(np.mean(v >= 190)), 4),
    }


results = {
    "seed": SEED,
    "simulations": N,
    "logistic_regression": {
        "sample_games": len(y),
        "weeks": [3, 4],
        "loo_brier": round(brier, 4),
        "constant_prior_brier": round(base_brier, 4),
        "intercept": round(float(full.intercept_[0]), 4),
        "elo_gap_coef_per_100pts": round(float(full.coef_[0, 0]), 4),
        "assessment": "Exploratory fit failed to outperform the baseline on LOO; not used in final choice.",
    },
    "markets": MARKET,
    "elo_published": ELO,
    "epa": EPA,
    "lineups": {k: metrics(v) for k, v in L.items()},
    "portfolio": {
        "correlation": round(float(np.corrcoef(*list(L.values()))[0, 1]), 4),
        "at_least_one_170": round(
            float(np.mean((L["5_dollar_23k"] >= 170) | (L["3_dollar_7k"] >= 170))), 4
        ),
        "both_170": round(
            float(np.mean((L["5_dollar_23k"] >= 170) & (L["3_dollar_7k"] >= 170))), 4
        ),
    },
    "scenarios": {
        k: {
            "fraction": round(float(np.mean(mask)), 4),
            "lineups": {nm: metrics(v[mask]) for nm, v in L.items()},
        }
        for k, mask in SCENARIOS.items()
    },
    "player_mean_diagnostic": {
        name: round(float(np.mean(v)), 2) for name, v in SCORES.items()
    },
    "caveat": "Uncalibrated event and role assumptions; no field/payout/ownership EV model.",
}
(OUT / "results.json").write_text(json.dumps(results, indent=2) + "\n")
with (OUT / "scenario_comparison.csv").open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "scenario",
            "scenario_fraction",
            "contest",
            "mean",
            "p90",
            "p95",
            "p170",
            "p190",
        ]
    )
    for scenario, result in results["scenarios"].items():
        for contest, stat in result["lineups"].items():
            w.writerow(
                [
                    scenario,
                    result["fraction"],
                    contest,
                    stat["mean"],
                    stat["p90"],
                    stat["p95"],
                    stat["p170"],
                    stat["p190"],
                ]
            )
print(
    json.dumps(
        {
            "lineups": results["lineups"],
            "portfolio": results["portfolio"],
            "logistic": results["logistic_regression"],
        },
        indent=2,
    )
)
