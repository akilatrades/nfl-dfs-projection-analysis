import pandas as pd
import pytest

from src.projections import add_model_projections, validate_projection_inputs


def test_wr_projection_and_value() -> None:
    players = pd.DataFrame(
        [
            {
                "player": "Example WR",
                "position": "WR",
                "salary": 6000,
                "targets": 10,
                "catch_rate": 0.70,
                "yards_per_reception": 10,
                "rec_td": 0.50,
                "recent_dk_std": 5,
            }
        ]
    )

    result = add_model_projections(players)

    assert result.loc[0, "model_projection"] == pytest.approx(17.0)
    assert result.loc[0, "value_per_1000"] == pytest.approx(2.833333, rel=1e-5)


def test_qb_projection_arithmetic() -> None:
    players = pd.DataFrame(
        [
            {
                "player": "Example QB",
                "position": "QB",
                "salary": 6500,
                "pass_attempts": 35,
                "completion_rate": 0.65,
                "yards_per_completion": 11,
                "pass_td": 2.0,
                "interceptions": 0.8,
                "rush_attempts": 5,
                "yards_per_carry": 5,
                "rush_td": 0.20,
                "recent_dk_std": 6,
            }
        ]
    )

    result = add_model_projections(players)
    expected = 250.25 * 0.04 + 2.0 * 4 - 0.8 + 25 * 0.10 + 0.20 * 6

    assert result.loc[0, "model_projection"] == pytest.approx(expected)


def test_projection_input_validation_rejects_missing_salary() -> None:
    players = pd.DataFrame([{"player": "Example WR", "position": "WR"}])

    with pytest.raises(ValueError, match="Missing required columns"):
        validate_projection_inputs(players)
