import pandas as pd

from src.statistical_analysis import (
    add_position_percentiles,
    add_salary_hit_probabilities,
    add_tournament_leverage_index,
    projection_sensitivity,
    simulate_player_outcomes,
)


def _players() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "player": "WR A",
                "position": "WR",
                "salary": 6000,
                "model_projection": 18.0,
                "model_ceiling": 30.8,
                "value_per_1000": 3.0,
                "our_ownership_estimate": 20.0,
            },
            {
                "player": "WR B",
                "position": "WR",
                "salary": 6000,
                "model_projection": 16.0,
                "model_ceiling": 28.8,
                "value_per_1000": 2.67,
                "our_ownership_estimate": 5.0,
            },
        ]
    )


def test_percentiles_probabilities_and_leverage() -> None:
    ranked = add_position_percentiles(_players())

    assert ranked.loc[0, "projection_percentile"] == 100.0
    assert ranked.loc[1, "projection_percentile"] == 50.0

    with_probs = add_salary_hit_probabilities(ranked)
    assert with_probs["prob_3x"].between(0, 1).all()
    assert with_probs["prob_4x"].between(0, 1).all()

    leveraged = add_tournament_leverage_index(with_probs)
    assert (
        leveraged.loc[1, "tournament_leverage_index"]
        > leveraged.loc[0, "tournament_leverage_index"]
    )


def test_simulation_is_reproducible_with_fixed_seed() -> None:
    ranked = add_position_percentiles(_players())
    with_probs = add_salary_hit_probabilities(ranked)
    leveraged = add_tournament_leverage_index(with_probs)

    first = simulate_player_outcomes(leveraged, n_sims=10_000, seed=1)
    second = simulate_player_outcomes(leveraged, n_sims=10_000, seed=1)

    pd.testing.assert_frame_equal(first, second)
    assert (first["sim_p95"] >= first["sim_median"]).all()


def test_projection_sensitivity_orders_high_and_low_cases() -> None:
    row = pd.Series(
        {
            "player": "Example WR",
            "position": "WR",
            "salary": 6000,
            "targets": 8.0,
            "catch_rate": 0.65,
            "yards_per_reception": 12.0,
            "rec_td": 0.40,
        }
    )

    sensitivity = projection_sensitivity(
        row,
        inputs=["targets", "catch_rate", "yards_per_reception", "rec_td"],
    )

    assert not sensitivity.empty
    assert (sensitivity["high_projection"] >= sensitivity["low_projection"]).all()
