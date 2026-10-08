"""Game-environment scoring for the NFL DFS project.

The purpose is to rank games before choosing individual players.

The score uses three simple public-market inputs:

- 50% game total
- 25% higher implied team total
- 25% closeness of the spread

Each input is converted to a 0-100 scale within the slate before the weights
are applied.

A higher score means the game has a stronger combination of expected scoring
and competitiveness according to this project-specific model.

This is not an industry-standard metric and it is not a prediction that the
game will actually score the most points.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def _minmax(series: pd.Series) -> pd.Series:
    """Convert a numeric series to a 0-100 scale."""
    values = pd.to_numeric(series, errors="coerce")
    lo = values.min()
    hi = values.max()

    if pd.isna(lo) or pd.isna(hi):
        return pd.Series(np.nan, index=series.index)

    if hi == lo:
        return pd.Series(50.0, index=series.index)

    return (values - lo) / (hi - lo) * 100.0


def score_game_environments(games: pd.DataFrame) -> pd.DataFrame:
    """Add the project's game-environment score and rank."""
    required = {
        "game",
        "team_a",
        "team_b",
        "game_total",
        "team_a_total",
        "team_b_total",
        "spread_abs",
    }
    missing = required.difference(games.columns)

    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    out = games.copy()

    out["higher_team_total"] = out[["team_a_total", "team_b_total"]].max(axis=1)

    total_score = _minmax(out["game_total"])
    team_score = _minmax(out["higher_team_total"])

    # Smaller spread = more competitive game.
    spread_score = 100.0 - _minmax(out["spread_abs"])

    out["environment_score"] = (
        0.50 * total_score + 0.25 * team_score + 0.25 * spread_score
    )

    out["rank"] = (
        out["environment_score"].rank(method="min", ascending=False).astype(int)
    )

    return out.sort_values(
        ["rank", "game_total"],
        ascending=[True, False],
    )
