> **Final prelock review:** The [final Allen construction](final_prelock.md) is the latest recommendation following the 11:30 AM Central review request and confirmed early inactives. The five-option comparison below remains the earlier research record.

# Week 8 high-total lineup comparison — November 1, 2026

This is the current five-option shortlist for my **$27 NFL $60K Blind Side single-entry contest, maximum 2,591 entrants**. It supersedes the earlier Dak and Burrow recommendations; those remain preserved as dated process records. These are five alternatives for **one entry**, not five entries in the same single-entry contest. No lineup was submitted by this research workflow.

## Decision

My first preference is **option 1, Dak–Lamb with McBride and Bourne on Arizona**, keeping Stevenson, Irving and Tuten. It combines the highest-total indoor environment with a premium receiving role at TE. The receiving discount is real risk: Bourne and Malik are the weak WR spots, and the Chargers are a budget defense. I am not calling it a proven higher-EV roster.

Dallas–Arizona is listed around 54.5 with Dallas -7; Baltimore–Buffalo around 53.5–54.5 with Buffalo favored by roughly a field goal. Those are the primary game targets. Tennessee–Cincinnati is around 46.5 with Cincinnati -12.5; I do not treat it as a projected shootout. Pollard remained in the pool but was not required and did not make these finalists.

The exact slot-by-slot table is in [lineup_table.md](lineup_table.md), and the machine-readable five rosters, salary totals and scenario statistics are in [five_lineups.json](five_lineups.json).

| Choice | Primary construction | Salary | Baseline mean | Simulated P90 | Independent-forecast mean |
|---|---|---:|---:|---:|---:|
| 1 — first preference | Dak–Lamb / McBride–Bourne | $50,000 | 137.7 | 179 | 137.8 |
| 2 | Brissett–McBride–Michael Wilson / Lamb | $49,900 | 134.4 | 177 | 133.1 |
| 3 | Dak–Lamb–Javonte | $50,000 | 138.2 | 179 | 134.0 |
| 4 | Allen–Shakir / Flowers | $50,000 | 132.1 | 171 | 130.8 |
| 5 | Lamar–Flowers / Shakir | $49,900 | 131.4 | 170 | 130.1 |

P90 is the score exceeded in approximately one tenth of this model's draws, **not a prediction of the contest's winning score**. The percentiles are uncalibrated. Differences of a point or two should not be treated as reliable rank separation. Mean and percentile rounding are intentional.

## What ran

- Expanded the salary-confirmed curated pool from 33 to **66 players**, excluding the Thursday, Sunday-night and Monday-night games from the candidate pool. The original frozen pool and additions contain only the main-slate players used here. No questionable Pickens, D.J. Moore or Kincaid was included as a candidate. Their potential production remains in unlisted-teammate TD shares, rather than automatically reassigned to selected players.
- Generated **574 distinct family-tagged candidates** across six high-total construction families. These are not 582 exhaustive full-slate optima. Some rosters can occur in more than one family; the six finalists and five deliverable rosters were checked separately for duplicate sets after the single-stack restrictions were added.
- Used **20,000 exploratory draws** to select a candidate within each family by frequency of reaching 200 points, with P95 as a tiebreaker. The 200-point level is a chosen upper-tail comparison benchmark, not an estimated winning threshold.
- Ran **150,000 fresh holdout draws per scenario**, five scenarios: baseline, reduced common correlation, role downside, high-total games underperform, and a second projection board. Total for the final reproducible run: **770,000 slate draws**. Draw count reduces sampling noise; it does not validate the assumptions.
- Compared six family finalists and kept five distinct options. The sixth Lamar/Flowers/Andrews/Shakir construction was not preferred: it gave lower baseline output and depended on Andrews' weak recent role. Its results remain in [results.json](results.json).
- Verified salary, distinct players, positional eligibility, no DST against a rostered offensive opponent, TD-share mass, approximately centered player means and positive QB/receiver score correlation. Pinning the RNG and dependency versions makes the run repeatable.

## Constraints and construction controls

Nine distinct players; exactly one QB, one TE and one DST; 2–3 RB and 3–4 WR; salary $49,200–$50,000; one declared primary high-total core; at most three offensive players per team; no opposing DST conflict; at most two sub-$5k WRs; at most one of the designated uncertain-role punts (Coleman, Wan'Dale, Bourne, Flournoy, Lane). Candidates also retain at least 95.5% of the best additive forecast in their construction family.

The single-stack Lamar and Allen families explicitly exclude Andrews, preventing the accidental duplication of the separate Baltimore double-stack family. A double stack is a candidate, not a universal requirement. No individual player was forced into all five. Stevenson survives every option because of salary, forecast and Henderson's confirmed absence, not because the program demanded it.

## How the simulation works

This is a **touchdown-constrained score proxy**, not a play-by-play simulator or a historical backtest.

1. Each game gets a shared mean-one lognormal scoring factor; each team gets an additional scoring factor. Team TD expectations start from implied points after subtracting an assumed six points for field goals/other scoring, then dividing by seven.
2. Draw team TD counts; split them into passing/rushing scores with a random team passing fraction. The fractions and all TD shares are explicit analyst inputs, not fitted estimates.
3. Allocate each team TD once among modeled players and an unlisted-teammates residual. A receiver's receiving TD is part of the QB's passing-TD total. Rushing TDs compete with passing TDs; receiving teammates compete for a finite set of team scores.
4. Add positive continuous non-TD score components using mean-centered gamma distributions and shared game/team production factors. The components are centered to the saved external forecasts after subtracting expected TD points. QB/receiver yardage and target totals are **not fully conserved**; this remains a simplified score model. Bonuses and turnovers are absorbed into the external non-TD forecast rather than simulated as exact stat events.
5. DST uses an approximate score distribution with opponent-scoring shocks and occasional touchdown events, floored at -4. It does not model each sack, return or points-allowed bracket separately.

The code and frozen TD shares are in [run.py](run.py) and [inputs.json](inputs.json). Baseline player means are kept separate from the analyst distribution assumptions. Neither the variance assumptions nor simulated tail probabilities have been historically calibrated.

## Sensitivity results

| Choice | Baseline simulated mean | Role-downside mean | P90 with reduced correlation |
|---|---:|---:|---:|
| 1 | 137.7 | 132.2 | 173 |
| 2 | 134.4 | 129.2 | 170 |
| 3 | 138.3 | 129.2 | 173 |
| 4 | 132.1 | 121.5 | 165 |
| 5 | 131.4 | 124.4 | 164 |

Role downside multiplies Stevenson by .90; Shakir, Henry, Strange, Malik and Douglas by .85; Wan'Dale by .80; Andrews/Bourne/Flournoy/Lane by .75; Coleman by .65. These are **analyst stress choices**, not confidence intervals or probabilities of workload outcomes. Tuten's backfield split and every unstressed player's role remain uncertain too.

The reduced-correlation scenario reduces the common game lognormal sigma from .20 to .08 and team production sigma from .18 to .08. In the cold-game scenario, Dallas, Arizona, Baltimore and Buffalo TD rates fall 20% and their non-TD components 10%. The alternate-projection scenario uses the public SPAGS November 1 08:36 ET board where available; missing observations retain primary forecasts. The Chargers DST has no SPAGS observation on the public list and remains at 4.48. All offensive players in the selected five have a SPAGS cross-check.

For baseline Denver and Pittsburgh DST I used the lower of FSC and FTN's public forecasts, an explicit conservative rule. This changes Denver to 5.3 and Pittsburgh to 8.1 instead of letting one projection source dictate the cheap-defense choice.

## Individual roster theses and failure cases

**1 — Dak / McBride:** Dallas passing points land with Lamb, while Arizona's McBride and Bourne keep producing. Stevenson/Irving/Tuten provide opportunity without requiring another expensive passing stack. Bourne has a reported 15.3% target share since Week 5; he is a studied discount, not an assumed breakout. Still, his recent production is thin, Malik is uncertain and the Chargers' defense faces a strong Rams offense with defensive injuries. Those are substantial compromises at a full $50k salary.

**2 — Brissett / McBride / Wilson:** Arizona throws heavily and McBride/Wilson capture the receiving production; Lamb answers. This is an intentional four-player game concentration with a lower-owned QB, not four independent projections. Wan'Dale and Douglas are the weak supporting WR spots. Arizona offensive-line injuries and Miami weather remain risks. The salary does not validate an inflated assumption that every receiver inherits missing targets.

**3 — Dallas offense:** Dak/Lamb passing production and Javonte rushing production both contribute to a strong Dallas scoring day; Cincinnati's Chase is a standalone ceiling play. This is not a double-receiver passing stack. Pass/rush TD competition is modeled explicitly. Coleman has a recent leading snap share and Harvey is OUT, but Dobbins still competes for carries and goal-line work. The role-downside result is materially worse than option 1.

**4 — Buffalo lead:** Allen's legs and passing, Shakir receiving, and Flowers responding provide the main correlated scenario; Puka adds another premium receiving outcome. Coleman/Malik are price-sensitive role bets and Henry/Stevenson load some production on New England. This is the most exposed to the tested weak-role assumptions; choose it for the Allen/Puka scoring scenario, not because its mean beats Dallas.

**5 — Baltimore lead:** Lamar's rushing/passing and Flowers receiving succeed while Shakir answers. Chase is a standalone premium WR; Brown keeps strong Cincinnati backfield chalk without paying for Burrow. Wan'Dale is a cheap fourth WR, not a compulsory opposing player. The baseline forecast is lower than the Dallas options. Lamar's first game back after an ankle injury and the supporting cheap receiving roles are risks.

## Ownership and contest fit

These are alternatives for a 2,591-entry single-entry field. I keep good chalk such as Stevenson, Lamb, Brown or Irving, but the precise collection differs by scoring scenario. Published main-slate QB ownership is roughly Dak 15–19%, Brissett about 8%, Lamar 5–8%, Allen 8–10%; these are cross-provider/time snapshots, not this contest's observed ownership.

I did **not** simulate the actual 2,590 opposing entries, calibrate a joint field-lineup distribution, estimate duplication or calculate payout EV. No lineup is assigned a real first-place probability. Summing ownership or multiplying individual ownership percentages is not a duplicate-lineup model. The within-six best-score statistic in the raw result file is only a comparison among six modeled lineups; it is not contest win probability and is not used to claim an edge.

## News, eligibility and late swap

- Early games lock at noon Central on November 1. Final active lists are a pre-entry requirement; the research uses Friday/Saturday official reports.
- Henderson and A.J. Brown are OUT; Stevenson/Douglas/Henry are not automatically assigned every missing opportunity.
- Harvey is OUT/IR, supporting consideration of Coleman; his workload is still a split.
- Lamar practiced fully and has no designation but returns from an ankle injury and has acknowledged remaining discomfort.
- McBride/Brissett/Michael Wilson/Bourne do not carry final game designations in Arizona's report. Arizona has offensive-line injury concerns.
- The Chargers are missing Derwin James and Deane Leonard. Their low salary funds offense; it does not make their matchup strong.
- Miami/Tampa/Jacksonville rain and wind remain relevant to the supporting pieces. Buffalo's forecast is comparatively benign; Dallas is indoors.
- Roster names, positions and salaries match public Week 8 boards, not an official export for this exact contest ID. No official player IDs are invented and these are not upload CSVs.
- Use the slot assignments in the five-roster file. Where there are three RBs, Stevenson occupies FLEX. Option 2 leaves late Douglas at FLEX; option 4 late Malik at FLEX. Option 5 has only one late offensive player, Stevenson at RB, so less late-swap freedom.

## Reproduce

```bash
python -m pip install -r weeks/2026_week_08/high_total_simulation/requirements.txt
OPENBLAS_NUM_THREADS=1 python weeks/2026_week_08/high_total_simulation/run.py
python weeks/2026_week_08/high_total_simulation/package_report.py
```

The final execution manifest records the seed, NumPy version, draw counts, code/input hashes and model checks. Intermediate experiments with weaker constraints are not described as independent validation. The final reported run is the frozen reproducible specification.

## Sources, retrieved November 1, 2026

- Primary published salary/mean board: https://fantasysportscentral.com/football/dfscheat.php
- Independent SPAGS board, 08:36 ET: https://splashplaypodcast.com/dfs/nfl/players/
- Independent DST comparison: https://ftnfantasy.com/nfl/top-nfl-dfs-cash-game-picks-for-week-8-2026
- High-total game context: https://www.fantasylabs.com/articles/nfl-dfs-picks-week-8-main-slate-draftkings-breakdown-2026/
- Brissett ownership: https://www.fantasylabs.com/articles/week-8-nfl-dfs-qb-breakdown-top-cash-game-and-tournament-picks-2026/
- Workload/ownership/weather context: https://covertheslate.com/nfl-week-8-draftkings-main-slate-2026/
- Cardinals report: https://www.azcardinals.com/news/injury-report-week-8-vs-cowboys
- Bills report: https://www.buffalobills.com/news/buffalo-bills-injury-report-vs-ravens-week-8
- Ravens report: https://www.baltimoreravens.com/news/lamar-jackson-ravens-bills-set-to-play-2026
- Patriots report: https://www.patriots.com/news/week-8-injury-report-patriots-at-dolphins-x9227
- Broncos roster update: https://www.denverbroncos.com/news/broncos-promote-s-taylor-rapp-to-active-roster-place-rb-rj-harvey-on-injured-reserve
- Chargers report: https://www.chargers.com/news/chargers-vs-rams-injury-report-mcconkey-full-james-awosika-don-t-practice-wednesday
- Bourne role: https://www.fantasypros.com/nfl/notes/480218/kendrick-bourne-2026-week-8-outlook.php
- Malik role: https://www.fantasypros.com/nfl/notes/480203/malik-washington-2026-week-8-outlook.php
- Shakir role: https://www.fantasypros.com/nfl/notes/480216/khalil-shakir-2026-week-8-outlook.php

After the slate, preserve the selected entry, actual ownership, rank, score, cash line and payout. Compare forecast and assumptions with outcomes without rewriting this pregame decision.
