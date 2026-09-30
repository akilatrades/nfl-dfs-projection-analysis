"""Run the weekly statistical player analysis.

Example:

    python run_statistical_analysis.py weeks/2026_week_04/player_pool.csv

The script creates player_analysis.csv in the same week folder.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from src.statistical_analysis import (
    add_position_percentiles,
    add_salary_hit_probabilities,
    add_tournament_leverage_index,
    simulate_player_outcomes,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Add statistical tournament metrics to our DFS player pool."
    )
    parser.add_argument(
        "player_pool",
        type=Path,
        help="CSV produced by run_projections.py",
    )
    parser.add_argument(
        "--sims",
        type=int,
        default=50_000,
        help="Number of player simulations. Default: 50,000",
    )
    args = parser.parse_args()

    players = pd.read_csv(args.player_pool)

    analyzed = add_position_percentiles(players)
    analyzed = add_salary_hit_probabilities(analyzed)
    analyzed = add_tournament_leverage_index(analyzed)

    sim = simulate_player_outcomes(
        analyzed,
        n_sims=args.sims,
    )

    analyzed = analyzed.merge(
        sim,
        on="player",
        how="left",
    )

    output_path = args.player_pool.parent / "player_analysis.csv"

    analyzed.to_csv(
        output_path,
        index=False,
    )

    print(f"Wrote: {output_path}")
    print()
    print(
        analyzed[
            [
                "player",
                "position",
                "salary",
                "model_projection",
                "model_ceiling",
                "projection_percentile",
                "ceiling_percentile",
                "prob_3x",
                "prob_4x",
                "our_ownership_estimate",
                "tournament_leverage_index",
                "sim_p90",
                "sim_p95",
                "sim_p99",
            ]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()
