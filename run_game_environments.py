"""Score the Week 4 game environments.

Example:

    python run_game_environments.py \
        weeks/2026_week_04/game_environments.csv

The input file must contain the raw total, implied team totals, and absolute
spread. The script recalculates the score and rank.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from src.game_environment import score_game_environments


def main() -> None:
    parser = argparse.ArgumentParser(description="Rank DFS game environments.")
    parser.add_argument(
        "game_file",
        type=Path,
        help="CSV containing Week game-market inputs.",
    )
    args = parser.parse_args()

    games = pd.read_csv(args.game_file)

    # Drop previously calculated columns so the result is reproducible.
    games = games.drop(
        columns=[
            "rank",
            "environment_score",
            "higher_team_total",
        ],
        errors="ignore",
    )

    scored = score_game_environments(games)
    scored.to_csv(args.game_file, index=False)

    print(
        scored[
            [
                "rank",
                "game",
                "game_total",
                "higher_team_total",
                "spread_abs",
                "environment_score",
            ]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()
