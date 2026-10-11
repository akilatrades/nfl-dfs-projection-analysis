# Week 5 — Final Sunday pre-lock audit

**October 11, 2026, approximately 11:00 a.m. Central.**

Both DraftKings Classic single-entry lineups are entered and remain fixed: [$5 / ~23,000 entries](../monte_carlo_2026-10-11/recommendation_prelock_v2.csv) and [$3 / ~7,000 entries](../contest_3usd_7k_2026-10-11/selected_prelock.csv). I ran one more pre-lock analysis using the official early inactive list, published market totals, Elo forecasts, team EPA/play and a new touchdown-event Monte Carlo. I found **no new confirmed inactive among the early-game players in either lineup**. The late-window inactives were not yet out when this report was made.

**Decision:** Keep both entries unchanged. Do not mistake this decision for a claim of positive expected payout; the field and prize data are unavailable.

## 1. Official inactive audit

Source: [NFL's October 11 Week 5 inactive tracker](https://www.nfl.com/news/nfl-week-5-inactives-players-ruled-out-sunday-2026-season).

| Contest exposure | Checked against official early inactive list | Finding |
|---|---|---|
| $5: Jordan Love, Christian Watson | GB–CHI | Neither is listed inactive |
| $5: D'Andre Swift | GB–CHI | Not listed inactive; Chicago RB Kyle Monangai **is inactive** |
| Both: Chase Brown | CIN–MIA | Not listed inactive; Ja'Marr Chase and Tee Higgins are playing, so no missing-CIN-WR workload assumption |
| $5: Hunter Henry | LV–NE | Not listed inactive |
| $3: Aaron Jones Sr. | MIN–NO | Not listed inactive; WR Jordan Addison inactive |
| $3: Luther Burden III | GB–CHI | Not listed inactive; Monangai inactive, Caleb Williams inactive |
| $3: Tre Tucker | LV–NE | Not listed inactive; four Patriots corners inactive, but target share and touchdowns are not guaranteed |
| Both: Chargers DST | DEN–LAC late game | **Official late inactives still pending** |
| $5: Michael Wilson, Jameson Williams, Trey McBride | DET–ARI late game | **Official late inactives still pending** |
| $3: Jared Goff, Amon-Ra St. Brown, Sam LaPorta | DET–ARI late game | **Official late inactives still pending** |
| $3: George Kittle | SF–SEA late game | **Official late inactives still pending** |

Late game reports generally become official ~90 minutes before kickoff: about **1:35 p.m. Central** for 4:05 p.m. ET, and **1:55 p.m. Central** for 4:25 p.m. ET. The prior report naming Marvin Harrison Jr. inactive supports extra opportunity for Arizona pass catchers, but I do not assume all his targets go to one player.

## 2. Elo team-strength check

Source: [public Week 5 NFL Elo walk-forward ledger](https://nflanalytic.com/nfl-predictions.html), locked October 6.

| Relevant winner | Published Elo probability |
|---|---:|
| Detroit over Arizona | 64% |
| Chicago over Green Bay | 54% |
| Cincinnati over Miami | 59% |
| Minnesota over New Orleans | 73% |
| New England over Las Vegas | 76% |
| Denver over Los Angeles Chargers | 63% |

Elo helps me check game-script plausibility. It does **not** mean a favorite's receivers are guaranteed to score, and a team win probability is not a DraftKings roster cash probability. For example, Detroit's 64% is compatible with many outcomes in which Gibbs gets rushing TDs instead of Goff passing TDs.

## 3. Logistic regression — negative result

I independently fitted L2-regularized logistic regression with **pregame Elo home-minus-away gap** from 29 Week 3–4 matchups as the feature and the actual home win as the label. The leave-one-out Brier score was **0.2507**; a simple constant-rate baseline was **0.2426** (lower is better).

This small regression **failed** an out-of-sample benchmark. I did not promote it into the lineup evaluation or fabricate precision by putting its probabilities next to better-supported published Elo forecasts. The model is saved in [score_model.py](score_model.py) so the failure can be reproduced.

## 4. EPA — measure opportunity, not just records

Source: [NFL team EPA/play and success rates, updated October 8](https://gridironandwine.com/nfl/advanced/teams/).

| Team | Offensive EPA/play | Defensive EPA/play | DFS read |
|---|---:|---:|---|
| Detroit | +0.051 | +0.047 | Productive offense, permissive defense: viable high-volume game |
| Arizona | −0.013 | +0.027 | Offense less efficient; weak defensive resistance could help DET passing |
| Green Bay | +0.008 | +0.031 | Neutral-ish offensive efficiency, defense can be attacked |
| Chicago | +0.053 | −0.006 | Stronger aggregate offensive EPA but starter Caleb Williams unavailable |
| Minnesota | −0.072 | −0.090 | League-worst offensive EPA despite strong defense and 4–0 record: a **real caution** for Aaron Jones |
| Las Vegas | −0.056 | −0.024 | Poor offense: Tucker's fantasy path still requires volume despite Patriots CB absences |
| New England | +0.007 | −0.031 | Defense quality may hold Raiders team scoring down |

Defensive EPA/play **positive is worse for the defense**. These are team aggregates, not player EPA, and do not identify who absorbs targets after an injury. I used them as cross-checks instead of automatically adding a second scoring bonus on top of market-implied team totals.

## 5. Bayesian conditioning on inactives

The official inactive list changes the probability of **player availability**, which is a legitimate data update. For each early-game entrant absent from the complete inactive list, I condition the active-player scenario on playing. The earlier DFS estimates already assumed these players were active, so I **do not count that good news twice** by raising projections again.

Monangai's absence supports Swift's opportunity, but a quantified shift from 50% to 70% rushing share cannot be learned from one availability report. My explicit illustrative **Beta share prior** around Swift's share is a scenario assumption, not a validated posterior. Patriots CB absences can support Tucker's matchup, but the offense remains a concern.

## 6. Poisson touchdown model + correlated Monte Carlo

The main incremental work is [score_model.py](score_model.py); seed **20261011**, **180,000** simulated slate paths. Inputs/results are in [summary.json](summary.json) and [scenario_comparison.csv](scenario_comparison.csv).

- Matchup total/spread -> each team's **market-implied points** (e.g., 54.5 with DET −5.5 -> DET ~30, ARI ~24.5; GB–CHI 45.5 with CHI −1.5 -> GB ~22, CHI ~23.5).
- Assume 4.5 points per team from field goals as a modeling baseline; use **Poisson TD count** \(\lambda_{\mathrm{TD}}=\max(0.1,(\mu_\mathrm{team}-4.5)/6.95)\). This is an approximation, not an NFL touchdown-count likelihood fitted on historical drives.
- Draw a shared **Gamma game pace factor** and smaller team-specific variation. Split each team's realized touchdowns into rush/pass with explicit pass-rate assumptions and variance.
- Allocate passing touchdowns across **receivers, TEs and catching RBs without assigning the same touchdown twice**; rushing touchdowns are also conserved across modeled QB/RB assignments.
- Add lognormal non-TD DK points (receiving/rushing yards, catches, bonuses) with common team/game factors and idiosyncratic volatility. Defensive scoring uses a separate bounded variable.
- I anchor individual means to the earlier Week 5 analyst/public projection midpoint; three late additions carry only the single public baseline. I **do not** imply a trained player-specific regression model or calibrated contest outcomes.

### Model outputs (not empirical winning probabilities)

| Statistic | $5 / ~23K | $3 / ~7K |
|---|---:|---:|
| Simulated average | **123.20** | **126.44** |
| Median | 121.36 | 124.54 |
| 90th percentile | 154.19 | 158.10 |
| 95th percentile | 164.67 | 168.71 |
| 99th percentile | 186.24 | 190.75 |
| Fraction of model paths ≥170 | 3.40% | 4.57% |

Those 170-point event frequencies should **not** be interpreted as cash probabilities. There is no simulated opponent field, payout table, joint lineup ownership or duplicate penalty. The new means are also lower than earlier Week 5 scenarios because this generator uses an explicit finite team-TD budget rather than unconstrained fantasy-player upside.

### How the actual game script affects my entries

| Scenario | $5 mean DK | $3 mean DK |
|---|---:|---:|
| All simulated slate paths | 123.20 | 126.44 |
| Detroit throws 3+ TD | 127.86 | **139.89** |
| Detroit throws 0–1 TD | 118.53 | **112.78** |
| Arizona throws 3+ TD | **131.41** | 130.13 |
| Green Bay throws 3+ TD | **137.24** | 127.49 |
| Both Arizona and Detroit throw 3+ TD | 135.17 | **142.22** |

The two lineup totals have modeled correlation **0.323**. The $3 entry has a cleaner big-day path through **Goff–St. Brown–LaPorta**, but also a particularly harsh Goff-passing failure scenario. The $5 entry gains more from Arizona/GB passing success. Shared Chase Brown/Chargers DST exposure introduces additional portfolio correlation.

**Model diagnostics:** The simulated fraction with either lineup ≥170 is 7.43%, and with both ≥170 is 0.54%. Those are *only* uncalibrated score thresholds, not combined tournament win probabilities.

## Final decision

I am **not changing either entered lineup** on this evidence. The official early inactive reports show no disqualifying player news, and the quantitative methods mostly identify **how** each lineup can succeed or fail—not a justified upgrade after entry.

The one remaining operational check is the official **late-game inactive reports**. I will not treat a Friday injury projection, a depth chart or an external lineup model as proof someone is active. Any unexpected late inactive requires a fresh, salary-valid swap decision, not an automatic full-roster rebuild.

### Dated source list

- [NFL official Week 5 inactive tracker](https://www.nfl.com/news/nfl-week-5-inactives-players-ruled-out-sunday-2026-season)
- [Week 5 Elo predictions and Week 3–4 result history](https://nflanalytic.com/nfl-predictions.html)
- [Team offensive/defensive EPA/play](https://gridironandwine.com/nfl/advanced/teams/)
- [Detroit–Arizona Week 5 lines](https://dknetwork.draftkings.com/2026/10/11/detroit-lions-vs-arizona-cardinals-prediction-pick-for-nfl-week-5-on-sunday-10-11-26/)
- [Chicago–Green Bay Week 5 market](https://www.acmepackingcompany.com/green-bay-packers-game-information/87873/packers-vs-bears-week-5-game-time-tv-channel-odds-more)
- [Cincinnati–Miami Week 5 market](https://www.thephinsider.com/miami-dolphins-schedule/123644/bengals-vs-dolphins-2026-week-5-online-stream-kickoff-time-odds-injuries-more)
- [Minnesota–New Orleans Week 5 market](https://www.dailynorseman.com/minnesota-vikings-odds/100033/vikings-vs-saints-odds-week-5-opening-lines-point-spread-total)
- [Las Vegas–New England week-of-game market](https://edraft.com/nfl/games/2026-week-5-lv-at-ne?scoring=ppr)

*Freeze status:* Two entries, $8 of contest fees, no authorized lineup modifications. The code and archived reports preserve what was known and assumed before kickoff.
