# Week 8 postmortem — reviewed November 2, 2026

## Finding

The selected Lamar/Bijan roster reconstructs to **86.6 DK points versus a saved 140.4 projection**, conditional on retaining the nine recorded players including D.J. Moore. No final contest export or screenshot has been supplied. Rank, payout, net return, ownership, duplication and the actual winning roster are unknown. These are reconstructed player points, not a verified settled entry result.

The largest immediate cause was Lamar Jackson's **new right-thumb injury on Baltimore's first offensive snap**, followed by Tyler Huntley's toe injury and an emergency third quarterback. This was distinct from Lamar's pre-existing ankle injury. The evidence does not establish that the ankle caused the thumb injury, or that we should have predicted a first-play exit. Three correlated Baltimore roster positions nevertheless depended on the quarterback staying productive.

| Player | Saved forecast | Reconstructed DK | Error |
|---|---:|---:|---:|
| Lamar Jackson | 20.0 | 0.0 | -20.0 |
| Bijan Robinson | 25.0 | 7.6 | -17.4 |
| Braelon Allen | 19.4 | 26.3 | +6.9 |
| Zay Flowers | 18.8 | 0.0 | -18.8 |
| Wan'Dale Robinson | 11.8 | 16.7 | +4.9 |
| D.J. Moore | 11.7 | 17.6 | +5.9 |
| Mark Andrews | 8.8 | 4.4 | -4.4 |
| Rhamondre Stevenson | 18.9 | 12.0 | -6.9 |
| Broncos DST | 6.0 | 2.0 | -4.0 |
| Total | 140.4 | 86.6 | -53.8 |

Lamar/Flowers/Andrews cost $17,400 (34.8% of the $50,000 cap), projected for 47.6 and returned 4.4. Their 43.2-point deficit equals about 80.3% of the total net forecast shortfall. That is an arithmetic attribution, not a causal estimate that injury alone explains every missing point. We cannot observe the counterfactual healthy-Lamar score.

Scoring details: Braelon 147 rushing yards, one rushing TD, two catches for six yards plus the 100-yard rushing bonus = 26.3. Wan'Dale 6/57/1 less one lost fumble = 16.7. Moore 4/82/1 plus four rushing yards less one lost fumble = 17.6. Stevenson 82 rushing yards and 3/8 receiving = 12.0. Denver recorded two sacks, no takeaways and allowed 24 points, giving 2.0. DraftKings uses -1 per lost fumble, full PPR and +3 at 100 rushing yards. Other sites' standard/half-PPR totals cannot be copied directly.

## Outcome versus decision quality

**Immediate bad outcome:** Baltimore lost its first two quarterbacks. Flowers caught none of five targets; Andrews caught three for 14. Buffalo scored 36 while Baltimore scored ten. A high combined market total did not guarantee two productive passing attacks or the intended receiving-TD allocation.

**Avoidable modeling problem:** The saved `run.py` draws positive non-TD score components for every offensive player; it has no explicit playing-time/injury-exit state or backup-QB switch affecting the entire passing offense. `news_rebuild.py` adds 15% cuts to Moore/Kincaid/Pickens and 10% to Braelon under a hand-chosen stress. Earlier code cuts Andrews 25% and selected other roles. It does not create a joint Lamar/Flowers/Andrews QB-exit scenario. A generic high-game-scoring cut is a different experiment from a QB exiting on the first play. The previously shown P10 of 104.1 was conditional on this incomplete model and was uncalibrated. More Monte Carlo draws cannot repair the omitted mechanism.

**Avoidable construction/process weakness:** We had identified Andrews' weak recent receiving production (four catches for 27 yards over the previous two games), but reintroduced him as a cheap correlated touchdown bet to fit Bijan. This was a tradeoff, not independent evidence of a bounceback. A single-receiver Lamar stack deserved an explicit like-for-like comparison before buying the second Baltimore receiver. This loss does not establish a universal rule against double stacks.

**Premium-spend miss:** Bijan returned 7.6 from 19 carries for 76 yards, no reception and no TD as Atlanta was shut out. The 25-point forecast was a large bet at $8,500, requiring receiving/TD production that did not arrive. The pregame notes flagged Tampa weather but did not show a separately calibrated weather scenario or establish how much the public mean already incorporated it. The result alone does not prove Bijan was a bad pregame play or that weather alone caused his miss.

**Late-decision instability:** Recommendations changed repeatedly; the initial Allen comparison fixed Shakir and excluded then-questionable Moore/Kincaid as candidates. We corrected this after questioning, but the broader workflow should have reopened eligibility immediately after official actives and compared stack partners in one consistent search. The later rebuilt search still used declared fixed cores, one public projection board, subjective TD shares/variance and hand-chosen candidate restrictions. Constraints such as one cheap WR improve reviewability but are judgment choices, not statistical discoveries.

**Contest-fit limitation:** There was no calibrated 2,591-entry opponent field, current contest ownership, duplication estimate, payout ladder EV or validated first-place probability. We could compare a chosen score benchmark under the model, but could not establish that the top simulated tail was the best lineup to win this specific contest. I gave the simulation rankings more practical weight than their validation justified.

## What worked and what to retain

- Braelon's Hall-out workload case materialized: 21 carries, 147 yards and a touchdown, plus two catches. His production exceeded the saved mean by 6.9 DK points. One outcome supports the workload observation, not a claim of calibrated predictive skill.
- Wan'Dale returned 16.7 at $4,200, +4.9 over forecast. His seven targets remained in the same six-to-seven range as the previous three games; we should not attribute the result to a proven target-share surge from Carnell Tate's absence.
- Moore returned 17.6 versus 11.7 despite a lost fumble. His shoulder did not ruin this roster; seven targets, four catches, 82 receiving yards and a TD paid off. Keeping a credible Bills bring-back was defensible, although a bring-back should never be compulsory.
- Stevenson had 22 touches (19 carries/three catches), validating meaningful opportunity. His 12 points fell short because the receiving yardage/TD outcome was modest. A disappointing score does not by itself invalidate the volume case.
- Recorded pregame projections, candidates, constraints, rosters and alternate constructions survived. This review uses those original forecasts rather than retrospectively changing them.

## Next-slate changes required before relying on the model

1. Build playing-time and team-passing downside scenarios, including early QB exits that jointly affect receivers. Fit baseline frequencies to historical data; do not invent an injury probability for Lamar from this one event. Show full-game-conditional and unconditional forecasts separately when possible.
2. Require a volume/route/red-zone justification for the second stack receiver. Compare single and double stacks at similar salary, projection source and data time, accounting for opportunity cost elsewhere.
3. Reopen all eligible players on official actives, including Moore/Kincaid/Pickens-type returns, and apply explicit workload uncertainty. Keep a consistent candidate policy through the final comparison. A material news change can justify an amendment; a question alone should trigger a check rather than an unsupported roster change.
4. Use multiple timestamped forecasts and test sensitivity to receiving/TD assumptions, premium-RB opportunity cost and relevant weather. Calibration needs many slates. One bad slate cannot identify precise new multipliers or prove an edge.
5. Limit contest-winning and uniqueness claims to what observed field/ownership/payout data support. Use score simulations as scenario comparisons until a field model is tested.
6. Reconcile the final entered roster, actual score, final contest size, rank and payout from a DraftKings export or screenshot. If Moore was changed, reconstruct that actual roster separately and preserve this selection record.

These are required follow-up changes, **not implemented or validated model fixes**. Pregame files are preserved. No new strategy is declared profitable or winning from this review.

## Sources

Retrieved November 2, 2026.

- Saved selection: ../high_total_simulation/selected_entry.json
- Saved forecasts/assumptions: ../high_total_simulation/news_rebuild_results.json and ../high_total_simulation/news_rebuild.py
- Original score model: ../high_total_simulation/run.py
- Official injury account: https://www.baltimoreravens.com/news/ravens-bills-blowout-week-8-lamar-jackson-tyler-huntley-joe-fagnano-injuries
- Injury chronology: https://www.baltimoreravens.com/news/joe-fagnano-tyler-huntley-injured-toe-questionable-emergency-quarterback
- BAL/BUF box score: https://www.pro-football-reference.com/boxscores/202611010buf.htm (search-index table retrieved; direct request returned 403); cross-check https://www.footballdb.com/games/boxscore/baltimore-ravens-vs-buffalo-bills-2026110102 and https://www.baltimoreravens.com/game-day/box-scores/
- Bijan/Atlanta box: https://www.atlantafalcons.com/game-day/2026/reg-week8/falcons-at-buccaneers/
- Braelon official log: https://www.newyorkjets.com/team/players-roster/braelon-allen/logs/
- Wan'Dale official log: https://www.tennesseetitans.com/team/players-roster/wan-dale-robinson/logs/
- Moore official log: https://www.buffalobills.com/team/players-roster/dj-moore/logs/
- Stevenson official box: https://www.patriots.com/game-day/2026/reg-week8/patriots-at-dolphins/box-score
- Denver sacks/turnovers: https://www.pro-football-reference.com/boxscores/202611010den.htm (search-index table); points/scoring cross-check https://www.chiefs.com/game-day/2026/reg-week8/chiefs-at-broncos/
- Denver 2.0 cross-check: https://margin.football/players/denver-broncos-defense/week-8
- DK scoring: https://dknetwork.draftkings.com/2025/08/27/nfl-dfs-beginners-guide-draftkings/

Reproduce the arithmetic with `python weeks/2026_week_08/postmortem/reconstruct.py`; results are in `reconstructed_results.json`.
