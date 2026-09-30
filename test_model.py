import pandas as pd

from src.projections import add_model_projections


# WR example:
# 10 targets * 70% = 7 receptions
# 7 receptions * 10 yards = 70 receiving yards
# 7 reception points + 7 yardage points + 3 expected TD points
# from 0.50 expected receiving TDs = 17 DK points.
wr = pd.DataFrame(
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

wr_result = add_model_projections(wr)

assert round(
    wr_result.loc[0, "model_projection"],
    2,
) == 17.00

assert round(
    wr_result.loc[0, "value_per_1000"],
    2,
) == 2.83


# QB example:
# 35 attempts * 65% completion * 11 yards/completion
# = 250.25 expected passing yards.
qb = pd.DataFrame(
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

qb_result = add_model_projections(qb)

expected_qb_points = (
    250.25 * 0.04
    + 2.0 * 4
    - 0.8
    + 25 * 0.10
    + 0.20 * 6
)

assert round(
    qb_result.loc[0, "model_projection"],
    2,
) == round(expected_qb_points, 2)

print("Projection model checks passed.")
