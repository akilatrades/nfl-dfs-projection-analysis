"""Build projection_inputs.csv from a public-stat snapshot.

Example:

    python run_baseline_inputs.py \
        weeks/2026_week_04/public_stat_snapshot.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from src.input_model import build_projection_inputs


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Convert public Week-to-Date NFL stats into our projection inputs."
        )
    )
    parser.add_argument(
        "snapshot_file",
        type=Path,
        help="CSV containing the public-stat snapshot.",
    )
    args = parser.parse_args()

    snapshot = pd.read_csv(args.snapshot_file)
    projection_inputs = build_projection_inputs(snapshot)

    output_path = args.snapshot_file.parent / "projection_inputs.csv"

    projection_inputs.to_csv(
        output_path,
        index=False,
    )

    print(f"Wrote: {output_path}")
    print()
    print(
        projection_inputs[
            [
                "player",
                "position",
                "salary",
                "team_total",
                "game_total",
                "status_note",
            ]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()
