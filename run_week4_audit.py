"""Reconcile saved Week 4 records without changing pre-slate assumptions."""

import json
from pathlib import Path

import pandas as pd

from src.evaluation import projection_accuracy_summary
from src.projections import add_model_projections


def main():
    root = Path(__file__).resolve().parent
    week = root / "weeks/2026_week_04"
    out = week / "audit_2026-10-08"
    out.mkdir(exist_ok=True)
    final = pd.read_csv(week / "final_lineup.csv")
    inputs = add_model_projections(pd.read_csv(week / "projection_inputs.csv"))
    pool = pd.read_csv(week / "player_pool.csv")
    sample = pd.read_csv(week / "forecast_error_sample_2026-10-04.csv")
    players = final[["player", "dk_points"]].drop_duplicates()
    if players.player.duplicated().any():
        raise ValueError("Conflicting actual scores across contests.")
    players = players.merge(inputs[["player", "model_projection"]].rename(columns={"model_projection": "recomputed_input_projection"}), how="left", on="player", validate="one_to_one")
    players = players.merge(pool[["player", "model_projection"]].rename(columns={"model_projection": "saved_pool_projection"}), how="left", on="player", validate="one_to_one")
    players = players.merge(sample[["player", "source_projection", "error_classification"]], how="left", on="player", validate="one_to_one")
    for col in ["recomputed_input_projection", "saved_pool_projection", "source_projection"]:
        players[col + "_error"] = players.dk_points - players[col]
    players.to_csv(out / "player_coverage.csv", index=False, float_format="%.4f")
    totals = final.groupby("contest").agg(salary_used=("salary", "sum"), dk_score=("dk_points", "sum"), roster_size=("player", "size"), unique_players=("player", "nunique"))
    recorded = pd.read_csv(week / "actual_results_2026-10-04.csv").set_index("contest")
    totals["score_difference_from_record"] = totals.dk_score - recorded.dk_score
    totals["salary_difference_from_record"] = totals.salary_used - recorded.salary_used
    if not (totals.roster_size.eq(9) & totals.unique_players.eq(9) & totals.salary_used.le(50000) & totals.score_difference_from_record.abs().lt(1e-6) & totals.salary_difference_from_record.eq(0)).all():
        raise ValueError("Saved contest records do not reconcile.")
    totals.to_csv(out / "contest_reconciliation.csv", float_format="%.2f")
    metrics = {"scope": "Selected five-player sample; mixed projection snapshots; not slate-wide validation", "all_sample": projection_accuracy_summary(sample, "source_projection", "actual_dk_points").to_dict(), "sample_without_chase": projection_accuracy_summary(sample[sample.player != "Ja'Marr Chase"], "source_projection", "actual_dk_points").to_dict()}
    stack = sample[sample.player.isin(["Joe Burrow", "Ja'Marr Chase", "Tee Higgins", "Parker Washington"])]
    e = stack.actual_dk_points - stack.source_projection
    metrics["stack"] = {"projection": float(stack.source_projection.sum()), "actual": float(stack.actual_dk_points.sum()), "net_error": float(e.sum()), "sum_absolute_error": float(e.abs().sum())}
    metrics["coverage"] = {"unique_entered_players": len(players), "with_input_projection": int(players.recomputed_input_projection.notna().sum()), "with_saved_pool_projection": int(players.saved_pool_projection.notna().sum()), "with_sample_projection": int(players.source_projection.notna().sum())}
    metrics["raw_minus_ownership_actual"] = float(totals.loc["$50 Single Entry", "dk_score"] - totals.loc["$27 Single Entry", "dk_score"])
    (out / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
