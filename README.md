# NFL DFS projection analysis

[![tests](https://github.com/akilatrades/nfl-dfs-projection-analysis/actions/workflows/tests.yml/badge.svg)](https://github.com/akilatrades/nfl-dfs-projection-analysis/actions/workflows/tests.yml)

Can writing down my assumptions about volume, scoring and lineup correlation, before kickoff, make my DraftKings lineups better over time?

**Honest status: four weeks in, no edge claimed.** What this repository does is keep the pre-game reasoning and the post-game review side by side so I can see where I was wrong. The projections start from football inputs (pass attempts, targets, carries, efficiency, touchdown chances) rather than someone else's fantasy-point forecast, so a miss can be traced to a specific assumption.

## Week by week

| Week | What I did | What happened | What I changed |
|---|---|---|---|
| 3 | First single-entry lineups | [Review](weeks/2026_week_03/README.md): too much weight on individually cheap or efficient players | Shifted to strong game environments, players who score together, overall upside, and only a little contrarianism |
| 4 | First full test of the revised process: $50 and $27 single entry, $20 Millionaire | $50 lineup **153.62** DK points (simulation average 130.6, 95th percentile 178.7); the ownership-adjusted $27 lineup **137.52** | Lesson: don't give up expected points to be less popular. [Audit](weeks/2026_week_04/audit_2026-10-08/README.md): only 3 of 11 entered players had reproducible input forecasts, so inputs are now saved for every candidate |
| 6 | First week with fitted inputs: every player's Week 1–5 rates shrunk toward a position baseline, lines from the schedule file, salaries from three articles | [Pre-slate record](weeks/2026_week_06/README.md): leading builds within three points of each other; the Rams game and Kenneth Walker in every construction; decision waits on the Friday designations | Nothing yet; the test is whether fitted inputs beat the hand-set ones of Weeks 4–5 |
| 5 | Two single-entry contests, [$5 / ~23K](weeks/2026_week_05/sunday_2026-10-11/monte_carlo_2026-10-11/README.md) and [$3 / ~7K](weeks/2026_week_05/sunday_2026-10-11/contest_3usd_7k_2026-10-11/README.md), with a correlated Monte Carlo over 13 candidate lineups | [Reconciled scores](weeks/2026_week_05/postslate_2026-10-11/README.md) of **153.86** and **120.14**; rank, ownership and payout not yet recorded | [Process correction](weeks/2026_week_05/sunday_2026-10-11/process_review_2026-10-11/README.md) stress-tests the workload assumptions and removes a forced weak run-back |

Week 4 in a little more detail, because it was the first real test: Burrow (28.7), Higgins (29.7), Kyren Williams (36.7) and Hockenson (27.9) did what the game-environment thesis said. Chase scored 5.7 after a concussion, which I count as noise. Parker Washington scored 2.0, and he is the real lesson: he was chosen as the Jacksonville piece to pair with the Cincinnati stack, and his own role was too thin for the correlation to matter.

The simulations are scenario estimates of my own lineups' scores. They are not contest win probabilities, because I do not model the rest of the field. Until contest rank, the cash line and actual ownership are in the records, I cannot say whether any of this beats a simple projection.

## How the process works

```text
public football and market inputs
  -> expected volume and efficiency per player
  -> projections, floor and ceiling, position percentiles, salary-based hit rates, ownership estimate
  -> game-environment ranking and correlation
  -> candidate lineups compared under explicit scenarios
  -> pre-lock decision record (frozen)
  -> post-slate scoring and error review
```

| Area | What the code does |
|---|---|
| Projection engine | Turns expected passing, rushing, receiving and DST inputs into DraftKings points |
| Uncertainty | Ranges plus a simulation of the upper tail |
| Ownership | A simple popularity estimate from the project's own metrics |
| Relative strength | Position-specific percentiles for projection, ceiling and value |
| Tournament metrics | 3x and 4x hit probabilities and a leverage index |
| Sensitivity | Re-runs projections after controlled changes to key assumptions |
| Game environment | Ranks games on totals, team totals, spread and role concentration |
| Lineup analysis | Salary, projection, ceiling, correlation, ownership and the lineup's thesis |
| Audit trail | Pre-slate assumptions stored apart from the post-slate review |

[Methodology](docs/methodology.md) · [Limitations](docs/limitations.md)

## Reproduce

```bash
pip install -r requirements.txt
pytest
python run_projections.py weeks/2026_week_04/projection_inputs.csv
python run_statistical_analysis.py weeks/2026_week_04/player_pool.csv
python run_week4_audit.py
python run_week5_research.py          # and run_single_entry*.py, run_week5_*.py for the dated snapshots
python run_baseline_inputs.py weeks/2026_week_06/public_stat_snapshot.csv   # Week 6: fitted inputs from public stats
python run_week6_research.py
```

Tests cover projection arithmetic, value calculations, percentiles, hit probabilities, the deterministic simulation, sensitivity analysis and input validation.

## Limitations

- The football inputs are my own estimates, saved before lock but not sourced from a feed.
- The ownership model is simple and uncalibrated against real ownership.
- Parts of the uncertainty layer use normal and truncated-normal approximations.
- The correlated lineup simulation is not yet part of the core reproducible pipeline; it is kept as dated research.
- Three weeks is not a record. Nothing here is a claim of a long-term advantage, and nothing is a guarantee of a contest result.

## What I learned / what I would do differently

A high simulated ceiling is not validation. I would build a longer record with contest rank, cash line, actual ownership and forecast error against a simple baseline before describing any advantage. The weekly files keep the assumptions and reviews that comparison will need.
