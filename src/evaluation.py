"""Evaluation helpers for the NFL DFS projection-analysis project.

The functions in this file compare our pre-slate forecasts with actual results.
They are intentionally small so the calculations are easy to audit.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def add_projection_errors(
    players: pd.DataFrame,
    projection_col: str = "model_projection",
    actual_col: str = "actual_points",
) -> pd.DataFrame:
    """Add signed and absolute player projection errors.

    Signed error:
        actual points - projected points

    Positive signed error means the player scored above projection.
    Negative signed error means the player scored below projection.

    Absolute error ignores direction and measures only how far the forecast
    was from the actual result.
    """
    required = {projection_col, actual_col}
    missing = required.difference(players.columns)

    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    out = players.copy()

    out["projection_error"] = out[actual_col] - out[projection_col]
    out["absolute_projection_error"] = out["projection_error"].abs()

    return out


def projection_accuracy_summary(
    players: pd.DataFrame,
    projection_col: str = "model_projection",
    actual_col: str = "actual_points",
) -> pd.Series:
    """Calculate MAE, RMSE, and average signed error.

    MAE:
        Average absolute difference between projection and actual score.

    RMSE:
        Similar to MAE, but large misses receive more weight.

    Average signed error:
        Shows whether projections were too high or too low on average.
    """
    evaluated = add_projection_errors(
        players,
        projection_col=projection_col,
        actual_col=actual_col,
    )

    errors = evaluated["projection_error"].dropna()

    if errors.empty:
        raise ValueError("No complete projection/actual rows to evaluate.")

    mae = errors.abs().mean()
    rmse = np.sqrt(np.mean(errors**2))
    mean_error = errors.mean()

    return pd.Series(
        {
            "players_evaluated": len(errors),
            "mae": mae,
            "rmse": rmse,
            "mean_signed_error": mean_error,
        }
    )


def add_ownership_errors(
    players: pd.DataFrame,
    projected_col: str = "our_ownership_estimate",
    actual_col: str = "actual_ownership",
) -> pd.DataFrame:
    """Compare our ownership estimate with actual contest ownership.

    Ownership values should use the same scale in both columns.
    For example, use 18.5 for 18.5% in both columns.
    """
    required = {projected_col, actual_col}
    missing = required.difference(players.columns)

    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    out = players.copy()

    out["ownership_error"] = out[actual_col] - out[projected_col]
    out["absolute_ownership_error"] = out["ownership_error"].abs()

    return out


def ownership_accuracy_summary(
    players: pd.DataFrame,
    projected_col: str = "our_ownership_estimate",
    actual_col: str = "actual_ownership",
) -> pd.Series:
    """Return simple ownership forecast error statistics."""
    evaluated = add_ownership_errors(
        players,
        projected_col=projected_col,
        actual_col=actual_col,
    )

    errors = evaluated["ownership_error"].dropna()

    if errors.empty:
        raise ValueError("No complete projected/actual ownership rows to evaluate.")

    return pd.Series(
        {
            "players_evaluated": len(errors),
            "ownership_mae": errors.abs().mean(),
            "ownership_rmse": np.sqrt(np.mean(errors**2)),
            "mean_ownership_error": errors.mean(),
        }
    )
