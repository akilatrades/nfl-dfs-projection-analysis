"""Exact salary-constrained research search, not a contest win-probability model."""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.optimize import Bounds, LinearConstraint, milp


def optimize_lineup(
    pool: pd.DataFrame,
    objective_columns: list[str],
    *,
    quarterback: str | None = None,
    bring_back: bool = False,
    min_stack: int = 1,
    exclude: tuple[str, ...] = (),
    locks: tuple[str, ...] = (),
    salary_cap: int = 50_000,
    max_tight_ends: int = 2,
) -> pd.DataFrame:
    """Maximize the minimum total across supplied projection scenarios.

    One scenario maximizes its mean; multiple scenarios implement a maximin
    stress screen. Neither objective estimates tournament EV or a percentile.
    Strategy constraints: QB with WR/TE, no offense against own DST, at most
    four from a team and one speculative-role player. Bring-back is optional.
    max_tight_ends=1 separately tests constructions without a tight-end FLEX.
    """
    required = {
        "player",
        "position",
        "team",
        "opponent",
        "salary",
        "role_risk",
        *objective_columns,
    }
    if not objective_columns or not required.issubset(pool.columns):
        raise ValueError("Missing optimizer inputs or objective columns.")
    if pool.player.isna().any() or pool.player.duplicated().any():
        raise ValueError(
            "Player names must be present and unique in this research pool."
        )
    if pool[["team", "opponent"]].isna().any().any():
        raise ValueError("Every player needs a team and opponent.")
    if not pool.position.isin(["QB", "RB", "WR", "TE", "DST"]).all():
        raise ValueError("Unsupported position.")
    nums = pool[["salary", "role_risk", *objective_columns]].to_numpy(dtype=float)
    if not np.isfinite(nums).all() or (pool.salary <= 0).any():
        raise ValueError("Numeric inputs must be finite and salaries positive.")
    if not pool.role_risk.isin([0, 1]).all():
        raise ValueError("role_risk must be 0 or 1.")
    if not isinstance(min_stack, int) or min_stack < 0 or salary_cap <= 0:
        raise ValueError("Invalid stack minimum or salary cap.")
    if max_tight_ends not in (1, 2):
        raise ValueError("max_tight_ends must be 1 or 2.")
    if set(exclude) - set(pool.player):
        raise ValueError("Unknown excluded player.")
    if set(locks) - set(pool.player) or set(locks) & set(exclude):
        raise ValueError("Unknown or excluded locked player.")
    p = pool.loc[~pool.player.isin(exclude)].reset_index(drop=True)
    if (
        quarterback is not None
        and not ((p.player == quarterback) & (p.position == "QB")).any()
    ):
        raise ValueError("Requested quarterback is not available.")
    n = len(p)
    rows, lower, upper = [], [], []

    def constraint(v, lo=-np.inf, hi=np.inf, z=0):
        rows.append(np.r_[np.asarray(v, dtype=float), z])
        lower.append(lo)
        upper.append(hi)

    constraint(np.ones(n), 9, 9)
    constraint(p.salary, hi=salary_cap)
    for pos, lo, hi in [
        ("QB", 1, 1),
        ("RB", 2, 3),
        ("WR", 3, 4),
        ("TE", 1, max_tight_ends),
        ("DST", 1, 1),
    ]:
        constraint(p.position == pos, lo, hi)
    constraint(p.role_risk, hi=1)
    for team in sorted(p.team.unique()):
        constraint(p.team == team, hi=4)
    games = p.apply(lambda r: "-".join(sorted([r.team, r.opponent])), axis=1)
    for game in games.unique():
        constraint(games == game, hi=8)  # At least two games.
    for i, q in p[p.position == "QB"].iterrows():
        v = ((p.team == q.team) & p.position.isin(["WR", "TE"])).astype(float)
        v[i] = -min_stack
        constraint(v, lo=0)
        if bring_back:
            v = ((p.team == q.opponent) & p.position.isin(["RB", "WR", "TE"])).astype(
                float
            )
            v[i] = -1
            constraint(v, lo=0)
    for i, d in p[p.position == "DST"].iterrows():
        for j in p.index[(p.team == d.opponent) & (p.position != "DST")]:
            v = np.zeros(n)
            v[i] = v[j] = 1
            constraint(v, hi=1)
    if quarterback is not None:
        constraint(p.player == quarterback, 1, 1)
    for name in locks:
        constraint(p.player == name, 1, 1)
    for col in objective_columns:
        constraint(-p[col], hi=0, z=1)
    result = milp(
        c=np.r_[np.zeros(n), -1.0],
        integrality=np.r_[np.ones(n), 0],
        bounds=Bounds(np.r_[np.zeros(n), -np.inf], np.r_[np.ones(n), np.inf]),
        constraints=LinearConstraint(np.array(rows), lower, upper),
        options={"mip_rel_gap": 0.0, "time_limit": 30},
    )
    if result.status != 0:
        raise ValueError(f"No certified optimum: {result.message}")
    out = p.loc[result.x[:n] > 0.5].copy()
    out.attrs["objective"] = float(-result.fun)
    return out


def assign_slots(lineup: pd.DataFrame) -> pd.DataFrame:
    """Assign legal slots, putting the latest eligible starter into FLEX."""
    out = lineup.copy()
    out["slot"] = out.position
    eligible = []
    for pos, count in [("RB", 2), ("WR", 3), ("TE", 1)]:
        group = out[out.position == pos]
        if len(group) > count:
            eligible.extend(group.index)
    if not eligible:
        raise ValueError("Lineup has no valid FLEX player.")
    latest = out.loc[eligible].sort_values(["kickoff_utc", "player"]).index[-1]
    out.loc[latest, "slot"] = "FLEX"
    order = {"QB": 0, "RB": 1, "WR": 2, "TE": 3, "FLEX": 4, "DST": 5}
    return (
        out.assign(_order=out.slot.map(order))
        .sort_values(["_order", "player"])
        .drop(columns="_order")
    )
