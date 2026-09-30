"""Generate this project's own weekly DraftKings projections.

Example:

    python run_projections.py weeks/2026_week_04/projection_inputs.csv

The script writes a player_pool.csv file in the same week folder.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from src.projections import (
    add_model_projections,
    validate_projection_inputs,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate our NFL DFS player projections."
    )
    parser.add_argument(
        "input_file",
        type=Path,
        help="CSV containing our expected-stat assumptions.",
    )
    args = parser.parse_args()

    inputs = pd.read_csv(args.input_file)
    validate_projection_inputs(inputs)

    projected = add_model_projections(inputs)

    output_columns = [
        "player",
        "position",
        "team",
        "opponent",
        "salary",
        "model_projection",
        "model_floor",
        "model_ceiling",
        "value_per_1000",
        "our_ownership_estimate",
        "team_total",
        "game_total",
        "role_note",
        "correlation_note",
        "leverage_note",
        "decision",
        "reason",
        "status_note",
    ]

    for column in output_columns:
        if column not in projected.columns:
            projected[column] = pd.NA

    output = projected[output_columns].copy()

    output_path = args.input_file.parent / "player_pool.csv"
    output.to_csv(output_path, index=False)

    print(f"Wrote: {output_path}")
    print()
    print(
        output[
            [
                "player",
                "position",
                "salary",
                "model_projection",
                "model_floor",
                "model_ceiling",
                "value_per_1000",
            ]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()
