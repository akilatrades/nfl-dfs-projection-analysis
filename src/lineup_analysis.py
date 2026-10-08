"""Lineup-level statistical analysis.

This file evaluates a completed DraftKings lineup using the project's own
player projections.

The first version assumes player outcomes are independent. That is a useful
baseline, but it understates the effect of real football correlation.

Later versions can replace this with a joint simulation built from historical
QB/WR, QB/TE, RB/DST, and bring-back relationships.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def lineup_summary(lineup: pd.DataFrame) -> pd.Series:
    """Calculate simple lineup-level totals."""
    required = {
        "salary",
        "model_projection",
        "model_ceiling",
        "our_ownership_estimate",
    }
    missing = required.difference(lineup.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    ownership = pd.to_numeric(
        lineup["our_ownership_estimate"],
        errors="coerce",
    )

    ownership_decimal = ownership.clip(lower=0.1) / 100.0

    geometric_mean_ownership = float(np.exp(np.mean(np.log(ownership_decimal))) * 100.0)

    return pd.Series(
        {
            "salary_used": float(lineup["salary"].sum()),
            "model_projection": float(lineup["model_projection"].sum()),
            "sum_model_ceiling": float(lineup["model_ceiling"].sum()),
            "sum_ownership_estimate": float(ownership.sum()),
            "geometric_mean_ownership_pct": geometric_mean_ownership,
        }
    )


def simulate_lineup_score(
    lineup: pd.DataFrame,
    n_sims: int = 100_000,
    seed: int = 42,
    range_z: float = 1.28,
) -> pd.Series:
    """Simulate the lineup's total DraftKings score.

    Each player is sampled from a normal distribution using:
        mean = model projection
        standard deviation inferred from model ceiling

    Player outcomes are independent in this baseline version.
    """
    if n_sims <= 0:
        raise ValueError("n_sims must be positive.")

    required = {"model_projection", "model_ceiling"}
    missing = required.difference(lineup.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    rng = np.random.default_rng(seed)
    total = np.zeros(n_sims)

    for _, row in lineup.iterrows():
        mean = float(row["model_projection"])
        ceiling = float(row["model_ceiling"])
        std = max((ceiling - mean) / range_z, 0.01)

        player_scores = rng.normal(mean, std, size=n_sims)
        player_scores = np.clip(player_scores, 0.0, None)

        total += player_scores

    return pd.Series(
        {
            "sim_mean": float(np.mean(total)),
            "sim_median": float(np.median(total)),
            "sim_p75": float(np.quantile(total, 0.75)),
            "sim_p90": float(np.quantile(total, 0.90)),
            "sim_p95": float(np.quantile(total, 0.95)),
            "sim_p99": float(np.quantile(total, 0.99)),
        }
    )
