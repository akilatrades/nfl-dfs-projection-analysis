# Week 4 audit — October 8, 2026

The saved entries reconcile: both the $50 single-entry and Millionaire builds total **153.62 points**, and the $27 single-entry build totals **137.52**. Each used **$49,800** and nine unique players. These are repository-recorded results; contest exports, actual ownership, ranks and payouts remain unavailable.

## What the comparison establishes

The raw build beat the ownership-adjusted build by 16.10 points. Kyren Williams instead of James Cook contributed +20.40; Parker Washington instead of Jakobi Meyers contributed -4.30. The saved simulated means differed by only 3.70. A single realized result cannot establish that ownership adjustments are generally harmful or that the higher-ceiling build had better expected payout.

The $50 and Millionaire entries overlap 9/9 players. The $27 entry overlaps 7/9 with each. This measures concentration, not evidence that duplicating the lineup was necessarily suboptimal; contest payouts and joint outcomes would be needed to establish that.

## Forecast coverage and snapshot mismatch

There are 11 distinct entered players. Only **3** have football inputs that can be rerun with the committed scoring model: Burrow, Chase and Higgins. The saved player pool covers **3**, and the selected error sample covers **5**. Six entered players have no projection in any of these sources. Missing forecasts remain blank, never zero.

Burrow is 19.8067 in the recomputed inputs but 18.4317 in the saved pool. Parker and Cook have saved pool estimates but no corresponding football-input rows. The five-player error sample combines these versions; it is not one verified final pre-lock snapshot. `player_coverage.csv` exposes each source separately.

| Diagnostic | Value | Scope |
|---|---:|---|
| Mean absolute error | 9.56 | Selected five-player sample |
| Root mean squared error | 10.86 | Same sample |
| Mean signed error | +0.14 | Actual minus forecast |
| Four-player stack net error | +1.14 | Burrow / Chase / Higgins / Parker |
| Sum of absolute stack errors | 47.39 | Same four players |

The small aggregate error results from cancellation. It does **not** demonstrate calibrated game environments, player allocation or simulated tails. One realized score below P95 is not a coverage test.

## Volume, efficiency, touchdowns and injuries

The archived files do not contain complete realized targets, routes, carries and component projections for every entered player. A numerical volume/efficiency/TD decomposition would require inventing missing data. In particular, Parker's 2.00 points cannot tell us which input was wrong.

The Chase injury is recorded in the existing review. Independent reporting also describes Higgins leaving with an adductor injury ([Reuters, October 4](https://www.reuters.com/sports/bengals-wr-jamarr-chase-ruled-out-with-concussion--flm-2026-10-04/)). The old sample labels Higgins as ordinary football variance. Retain that original label for traceability, but do not treat it as a verified injury classification.

The all-player error is the primary diagnostic. The mechanical exclusion of Chase is a sensitivity only: MAE 9.52, RMSE 11.13 across four selected players. It is neither an estimate of injury-free performance nor a complete non-injury subset. Replacing Chase's actual points with a forecast while keeping teammates fixed is also not a causal estimate of what would have happened.

## Changes carried into Week 5

- Save numerical inputs for every candidate, with source and assumption labels.
- Search complete salary-valid rosters; permit optional bring-backs rather than forcing a weak one.
- Compare mean and workload-stress objectives. Keep speculative receiver roles explicit.
- Rebuild whole lineups after exclusions; do not suggest swaps that exceed the cap.
- Preserve the original Week 4 files. This audit is an appended correction, not a new pre-game forecast.

Run `python run_week4_audit.py` from the repository root to regenerate the three audit outputs. Broader calibration and a retrospective optimal Week 4 lineup cannot be established from the incomplete saved pool.
