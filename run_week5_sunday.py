"""Sunday Week 5 single-entry screen, versioned after Oct 9 and Oct 10 research.

Usage:
    python run_week5_sunday.py
    python -m unittest discover -s tests -v

Produces provisional pre-lock player inputs, alternative-game lineups,
sensitivity comparisons and a hash manifest. Does NOT predict contest EV,
use verified contest player IDs, or estimate joint field ownership.
"""

import hashlib
import json
from pathlib import Path

import pandas as pd

from run_week5_saturday import OLD as FRIDAY_INPUTS
from run_week5_saturday import refresh as saturday_refresh
from src.optimizer import assign_slots, optimize_lineup
from src.projections import add_model_projections

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "weeks/2026_week_05/sunday_2026-10-11"
HELD = (
    "Mitch Tinsley",
    "Dohnte Meyers",
    "Stefon Diggs",
    "Jaylen Warren",
    "Malik Nabers",
    "Emanuel Wilson",
)
CHALK = (
    "Jahmyr Gibbs",
    "Michael Wilson",
    "Trey McBride",
    "D'Andre Swift",
    "Amon-Ra St. Brown",
)
# Published Fantasy Alarm Oct 10, not actual contest ownership.
OWN = {
    "Jahmyr Gibbs": 33.5,
    "Michael Wilson": 33.1,
    "Trey McBride": 31.3,
    "D'Andre Swift": 30.8,
    "Braelon Allen": 27.1,
    "Amon-Ra St. Brown": 24.8,
    "Chase Brown": 22.1,
    "Jacoby Brissett": 19.0,
}
SPECS = [
    (
        "purdy_kittle_arizona",
        "Brock Purdy",
        ("George Kittle", "Trey McBride"),
        False,
        1,
        2,
    ),
    (
        "maye_gibbs_mcbride",
        "Drake Maye",
        ("Romeo Doubs", "Jahmyr Gibbs", "Trey McBride"),
        False,
        2,
        2,
    ),
    (
        "love_watson_arizona",
        "Jordan Love",
        ("Christian Watson", "Trey McBride", "D'Andre Swift"),
        True,
        1,
        2,
    ),
    ("maye_doubs_arizona", "Drake Maye", ("Romeo Doubs",), False, 1, 2),
    ("maye_doubs_bowers", "Drake Maye", ("Romeo Doubs", "Brock Bowers"), True, 1, 2),
    (
        "purdy_kittle_gibbs",
        "Brock Purdy",
        ("George Kittle", "Jahmyr Gibbs"),
        False,
        1,
        2,
    ),
    (
        "brissett_gibbs_comparison",
        "Jacoby Brissett",
        ("Trey McBride", "Jahmyr Gibbs"),
        False,
        2,
        3,
    ),
]


def append_player(df: pd.DataFrame, template_name: str, patch: dict) -> pd.DataFrame:
    if not df.player.eq(template_name).any():
        raise ValueError("Missing player template: " + template_name)
    if set(patch) - set(df.columns):
        raise ValueError("Unknown football input field")
    template = df.loc[df.player.eq(template_name)].iloc[0].copy()
    for key, value in patch.items():
        template[key] = value
    return pd.concat([df, template.to_frame().T], ignore_index=True)


def sunday_inputs() -> pd.DataFrame:
    df = saturday_refresh(pd.read_csv(FRIDAY_INPUTS))
    numerics = df.select_dtypes(include="number").columns
    updates = {
        "Romeo Doubs": {
            "targets": 7.5,
            "rec_td": 0.35,
            "condition": "Hollins on IR; 7.5 target scenario, not measured",
        },
        "DK Metcalf": {
            "targets": 7.0,
            "rec_td": 0.40,
            "condition": "Rain sensitivity: seven-target scenario, not weather model",
        },
        "Braelon Allen": {
            "rush_attempts": 18.5,
            "yards_per_carry": 3.9,
            "rush_td": 0.45,
            "targets": 4.0,
            "catch_rate": 0.72,
            "yards_per_reception": 6.0,
            "rec_td": 0.08,
            "prob_100_rush": 0.15,
            "condition": "Breece Hall OUT; workload remains an analyst assumption",
        },
    }
    for name, patch in updates.items():
        mask = df.player.eq(name)
        if mask.sum() != 1:
            raise ValueError("Cannot locate player to revise: " + name)
        for key, value in patch.items():
            df.loc[mask, key] = value

    qbs = [
        (
            "Brock Purdy",
            "SF",
            "SEA",
            6500,
            "2026-10-11T20:25:00Z",
            34.0,
            0.68,
            11.8,
            2.1,
            0.65,
            3.0,
            4.5,
            0.06,
            0.30,
        ),
        (
            "Jordan Love",
            "GB",
            "CHI",
            5700,
            "2026-10-11T17:00:00Z",
            38.0,
            0.65,
            10.5,
            1.9,
            0.75,
            3.0,
            3.8,
            0.07,
            0.25,
        ),
        (
            "Kirk Cousins",
            "LV",
            "NE",
            5400,
            "2026-10-11T17:00:00Z",
            36.0,
            0.67,
            11.2,
            1.8,
            0.75,
            1.5,
            1.0,
            0.01,
            0.25,
        ),
    ]
    for (
        name,
        team,
        opp,
        salary,
        kickoff,
        attempts,
        rate,
        ypc,
        passing_tds,
        ints,
        rushes,
        ypr,
        rushing_tds,
        bonus,
    ) in qbs:
        df = append_player(
            df,
            "Drake Maye",
            {
                "player": name,
                "team": team,
                "opponent": opp,
                "salary": salary,
                "salary_source": "DKN_WEEK5_OCT09",
                "salary_verification": "published_article_not_contest_export",
                "as_of": "2026-10-11",
                "kickoff_utc": kickoff,
                "pass_attempts": attempts,
                "completion_rate": rate,
                "yards_per_completion": ypc,
                "pass_td": passing_tds,
                "interceptions": ints,
                "rush_attempts": rushes,
                "yards_per_carry": ypr,
                "rush_td": rushing_tds,
                "prob_300_pass": bonus,
                "condition": "Manual Sunday role and efficiency assumptions",
            },
        )
    df = append_player(
        df,
        "Trey McBride",
        {
            "player": "George Kittle",
            "position": "TE",
            "team": "SF",
            "opponent": "SEA",
            "salary": 5200,
            "salary_source": "ROTOWIRE_OCT10",
            "salary_verification": "published_article_not_contest_export",
            "as_of": "2026-10-11",
            "kickoff_utc": "2026-10-11T20:25:00Z",
            "targets": 7.5,
            "catch_rate": 0.72,
            "yards_per_reception": 10.7,
            "rec_td": 0.50,
            "prob_100_rec": 0.16,
            "condition": "Manual target and TD scenario, confirm active",
        },
    )
    for col in numerics:
        df[col] = pd.to_numeric(df[col], errors="raise")
    if df.player.duplicated().any() or len(df) != 48:
        raise ValueError("Sunday candidate pool identity mismatch")
    df["as_of"] = "2026-10-11 morning before final inactives"
    return df


def football_scenarios(df: pd.DataFrame, qb: str) -> dict:
    def scores(table):
        return add_model_projections(table).set_index("player").model_projection

    scenarios = {"mean": scores(df)}
    rb = df.copy()
    cols = [
        "rush_attempts",
        "rush_td",
        "targets",
        "rec_td",
        "prob_100_rush",
        "prob_100_rec",
    ]
    rb.loc[rb.position.eq("RB"), cols] *= 0.80
    scenarios["rb_workload_down20"] = scores(rb)

    qb_down = df.copy()
    team = df.loc[df.player.eq(qb), "team"].iloc[0]
    qb_down.loc[
        qb_down.player.eq(qb), ["pass_attempts", "pass_td", "prob_300_pass"]
    ] *= 0.80
    qb_down.loc[
        (qb_down.team.eq(team) & qb_down.position.isin(["RB", "WR", "TE"])),
        ["targets", "rec_td", "prob_100_rec"],
    ] *= 0.80
    scenarios["qb_passing_down20"] = scores(qb_down)

    game_down = df.copy()
    game = game_down.team.isin(["DET", "ARI"])
    for pos, fields in [
        ("QB", ["pass_attempts", "pass_td", "prob_300_pass"]),
        (
            "RB",
            [
                "rush_attempts",
                "rush_td",
                "targets",
                "rec_td",
                "prob_100_rush",
                "prob_100_rec",
            ],
        ),
        ("WR", ["targets", "rec_td", "prob_100_rec"]),
        ("TE", ["targets", "rec_td", "prob_100_rec"]),
    ]:
        game_down.loc[game & game_down.position.eq(pos), fields] *= 0.8
    scenarios["det_ari_offense_down20"] = scores(game_down)
    return scenarios


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    df = sunday_inputs()
    df.to_csv(OUT / "projection_inputs.csv", index=False)
    pool = add_model_projections(df)
    pool[
        [
            "player",
            "position",
            "team",
            "salary",
            "model_projection",
            "model_floor",
            "model_ceiling",
            "value_per_1000",
        ]
    ].to_csv(OUT / "projections.csv", index=False, float_format="%.4f")
    lineup_rows, comparisons = [], []
    for name, qb, locks, bringback, nmin, nmax in SPECS:
        optimal = optimize_lineup(
            pool,
            ["model_projection"],
            quarterback=qb,
            locks=locks,
            bring_back=bringback,
            min_stack=1,
            exclude=HELD,
            max_tight_ends=2,
            team_group_bounds=(("DET", "ARI"), nmin, nmax),
            player_group_bounds=(CHALK, 0, 3),
        )
        lineup = assign_slots(optimal)
        players = set(lineup.player)
        if not set(locks).issubset(players) or int(lineup.salary.sum()) > 50000:
            raise ValueError("Lineup postcondition failed")
        if not (nmin <= lineup.team.isin(["DET", "ARI"]).sum() <= nmax):
            raise ValueError("Game concentration constraint failed")
        scen = football_scenarios(df, qb)
        comparison = {
            "candidate": name,
            "qb": qb,
            "salary": int(lineup.salary.sum()),
            "high_ownership_count": int(lineup.player.isin(CHALK).sum()),
            "source_ownership_over25_count": int(
                lineup.player.map(lambda x: OWN.get(x, 0) >= 25).sum()
            ),
            "game_players": int(lineup.team.isin(["DET", "ARI"]).sum()),
        }
        for label, values in scen.items():
            comparison[label] = round(float(values.loc[lineup.player].sum()), 4)
        comparisons.append(comparison)
        for _, p in lineup.iterrows():
            lineup_rows.append(
                {
                    "candidate": name,
                    "slot": p.slot,
                    "player": p.player,
                    "position": p.position,
                    "team": p.team,
                    "opponent": p.opponent,
                    "salary": int(p.salary),
                    "kickoff_utc": p.kickoff_utc,
                    "model_projection": round(float(p.model_projection), 4),
                    "published_oct10_ownership_pct": OWN.get(p.player),
                    "condition": p.condition,
                }
            )
    pd.DataFrame(comparisons).to_csv(
        OUT / "comparison.csv", index=False, float_format="%.4f"
    )
    pd.DataFrame(lineup_rows).to_csv(
        OUT / "lineups.csv", index=False, float_format="%.4f"
    )
    source_paths = [
        FRIDAY_INPUTS,
        ROOT / "run_week5_saturday.py",
        ROOT / "run_week5_sunday.py",
        ROOT / "src/optimizer.py",
        ROOT / "src/projections.py",
        OUT / "projection_inputs.csv",
        OUT / "projections.csv",
        OUT / "comparison.csv",
        OUT / "lineups.csv",
    ]
    manifest = {
        "status": "Sunday pre-inactives provisional; no upload-ready IDs",
        "date": "2026-10-11",
        "lineage": "Oct 9 frozen baseline -> Oct 10 changes -> Oct 11 scenario",
        "n_players": len(pool),
        "n_candidate_specs": len(SPECS),
        "selection_objective": "max model mean with constraints",
        "field_size_is_analyst_label_not_optimized_contest_ev": True,
        "model_is_calibrated": False,
        "scenario_probabilities_assigned": False,
        "salary_export_verified": False,
        "ownership": "Oct 10 Fantasy Alarm estimates where available only",
        "sha256": {
            str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in source_paths
        },
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(pd.DataFrame(comparisons).to_string(index=False))


if __name__ == "__main__":
    main()
