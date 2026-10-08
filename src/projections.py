"""Transparent DraftKings NFL projection model.

The project builds fantasy projections from football assumptions rather than
starting with a fantasy-point projection from another source.

For offensive players, the model converts expected passing, rushing, and
receiving statistics into DraftKings points.

For DST, the model converts expected defensive events into DraftKings points.

The scoring constants follow the standard DraftKings NFL scoring structure
used by this project. Bonus probabilities are entered separately because a
300-yard or 100-yard bonus is not guaranteed simply because a mean projection
is near the threshold.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

PASS_YARD_POINT = 0.04
PASS_TD_POINT = 4.0
INTERCEPTION_POINT = -1.0

RUSH_YARD_POINT = 0.10
RUSH_TD_POINT = 6.0

RECEPTION_POINT = 1.0
RECEIVING_YARD_POINT = 0.10
RECEIVING_TD_POINT = 6.0

FUMBLE_LOST_POINT = -1.0
TWO_POINT_CONVERSION_POINT = 2.0
YARDAGE_BONUS_POINT = 3.0

DST_SACK_POINT = 1.0
DST_INTERCEPTION_POINT = 2.0
DST_FUMBLE_RECOVERY_POINT = 2.0
DST_TD_POINT = 6.0
DST_SAFETY_POINT = 2.0
DST_BLOCK_POINT = 2.0


def _number(row: pd.Series, name: str, default: float = 0.0) -> float:
    """Read a numeric input safely.

    Blank cells are treated as the supplied default. This lets one shared
    input file work for QB, RB, WR, TE, and DST rows even though different
    positions use different columns.
    """
    value = row.get(name, default)

    if pd.isna(value) or value == "":
        return float(default)

    return float(value)


def project_offensive_player(row: pd.Series) -> dict[str, float]:
    """Project one QB/RB/WR/TE from expected football statistics.

    The projection is an expected-value calculation.

    Example:
        8 targets * 0.65 catch rate = 5.2 expected receptions

    Fractional touchdowns are allowed because they represent an expectation
    before the game, not a literal game result.
    """
    pass_attempts = _number(row, "pass_attempts")
    completion_rate = _number(row, "completion_rate")
    yards_per_completion = _number(row, "yards_per_completion")
    pass_td = _number(row, "pass_td")
    interceptions = _number(row, "interceptions")

    rush_attempts = _number(row, "rush_attempts")
    yards_per_carry = _number(row, "yards_per_carry")
    rush_td = _number(row, "rush_td")

    targets = _number(row, "targets")
    catch_rate = _number(row, "catch_rate")
    yards_per_reception = _number(row, "yards_per_reception")
    rec_td = _number(row, "rec_td")

    fumbles_lost = _number(row, "fumbles_lost")
    expected_two_point_conversions = _number(
        row,
        "expected_two_point_conversions",
    )

    prob_300_pass = _number(row, "prob_300_pass")
    prob_100_rush = _number(row, "prob_100_rush")
    prob_100_rec = _number(row, "prob_100_rec")

    pass_yards = pass_attempts * completion_rate * yards_per_completion

    rush_yards = rush_attempts * yards_per_carry

    receptions = targets * catch_rate

    rec_yards = receptions * yards_per_reception

    points = (
        pass_yards * PASS_YARD_POINT
        + pass_td * PASS_TD_POINT
        + interceptions * INTERCEPTION_POINT
        + rush_yards * RUSH_YARD_POINT
        + rush_td * RUSH_TD_POINT
        + receptions * RECEPTION_POINT
        + rec_yards * RECEIVING_YARD_POINT
        + rec_td * RECEIVING_TD_POINT
        + fumbles_lost * FUMBLE_LOST_POINT
        + expected_two_point_conversions * TWO_POINT_CONVERSION_POINT
        + prob_300_pass * YARDAGE_BONUS_POINT
        + prob_100_rush * YARDAGE_BONUS_POINT
        + prob_100_rec * YARDAGE_BONUS_POINT
    )

    return {
        "expected_pass_yards": pass_yards,
        "expected_rush_yards": rush_yards,
        "expected_receptions": receptions,
        "expected_rec_yards": rec_yards,
        "model_projection": points,
    }


def project_dst(row: pd.Series) -> dict[str, float]:
    """Project one defense/special-teams unit.

    The points-allowed component is entered as
    expected_points_allowed_score.

    That value can be fractional because it represents the average scoring
    expectation across possible points-allowed outcomes.
    """
    expected_sacks = _number(row, "expected_sacks")
    expected_dst_interceptions = _number(
        row,
        "expected_dst_interceptions",
    )
    expected_fumble_recoveries = _number(
        row,
        "expected_fumble_recoveries",
    )
    expected_dst_tds = _number(row, "expected_dst_tds")
    expected_safeties = _number(row, "expected_safeties")
    expected_blocks = _number(row, "expected_blocks")
    expected_points_allowed_score = _number(
        row,
        "expected_points_allowed_score",
    )

    points = (
        expected_sacks * DST_SACK_POINT
        + expected_dst_interceptions * DST_INTERCEPTION_POINT
        + expected_fumble_recoveries * DST_FUMBLE_RECOVERY_POINT
        + expected_dst_tds * DST_TD_POINT
        + expected_safeties * DST_SAFETY_POINT
        + expected_blocks * DST_BLOCK_POINT
        + expected_points_allowed_score
    )

    return {
        "expected_pass_yards": np.nan,
        "expected_rush_yards": np.nan,
        "expected_receptions": np.nan,
        "expected_rec_yards": np.nan,
        "model_projection": points,
    }


def add_model_projections(
    players: pd.DataFrame,
    range_z: float = 1.28,
) -> pd.DataFrame:
    """Add our projection, floor, ceiling, and value to a player table.

    Floor and ceiling use:

        projection +/- range_z * recent_dk_std

    With the default range_z=1.28, the range is approximately the 10th to
    90th percentile if fantasy outcomes were normally distributed.

    That normal-distribution assumption is only a first version. The project
    can replace it with simulation after enough historical data is collected.
    """
    out = players.copy()

    results = []

    for _, row in out.iterrows():
        position = str(row.get("position", "")).upper()

        if position == "DST":
            result = project_dst(row)
        else:
            result = project_offensive_player(row)

        results.append(result)

    result_frame = pd.DataFrame(
        results,
        index=out.index,
    )

    for column in result_frame.columns:
        out[column] = result_frame[column]

    std = pd.to_numeric(
        out.get(
            "recent_dk_std",
            pd.Series(np.nan, index=out.index),
        ),
        errors="coerce",
    )

    out["model_floor"] = (out["model_projection"] - range_z * std).clip(lower=0)

    out["model_ceiling"] = out["model_projection"] + range_z * std

    salary = pd.to_numeric(
        out.get(
            "salary",
            pd.Series(np.nan, index=out.index),
        ),
        errors="coerce",
    )

    out["value_per_1000"] = np.where(
        salary > 0,
        out["model_projection"] / (salary / 1000.0),
        np.nan,
    )

    return out


def validate_projection_inputs(players: pd.DataFrame) -> None:
    """Run a few basic checks before generating projections."""
    required = {
        "player",
        "position",
        "salary",
    }

    missing = required.difference(players.columns)

    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    if players["player"].isna().any():
        raise ValueError("Every row needs a player name.")

    salary = pd.to_numeric(
        players["salary"],
        errors="coerce",
    )

    if salary.isna().any():
        raise ValueError("Every row needs a numeric salary.")

    if (salary < 0).any():
        raise ValueError("Salary cannot be negative.")
