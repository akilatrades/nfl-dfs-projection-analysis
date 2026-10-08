"""Convert public Week-to-Date football stats into projection inputs.

This file creates the starting assumptions used by our fantasy model.

The problem:
Three NFL games are a very small sample. If we simply copy a player's first
three games into Week 4, one hot or cold stretch can dominate the projection.

The solution used in this first version is shrinkage.

Shrinkage blends the player's 2026 rate with a simple position baseline:

    adjusted rate =
        (games * player rate + prior games * position baseline)
        / (games + prior games)

We use different amounts of shrinkage for different types of statistics:

- Volume gets 2 prior games because carries, targets, and attempts stabilize
  faster than scoring.
- Efficiency gets 4 prior games because catch rate and yards per touch are
  noisier.
- Touchdowns get 8 prior games because touchdowns are especially volatile.

This is a transparent first version, not a claim that these prior weights are
perfect. They can be tested and improved after more weeks are collected.
"""

from __future__ import annotations

from math import erfc, sqrt

import numpy as np
import pandas as pd


POSITION_PRIORS = {
    "QB": {
        "pass_attempts": 32.0,
        "rush_attempts": 4.0,
        "completion_rate": 0.65,
        "yards_per_completion": 11.5,
        "yards_per_carry": 4.5,
        "pass_td_per_game": 1.50,
        "rush_td_per_game": 0.15,
        "interceptions_per_game": 0.65,
        "recent_dk_std": 6.5,
    },
    "RB": {
        "rush_attempts": 14.0,
        "targets": 4.0,
        "yards_per_carry": 4.2,
        "catch_rate": 0.75,
        "yards_per_reception": 8.0,
        "rush_td_per_game": 0.45,
        "rec_td_per_game": 0.10,
        "recent_dk_std": 7.5,
    },
    "WR": {
        "targets": 7.0,
        "catch_rate": 0.65,
        "yards_per_reception": 12.0,
        "rec_td_per_game": 0.35,
        "recent_dk_std": 8.0,
    },
    "TE": {
        "targets": 5.5,
        "catch_rate": 0.72,
        "yards_per_reception": 10.0,
        "rec_td_per_game": 0.30,
        "recent_dk_std": 6.5,
    },
}


def shrink_rate(
    player_rate: float,
    prior_rate: float,
    games: float,
    prior_games: float,
) -> float:
    """Blend a small player sample with a position baseline."""
    return (games * player_rate + prior_games * prior_rate) / (games + prior_games)


def _tail_probability(
    threshold: float,
    mean: float,
    std: float,
) -> float:
    """Normal-approximation probability of finishing above a threshold."""
    if std <= 0:
        return float(mean >= threshold)

    z = (threshold - mean) / std
    return 0.5 * erfc(z / sqrt(2.0))


def _safe_rate(
    numerator: float,
    denominator: float,
    fallback: float,
) -> float:
    if denominator <= 0:
        return fallback
    return numerator / denominator


def build_projection_inputs(snapshot: pd.DataFrame) -> pd.DataFrame:
    """Create Week projection assumptions from a public-stat snapshot."""
    required = {
        "player",
        "position",
        "team",
        "opponent",
        "salary",
        "games",
        "team_total",
        "game_total",
    }
    missing = required.difference(snapshot.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    output = []

    for _, row in snapshot.iterrows():
        position = str(row["position"]).upper()
        prior = POSITION_PRIORS[position]
        games = float(row["games"])

        # Team implied points are used only to scale touchdown expectation.
        # The adjustment is capped so one betting line cannot overwhelm the
        # rest of the model.
        td_environment = np.clip(
            float(row["team_total"]) / 22.5,
            0.75,
            1.25,
        )

        result = {
            "player": row["player"],
            "position": position,
            "team": row["team"],
            "opponent": row["opponent"],
            "salary": float(row["salary"]),
            "pass_attempts": 0.0,
            "completion_rate": 0.0,
            "yards_per_completion": 0.0,
            "pass_td": 0.0,
            "interceptions": 0.0,
            "rush_attempts": 0.0,
            "yards_per_carry": 0.0,
            "rush_td": 0.0,
            "targets": 0.0,
            "catch_rate": 0.0,
            "yards_per_reception": 0.0,
            "rec_td": 0.0,
            "fumbles_lost": 0.04,
            "expected_two_point_conversions": 0.0,
            "prob_300_pass": 0.0,
            "prob_100_rush": 0.0,
            "prob_100_rec": 0.0,
            "recent_dk_std": prior["recent_dk_std"],
            "team_total": float(row["team_total"]),
            "game_total": float(row["game_total"]),
            "our_ownership_estimate": np.nan,
            "role_note": ("Week 1-3 public usage blended with position baselines"),
            "correlation_note": "",
            "leverage_note": "",
            "decision": "research",
            "reason": "",
            "status_note": row.get("status_note", "active"),
        }

        if position == "QB":
            pass_attempts = float(row.get("pass_attempts_raw", 0.0))
            completions = float(row.get("completions_raw", 0.0))
            pass_yards = float(row.get("pass_yards_raw", 0.0))
            pass_td = float(row.get("pass_td_raw", 0.0))
            interceptions = float(row.get("interceptions_raw", 0.0))
            rush_attempts = float(row.get("rush_attempts_raw", 0.0))
            rush_yards = float(row.get("rush_yards_raw", 0.0))
            rush_td = float(row.get("rush_td_raw", 0.0))

            raw_completion_rate = _safe_rate(
                completions,
                pass_attempts,
                prior["completion_rate"],
            )
            raw_yards_per_completion = _safe_rate(
                pass_yards,
                completions,
                prior["yards_per_completion"],
            )
            raw_rush_ypc = _safe_rate(
                rush_yards,
                rush_attempts,
                prior["yards_per_carry"],
            )

            result["pass_attempts"] = shrink_rate(
                pass_attempts / games,
                prior["pass_attempts"],
                games,
                2.0,
            )
            result["completion_rate"] = shrink_rate(
                raw_completion_rate,
                prior["completion_rate"],
                games,
                4.0,
            )
            result["yards_per_completion"] = shrink_rate(
                raw_yards_per_completion,
                prior["yards_per_completion"],
                games,
                4.0,
            )
            result["pass_td"] = (
                shrink_rate(
                    pass_td / games,
                    prior["pass_td_per_game"],
                    games,
                    8.0,
                )
                * td_environment
            )
            result["interceptions"] = shrink_rate(
                interceptions / games,
                prior["interceptions_per_game"],
                games,
                6.0,
            )
            result["rush_attempts"] = shrink_rate(
                rush_attempts / games,
                prior["rush_attempts"],
                games,
                2.0,
            )
            result["yards_per_carry"] = shrink_rate(
                raw_rush_ypc,
                prior["yards_per_carry"],
                games,
                4.0,
            )
            result["rush_td"] = (
                shrink_rate(
                    rush_td / games,
                    prior["rush_td_per_game"],
                    games,
                    8.0,
                )
                * td_environment
            )

            expected_pass_yards = (
                result["pass_attempts"]
                * result["completion_rate"]
                * result["yards_per_completion"]
            )
            expected_rush_yards = result["rush_attempts"] * result["yards_per_carry"]

            result["prob_300_pass"] = _tail_probability(
                300.0,
                expected_pass_yards,
                55.0,
            )
            result["prob_100_rush"] = _tail_probability(
                100.0,
                expected_rush_yards,
                35.0,
            )

        elif position == "RB":
            rush_attempts = float(row.get("rush_attempts_raw", 0.0))
            rush_yards = float(row.get("rush_yards_raw", 0.0))
            rush_td = float(row.get("rush_td_raw", 0.0))
            targets = float(row.get("targets_raw", 0.0))
            receptions = float(row.get("receptions_raw", 0.0))
            rec_yards = float(row.get("rec_yards_raw", 0.0))
            rec_td = float(row.get("rec_td_raw", 0.0))

            result["rush_attempts"] = shrink_rate(
                rush_attempts / games,
                prior["rush_attempts"],
                games,
                2.0,
            )
            result["yards_per_carry"] = shrink_rate(
                _safe_rate(
                    rush_yards,
                    rush_attempts,
                    prior["yards_per_carry"],
                ),
                prior["yards_per_carry"],
                games,
                4.0,
            )
            result["rush_td"] = (
                shrink_rate(
                    rush_td / games,
                    prior["rush_td_per_game"],
                    games,
                    8.0,
                )
                * td_environment
            )
            result["targets"] = shrink_rate(
                targets / games,
                prior["targets"],
                games,
                2.0,
            )
            result["catch_rate"] = shrink_rate(
                _safe_rate(
                    receptions,
                    targets,
                    prior["catch_rate"],
                ),
                prior["catch_rate"],
                games,
                4.0,
            )
            result["yards_per_reception"] = shrink_rate(
                _safe_rate(
                    rec_yards,
                    receptions,
                    prior["yards_per_reception"],
                ),
                prior["yards_per_reception"],
                games,
                4.0,
            )
            result["rec_td"] = (
                shrink_rate(
                    rec_td / games,
                    prior["rec_td_per_game"],
                    games,
                    8.0,
                )
                * td_environment
            )

            expected_rush_yards = result["rush_attempts"] * result["yards_per_carry"]
            expected_rec_yards = (
                result["targets"] * result["catch_rate"] * result["yards_per_reception"]
            )

            result["prob_100_rush"] = _tail_probability(
                100.0,
                expected_rush_yards,
                35.0,
            )
            result["prob_100_rec"] = _tail_probability(
                100.0,
                expected_rec_yards,
                30.0,
            )

        else:
            targets = float(row.get("targets_raw", 0.0))
            receptions = float(row.get("receptions_raw", 0.0))
            rec_yards = float(row.get("rec_yards_raw", 0.0))
            rec_td = float(row.get("rec_td_raw", 0.0))

            result["targets"] = shrink_rate(
                targets / games,
                prior["targets"],
                games,
                2.0,
            )
            result["catch_rate"] = shrink_rate(
                _safe_rate(
                    receptions,
                    targets,
                    prior["catch_rate"],
                ),
                prior["catch_rate"],
                games,
                4.0,
            )
            result["yards_per_reception"] = shrink_rate(
                _safe_rate(
                    rec_yards,
                    receptions,
                    prior["yards_per_reception"],
                ),
                prior["yards_per_reception"],
                games,
                4.0,
            )
            result["rec_td"] = (
                shrink_rate(
                    rec_td / games,
                    prior["rec_td_per_game"],
                    games,
                    8.0,
                )
                * td_environment
            )

            expected_rec_yards = (
                result["targets"] * result["catch_rate"] * result["yards_per_reception"]
            )

            rec_std = 30.0 if position == "TE" else 35.0
            result["prob_100_rec"] = _tail_probability(
                100.0,
                expected_rec_yards,
                rec_std,
            )

        output.append(result)

    return pd.DataFrame(output)
