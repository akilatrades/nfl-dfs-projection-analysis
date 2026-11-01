# Updated five lineups after confirmed early inactives — November 1, 2026

This is the latest shortlist for one $27 NFL $60K Blind Side single entry (maximum 2,591). It supersedes the previous final checks as a current recommendation; prior research is preserved. No entry is submitted by this workflow.

My tournament preference is option 1, Allen–Moore–Kincaid with Flowers answering. Option 2 is the previous Allen–Moore/London construction and remains a reasonable choice with less Buffalo receiving concentration. A small simulated difference does not prove a better contest-winning chance.

| Slot | 1 Allen double stack | 2 Allen / London | 3 Dak / McBride | 4 Lamar / Bijan | 5 Brissett |
|---|---|---|---|---|---|---|
| QB | Josh Allen | Josh Allen | Dak Prescott | Lamar Jackson | Jacoby Brissett |
| RB1 | Bhayshul Tuten | Braelon Allen | Jonah Coleman | Bijan Robinson | Jonah Coleman |
| RB2 | Braelon Allen | Rhamondre Stevenson | Braelon Allen | Braelon Allen | Braelon Allen |
| WR1 | Zay Flowers | Zay Flowers | CeeDee Lamb | Zay Flowers | CeeDee Lamb |
| WR2 | Wan'Dale Robinson | Drake London | DK Metcalf | Wan'Dale Robinson | Michael Wilson |
| WR3 | DJ Moore | DJ Moore | Demario Douglas | DJ Moore | Demario Douglas |
| TE | Dalton Kincaid | Brenton Strange | Trey McBride | Mark Andrews | Trey McBride |
| FLEX | Rhamondre Stevenson | Wan'Dale Robinson | Rhamondre Stevenson | Rhamondre Stevenson | Rhamondre Stevenson |
| DST | Broncos | Broncos | Broncos | Broncos | Chargers |
| Salary | $50,000 | $49,800 | $49,900 | $49,800 | $49,800 |
| Projection | 139.1 | 137.9 | 139.1 | 140.4 | 136.3 |
| Simulated P90 | 179 | 176 | 179 | 180 | 178 |
| Assumed role-downside mean | 129.4 | 128.2 | 129.4 | 130.2 | 126.6 |

## Why these options

1. Allen/Moore/Kincaid/Flowers concentrates four players in the high-total Buffalo game while retaining three running backs. Moore and Kincaid compete for targets and both return from injury; active status is not an assurance of unrestricted workload. Wan'Dale is the single cheap WR. Tuten shares his backfield. This is a deliberate ceiling scenario, not a claim that both Bills receivers inherit the same missing targets.
2. Keep the previous Moore/London/Strange version for less concentration in Buffalo. London trades Kincaid/Tuten exposure for a standalone WR role, with Tampa weather risk. Wan'Dale is still the cheap WR. It has the lower modeled upper tail but does not require another injury-return Bills player.
3. Dak/Lamb with McBride targets Dallas–Arizona and keeps Braelon/Stevenson. Coleman is a budget RB with Dobbins competition; Douglas benefits from unavailable New England receivers but still has an uncertain ceiling.
4. Lamar/Flowers/Andrews with Moore answering uses the QB discount to fit Bijan alongside Braelon and Stevenson. Lamar returns from an ankle injury, Andrews has weak recent receiving production, and the modeled ceiling depends on that allocation working. Bijan offers a different premium RB scoring path.
5. Brissett/McBride/Michael Wilson with Lamb answering is the more concentrated Arizona alternative. Coleman, Douglas and Chargers DST are compromises. Chargers defensive injuries and the Rams matchup are substantial risks. This is my least preferred of these five.

## Verified updates and controls

- Bills officially list Moore and Kincaid active; Shakir remains eligible, but is no longer forced into all Allen lineups. George Pickens is also eligible after his confirmed active status.
- Hall is inactive. Braelon is available throughout the pool and selected by the search; he is not forced in every family.
- Henderson and A.J. Brown are out. Stevenson appears in all five based on salary/projection, not a mandatory-player constraint. Patriots late inactives remain pending in the retrieved early-game roundup.
- Calvin Ridley is treated as active, consistent with the Titans official inactive list and the sourced Schefter report. One secondary roundup incorrectly lists him out; no Ridley absence boost is applied to Wan'Dale.
- Every early offensive player in these five is absent from the relevant checked early inactive lists. Coleman, Stevenson and Chargers/Broncos DST play late; final game-day lists were not yet available in the retrieved early roundup.
- At most one WR below $5,000, at most one designated speculative-role punt, no Lane or Bourne. These are judgment controls motivated by prior cheap-receiver failures, not validated statistical rules.
- One QB/TE/DST, 2–3 RB, 3–4 WR, nine distinct players, salary <= $50,000, maximum three offensive teammates, and no DST opposing a rostered offensive player. All five are distinct. Salaries use public boards, not an official contest export.
- In three-RB lineups Stevenson is in FLEX to preserve late-swap flexibility. Option 2 has only two RB and leaves Stevenson at RB.

## Simulation and limits

The final rebuilt search contains 66 players and 471 distinct family-tagged candidates across six declared construction families. Candidates may occur in multiple families: Allen/Moore and Allen/Kincaid selected the same exact roster, counted once in this shortlist. Six family finalists and the prior recommendation benchmark were scored. The Shakir-family finalist depended on Andrews plus Cook and was not selected for delivery.

20,000 exploratory draws select candidates within each family by frequency of reaching an arbitrary 200-point benchmark, with P95 tiebreaker. Then 150,000 separate draws in each of four scenarios (baseline, reduced correlation, role downside, and high-total-game downside) give 620,000 slate draws in this final run. This is not exhaustive optimization or independent model validation. Earlier constraint experiments were exploratory. The code reproduces the final specification.

Means use the public SPAGS November 1 12:03 PM ET board for all candidates except Chargers DST (prior 4.48 retained; no public second-board observation). Buffalo/Baltimore implied means updated to 28.5/25.0 from total 53.5, BUF -3.5. Other team totals and variance assumptions remain frozen from the earlier model. New TD shares: Moore .30, Kincaid .22, Pickens .25, Braelon receiving .12/rushing .80. These are analyst allocations, not fitted estimates. Team receiving TD shares are <=1; unlisted teammates consume residual production. New role stress: Moore/Kincaid/Pickens .85, Braelon .90, in addition to prior explicit stress choices.

P90 is an uncalibrated model score percentile, not a winning-score forecast. No actual opposing field, lineup duplication model, contest-specific ownership or payout EV was simulated. Historical calibration and actual first-place probabilities remain unavailable. Do not read small score or tail differences as a demonstrated edge. Good chalk is retained; uniqueness is not established by multiplying ownership estimates.

Reproduce: `OPENBLAS_NUM_THREADS=1 python weeks/2026_week_08/high_total_simulation/news_rebuild.py`. Read `news_rebuild_results.json`, `news_rebuild_inputs.json` and `news_five_lineups.json` for the saved results and exact slots. The existing pinned requirements apply.

## Sources

- Latest projections/salaries: https://splashplaypodcast.com/dfs/nfl/players/
- Bills active confirmations: https://www.buffalobills.com/news/buffalo-bills-inactives-vs-ravens-week-8
- Hall out: https://www.newyorkjets.com/news/jets-vs-raiders-nfl-game-inactives-11-1-2026
- Titans inactive list: https://www.tennesseetitans.com/news/game-inactives-week-8-titans-at-bengals
- Pickens/Ridley/Moore/Kincaid active report: https://www.fantasypros.com/nfl/news/616952/dj-moore-shoulder-active-week-8.php
- Official league early inactive roundup: https://amp.nfl.com/news/nfl-week-8-inactives-players-ruled-out-sunday-2026-season
- Patriots downgrades: https://www.patriots.com/news/roster-analysis-patriots-downgrade-wr-a-j-brown-rb-treveyon-henderson-to-out-for-week-8-vs-dolphins
- Updated game environment: https://www.cbssports.com/nfl/news/how-to-bet-on-2026-nfl-week-8-betting-odds-trends-tips-schedule-game-previews-sportsbook-promos-offers/
