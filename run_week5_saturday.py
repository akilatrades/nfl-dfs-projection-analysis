"""Week 5 Saturday scenario refresh; manual assumptions, not calibrated forecasts.

Run from repository root:
    python run_week5_saturday.py

Saves fresh artifacts without modifying October 9 assumptions/results.
"""

import hashlib
import json
from pathlib import Path

import pandas as pd

from src.optimizer import assign_slots, optimize_lineup
from src.projections import add_model_projections

ROOT = Path(__file__).resolve().parent
OLD = ROOT / "weeks/2026_week_05/single_entry_2026-10-09/projection_inputs.csv"
OUT = ROOT / "weeks/2026_week_05/saturday_2026-10-10"
HELD = (
    "Mitch Tinsley",
    "Dohnte Meyers",
    "Stefon Diggs",
    "Jaylen Warren",
    "Braelon Allen",
)


# Analyst scenarios, not empirical role forecasts. Main-slate salary
# references are published articles, not a verified DraftKings salary CSV.
def refresh(df):
    df = df.copy()
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    wilson = df.player.eq("Michael Wilson")
    mcbride = df.player.eq("Trey McBride")
    df.loc[wilson, "targets"] += 0.50
    df.loc[wilson, "rec_td"] += 0.05
    df.loc[mcbride, "targets"] += 0.75
    df.loc[mcbride, "rec_td"] += 0.05

    swift = df.loc[df.player.eq("Chase Brown")].iloc[0].copy()
    swift.update(
        {
            "player": "D'Andre Swift",
            "position": "RB",
            "team": "CHI",
            "opponent": "GB",
            "salary": 6200,
            "salary_source": "ST_OCT7_EARLY",
            "as_of": "2026-10-10",
            "salary_verification": "published_article_not_contest_export",
            "kickoff_utc": "2026-10-11T17:00:00Z",
            "role_risk": 0,
            "recent_dk_std": 8,
            "rush_attempts": 18.5,
            "yards_per_carry": 4.4,
            "rush_td": 0.55,
            "targets": 4.5,
            "catch_rate": 0.72,
            "yards_per_reception": 6.8,
            "rec_td": 0.12,
            "prob_100_rush": 0.22,
            "prob_100_rec": 0.02,
            "condition": "Monangai OUT; Swift full practice Friday; projected workload uncalibrated",
            "input_type": "analyst_assumption_not_fitted_forecast",
        }
    )
    df = pd.concat([df, swift.to_frame().T], ignore_index=True)
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="raise")
    df.loc[df.player.eq("Emanuel Wilson"), "condition"] = (
        "Charbonnet OUT, Holani questionable, Mixon added; verify committee at lock"
    )
    df.loc[df.player.eq("Michael Wilson"), "condition"] = (
        "Harrison Jr out; +0.5 targets and +0.05 rec TD scenario"
    )
    df.loc[df.player.eq("Trey McBride"), "condition"] = (
        "Harrison Jr out; +0.75 targets and +0.05 rec TD scenario"
    )
    return df


def projection_scenarios(inp, qb):
    base = add_model_projections(inp).set_index("player").model_projection
    rb_down = inp.copy()
    rb_down.loc[
        rb_down.position.eq("RB"),
        [
            "rush_attempts",
            "targets",
            "rush_td",
            "rec_td",
            "prob_100_rush",
            "prob_100_rec",
        ],
    ] *= 0.8
    rb_score = add_model_projections(rb_down).set_index("player").model_projection
    passing_down = inp.copy()
    team = inp.loc[inp.player.eq(qb), "team"].iloc[0]
    passing_down.loc[
        passing_down.player.eq(qb), ["pass_attempts", "pass_td", "prob_300_pass"]
    ] *= 0.8
    passing_down.loc[
        passing_down.team.eq(team) & passing_down.position.isin(["RB", "WR", "TE"]),
        ["targets", "rec_td", "prob_100_rec"],
    ] *= 0.8
    qb_score = add_model_projections(passing_down).set_index("player").model_projection
    az_revert = inp.copy()
    az_revert.loc[az_revert.player.eq("Michael Wilson"), "targets"] -= 0.50
    az_revert.loc[az_revert.player.eq("Michael Wilson"), "rec_td"] -= 0.05
    az_revert.loc[az_revert.player.eq("Trey McBride"), "targets"] -= 0.75
    az_revert.loc[az_revert.player.eq("Trey McBride"), "rec_td"] -= 0.05
    az_score = add_model_projections(az_revert).set_index("player").model_projection
    return {
        "mean": base,
        "rb_workload_down20": rb_score,
        "qb_passing_down20": qb_score,
        "arizona_uplift_reverts": az_score,
    }


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    inp = refresh(pd.read_csv(OLD))
    if inp.player.duplicated().any():
        raise ValueError("Duplicate player")
    inp.to_csv(OUT / "projection_inputs.csv", index=False)
    pool = add_model_projections(inp)
    pool[
        [
            "player",
            "team",
            "position",
            "salary",
            "model_projection",
            "model_floor",
            "model_ceiling",
            "value_per_1000",
        ]
    ].to_csv(OUT / "projections.csv", index=False, float_format="%.4f")
    # Analyst lineup bands; NO statistical mapping from field size to EV.
    choices = [
        ("1000-3000", "Drake Maye", 1, False, ()),
        ("4000-6000", "Jacoby Brissett", 2, True, ()),
        ("15000-25000", "Tyson Bagent", 2, True, ()),
        ("gibbs_alternative", "Jacoby Brissett", 1, False, ("Jahmyr Gibbs",)),
    ]
    lineup_rows, summary_rows = [], []
    for band, qb, stack, bringback, locks in choices:
        optimal = optimize_lineup(
            pool,
            ["model_projection"],
            quarterback=qb,
            min_stack=stack,
            bring_back=bringback,
            locks=locks,
            exclude=HELD,
            max_tight_ends=2,
        )
        lineup = assign_slots(optimal)
        scenarios = projection_scenarios(inp, qb)
        row = {"field_band": band, "qb": qb, "salary": int(lineup.salary.sum())}
        for name, series in scenarios.items():
            row[name] = round(float(series.loc[lineup.player].sum()), 4)
        summary_rows.append(row)
        for _, p in lineup.iterrows():
            lineup_rows.append(
                {
                    "field_band": band,
                    "slot": p.slot,
                    "player": p.player,
                    "team": p.team,
                    "position": p.position,
                    "salary": int(p.salary),
                    "model_projection": round(float(p.model_projection), 4),
                    "condition": p.condition,
                }
            )
    pd.DataFrame(lineup_rows).to_csv(
        OUT / "lineups.csv", index=False, float_format="%.4f"
    )
    pd.DataFrame(summary_rows).to_csv(
        OUT / "comparison.csv", index=False, float_format="%.4f"
    )
    artifacts = [
        OLD,
        Path(__file__),
        OUT / "projection_inputs.csv",
        OUT / "projections.csv",
        OUT / "lineups.csv",
        OUT / "comparison.csv",
    ]
    manifest = {
        "as_of": "2026-10-10 Saturday, provisional before Sunday inactives",
        "research_only": True,
        "field_size_expected_value_model": False,
        "verified_contest_salary_export": False,
        "ownership_projections_verified": False,
        "optimization": "SciPy MILP, max single-scenario mean within 44 player pool",
        "risk_metrics": "Separate deterministic sensitivities, not probabilities",
        "sha256": {
            str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in artifacts
        },
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(pd.DataFrame(summary_rows).to_string(index=False))


if __name__ == "__main__":
    main()
