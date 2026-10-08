"""Statistical analysis helpers for the NFL DFS project.

These functions sit on top of the project's own player projections.

The first version focuses on four questions:

1. How strong is a player relative to others at the same position?
2. How often does the player's simulated outcome reach a useful salary-based tournament target?
3. How much upside are we getting relative to our ownership estimate?
4. Which projection inputs matter most when we change them slightly?

The simulation uses a truncated normal approximation built from the model
projection and the model ceiling/floor. It is intentionally transparent.
Later versions can replace this with a full football-stat simulation once the
project has enough historical data to estimate richer distributions.
"""

from __future__ import annotations

from math import erf, sqrt
from typing import Iterable

import numpy as np
import pandas as pd

from src.projections import project_offensive_player


def _normal_cdf(x: float) -> float:
    return 0.5 * (1.0 + erf(x / sqrt(2.0)))


def add_position_percentiles(players: pd.DataFrame) -> pd.DataFrame:
    """Rank projection, ceiling, and value within each position."""
    required = {
        "position",
        "model_projection",
        "model_ceiling",
        "value_per_1000",
    }
    missing = required.difference(players.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    out = players.copy()

    for source, target in [
        ("model_projection", "projection_percentile"),
        ("model_ceiling", "ceiling_percentile"),
        ("value_per_1000", "value_percentile"),
    ]:
        out[target] = (
            out.groupby("position")[source].rank(pct=True, method="average") * 100.0
        )

    return out


def add_candidate_ownership_estimate(
    players: pd.DataFrame,
    target_sums: dict[str, float] | None = None,
    temperature: float = 80.0,
) -> pd.DataFrame:
    """Create our first candidate-pool popularity estimate.

    This is NOT imported ownership data.

    The estimate is built only from this project's own:
        projection percentile
        value percentile
        ceiling percentile

    First, a popularity score is calculated:

        45% projection percentile
        35% value percentile
        20% ceiling percentile

    The score is then converted into a percentage within each position.

    target_sums controls how much total ownership is assigned to the research
    pool at each position. Because this project does not yet model every
    player on the slate, these percentages are best treated as a relative
    popularity estimate rather than a fully calibrated field forecast.
    """
    required = {
        "position",
        "projection_percentile",
        "value_percentile",
        "ceiling_percentile",
    }
    missing = required.difference(players.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    if temperature <= 0:
        raise ValueError("temperature must be positive.")

    if target_sums is None:
        target_sums = {
            "QB": 60.0,
            "RB": 100.0,
            "WR": 130.0,
            "TE": 45.0,
        }

    out = players.copy()

    out["popularity_score"] = (
        0.45 * out["projection_percentile"]
        + 0.35 * out["value_percentile"]
        + 0.20 * out["ceiling_percentile"]
    )

    out["our_ownership_estimate"] = np.nan

    for position, group in out.groupby("position"):
        target = target_sums.get(position)

        if target is None:
            continue

        centered = group["popularity_score"] - group["popularity_score"].mean()

        weights = np.exp(centered / temperature)
        ownership = weights / weights.sum() * target

        out.loc[
            group.index,
            "our_ownership_estimate",
        ] = ownership

    return out


def add_salary_hit_probabilities(
    players: pd.DataFrame,
    range_z: float = 1.28,
) -> pd.DataFrame:
    """Estimate probability of reaching 3x and 4x salary value.

    Example:
        $6,000 salary -> 4x target = 24 DK points.

    The model infers standard deviation from:
        model_ceiling = projection + range_z * standard deviation

    This is a first-version approximation, not a claim that fantasy outcomes
    are perfectly normal.
    """
    required = {
        "salary",
        "model_projection",
        "model_ceiling",
    }
    missing = required.difference(players.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    out = players.copy()

    salary = pd.to_numeric(out["salary"], errors="coerce")
    projection = pd.to_numeric(out["model_projection"], errors="coerce")
    ceiling = pd.to_numeric(out["model_ceiling"], errors="coerce")

    std = (ceiling - projection) / range_z
    std = std.where(std > 0)

    out["target_3x"] = 3.0 * salary / 1000.0
    out["target_4x"] = 4.0 * salary / 1000.0

    def hit_probability(mean: float, sigma: float, target: float) -> float:
        if pd.isna(mean) or pd.isna(sigma) or pd.isna(target):
            return np.nan
        if sigma <= 0:
            return float(mean >= target)
        z = (target - mean) / sigma
        return 1.0 - _normal_cdf(z)

    out["prob_3x"] = [
        hit_probability(m, s, t) for m, s, t in zip(projection, std, out["target_3x"])
    ]
    out["prob_4x"] = [
        hit_probability(m, s, t) for m, s, t in zip(projection, std, out["target_4x"])
    ]

    return out


def add_tournament_leverage_index(
    players: pd.DataFrame,
    ownership_floor_pct: float = 1.0,
) -> pd.DataFrame:
    """Compare 4x hit probability with our ownership estimate.

    tournament_leverage_index =
        4x hit probability / ownership estimate as a decimal

    Larger values mean more simulated upside relative to expected popularity.
    This is a project-specific research metric, not an industry standard.
    """
    required = {
        "prob_4x",
        "our_ownership_estimate",
    }
    missing = required.difference(players.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    out = players.copy()

    ownership_pct = pd.to_numeric(
        out["our_ownership_estimate"],
        errors="coerce",
    ).clip(lower=ownership_floor_pct)

    out["tournament_leverage_index"] = out["prob_4x"] / (ownership_pct / 100.0)

    return out


def simulate_player_outcomes(
    players: pd.DataFrame,
    n_sims: int = 50_000,
    seed: int = 42,
    range_z: float = 1.28,
) -> pd.DataFrame:
    """Simulate a simple fantasy-point distribution for every player."""
    if n_sims <= 0:
        raise ValueError("n_sims must be positive.")

    required = {
        "player",
        "model_projection",
        "model_ceiling",
    }
    missing = required.difference(players.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    rng = np.random.default_rng(seed)
    records = []

    for _, row in players.iterrows():
        mean = float(row["model_projection"])
        ceiling = float(row["model_ceiling"])
        std = max((ceiling - mean) / range_z, 0.01)

        sims = rng.normal(mean, std, size=n_sims)
        sims = np.clip(sims, 0.0, None)

        records.append(
            {
                "player": row["player"],
                "sim_mean": float(np.mean(sims)),
                "sim_median": float(np.median(sims)),
                "sim_p75": float(np.quantile(sims, 0.75)),
                "sim_p90": float(np.quantile(sims, 0.90)),
                "sim_p95": float(np.quantile(sims, 0.95)),
                "sim_p99": float(np.quantile(sims, 0.99)),
            }
        )

    return pd.DataFrame(records)


def projection_sensitivity(
    player_row: pd.Series,
    inputs: Iterable[str],
    change_pct: float = 0.10,
) -> pd.DataFrame:
    """Measure how much the projection changes when one input moves."""
    if change_pct <= 0:
        raise ValueError("change_pct must be positive.")

    base = project_offensive_player(player_row)["model_projection"]
    records = []

    for input_name in inputs:
        original = player_row.get(input_name, np.nan)
        if pd.isna(original):
            continue

        original = float(original)
        low_row = player_row.copy()
        high_row = player_row.copy()

        low_row[input_name] = original * (1.0 - change_pct)
        high_row[input_name] = original * (1.0 + change_pct)

        low_projection = project_offensive_player(low_row)["model_projection"]
        high_projection = project_offensive_player(high_row)["model_projection"]

        records.append(
            {
                "input": input_name,
                "base_value": original,
                "low_value": low_row[input_name],
                "high_value": high_row[input_name],
                "base_projection": base,
                "low_projection": low_projection,
                "high_projection": high_projection,
                "downside_change": low_projection - base,
                "upside_change": high_projection - base,
                "sensitivity_range": high_projection - low_projection,
            }
        )

    return (
        pd.DataFrame(records)
        .sort_values("sensitivity_range", ascending=False)
        .reset_index(drop=True)
    )
