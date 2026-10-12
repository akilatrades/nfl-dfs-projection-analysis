# Week 5 post-slate review — October 11, 2026

**Scope:** DraftKings Classic Sunday main slate. I entered a $5 single-entry field of approximately 23,000 and a $3 single-entry field of approximately 7,000. This is my **post-slate player-level review**, not a retroactive lineup optimization. I preserved the original selection and [11 a.m. scoring-model snapshot](../sunday_2026-10-11/final_audit_2026-10-11/README.md) before scoring the results.

**Limit:** I can reconstruct fantasy points from the published box scores, but I have **not yet recorded my actual DraftKings contest placements, official DK app scores, cash thresholds, ownership or payouts**. No claim that either entry cashed can be made yet. Minor stat corrections could change the calculated total.

## Result

| Entered contest | Box-score calculated DK | Final pregame Poisson-MC mean | Actual minus model | Previous blended player-input mean |
|---|---:|---:|---:|---:|
| $5 / ~23K | **153.86** | 123.20 | **+30.66** | 124.22 |
| $3 / ~7K | **120.14** | 126.44 | **−6.30** | 127.63 |

Reproducible [scoring source](score_week5.py), [individual score/error audit](entered_player_results.csv) and [lineup-level comparison](lineup_summary.csv). The earlier 180K-draw simulation put 154.19 at the $5 lineup's modeled 90th percentile and 158.10 at the $3 lineup's 90th percentile. The observed $5 score was close to that *uncalibrated* upper-tail threshold; the $3 score was below its mean. This is **one slate**, not evidence that the simulator's percentiles are statistically calibrated.

### $5 lineup — Love/Watson

| Slot | Player | Before-game blended mean | Calculated DK | Difference |
|---|---|---:|---:|---:|
| QB | Jordan Love | 18.05 | **28.28** | +10.23 |
| RB | Chase Brown | 16.76 | 9.00 | −7.76 |
| RB | D'Andre Swift | 16.19 | 17.30 | +1.11 |
| WR | Michael Wilson | 15.69 | 7.28 | −8.41 |
| WR | Christian Watson | 15.04 | **35.30** | +20.26 |
| WR | Jameson Williams | 12.14 | 18.70 | +6.56 |
| TE | Hunter Henry | 8.76 | 13.40 | +4.64 |
| FLEX | Trey McBride | 16.15 | 21.60 | +5.45 |
| DST | Chargers | 5.44 | 3.00 | −2.44 |
| **Total** | | **124.22** | **153.86** | **+29.64** |

**What worked:** Love (367 passing yards, two TD, a successful passing two-point conversion) and Watson (six catches, 143 yards, two TD) combined for 63.58 DK points, with the passing-yard and receiving-yard bonuses applied. The alternative-game quarterback stack we selected **was not a forced contrarian play**: it had genuine standalone passing upside. Henry also caught a touchdown, Jameson caught two, and McBride caught nine passes and scored. The four receivers/TEs whose receiving touchdowns mattered here were Watson, Jameson, Henry and McBride.

**What hurt:** Chase Brown finished with 13 carries for 39 yards and three catches for 21 yards, despite Cincinnati scoring 31. His team had four **passing** touchdowns, demonstrating that a productive offense does not guarantee fantasy opportunity for its RB. Michael Wilson caught four of seven targets for just 30 yards, plus threw a seven-yard pass: **7.28 DK**. The Marvin Harrison Jr. absence did not translate into a guaranteed Wilson ceiling. Arizona's **Teagan Quitoriano** had two TD catches; McBride took the other. The receiving-touchdown distribution defeated our aggressive Wilson volume/TD case even though the overall game was high scoring.

### $3 lineup — Goff/LaPorta/St. Brown

| Slot | Player | Before-game blended mean | Calculated DK | Difference |
|---|---|---:|---:|---:|
| QB | Jared Goff | 19.52 | **28.94** | +9.42 |
| RB | Chase Brown | 16.76 | 9.00 | −7.76 |
| RB | Aaron Jones Sr. | 15.60 | **22.70** | +7.10 |
| WR | Amon-Ra St. Brown | 18.17 | 12.90 | −5.27 |
| WR | Luther Burden III | 14.70 | 8.90 | −5.80 |
| WR | Tre Tucker | 11.10 | 7.50 | −3.60 |
| TE | Sam LaPorta | 12.27 | **19.80** | +7.53 |
| FLEX | George Kittle | 14.06 | 7.40 | −6.66 |
| DST | Chargers | 5.44 | 3.00 | −2.44 |
| **Total** | | **127.63** | **120.14** | **−7.49** |

**What worked:** Goff produced 271 passing yards, three passing TD and a one-yard rushing TD. LaPorta recorded five receptions for 88 yards and a TD. Aaron Jones rushed 25 times for 113 yards and scored once, adding three short catches; the box score also records a **lost fumble**. These were credible salary/role choices.

**What hurt:** The **three-man Goff stack was the right offensive environment but not the best TD allocation**. St. Brown had an impressive **11 targets** (six catches for 69 yards), but no TD, and the three passing TDs went to LaPorta (one) and Jameson Williams (two). Jameson was selected in the **$5** lineup, so my two-entry portfolio benefited from his production, but the **$3** entry did not. Burden had four catches for 47 yards and two rushing yards; Tucker had four catches for 41 yards and **−6 rushing yards**; Kittle caught five balls for only 24 yards. None produced the second ceiling score needed for a high-field result. The same cheap Chargers defense returned three points.

**Shared failure:** Brown and Chargers DST were in both lineups. Brown scored only 9.00 against an archived 16.76 prior; Chargers DST scored 3.00 against 5.44. Low overall roster overlap did not fully diversify these common low-output positions.

## Football thesis versus what actually happened

- **DET–ARI was not a bad target game.** The 45–21 final = 66 total points, well above the 54.5 pregame research total. Goff passed for three TD; Arizona's Brissett passed for three. The game-level simulation correctly allowed high scoring, but our *player-level TD and target allocation* was unreliable.
- **Our Love–Watson pivot was successful.** Green Bay won 31–7: a 38-point game that came in below our ~45.5 pregame total, yet Watson alone scored 35.3. A **lower total does not preclude one stack capturing a high share of passing events**.
- **The high-chalk Gibbs fade was expensive in hindsight.** Gibbs rushed for 151 yards, scored twice and added five catches for 56 yards: **approximately 40.70 DK** including the 100-yard rushing bonus. A lower roster salary isn't sufficient reason to fade premium RB chalk. This is an opportunity-cost observation, not proof that Gibbs was the optimal *pregame* roster decision.
- **The unselected Maye ceiling was huge.** Maye had 374 passing yards, four passing TD, 25 rushing yards and a rushing score: **approximately 42.46 DK**. Our alternative QB research considered Maye but ruled out a lineup centered on the injury-driven Doubs opportunity. Not forcing Doubs was sensible; **Doubs himself had only one catch for 16 yards (2.60 DK)**. The error was treating the loss of confidence in Doubs as a reason to shift away from Maye's independent quarterback ceiling rather than assessing other NE pass-catching pairings.
- **Avoiding the risky $3,400 TeSlaa punt helped.** TeSlaa finished without a catch on two targets. This is an example where the Week 3–4 low-floor-punt lesson held up.

## What the model got wrong

The biggest problem was not the score distribution's average. It was **the allocation of high-upside fantasy events within successful offenses**. The old simulation used subjective target shares, TD shares and lognormal surplus points. Its high-scoring team factors didn't fully constrain receiver targets and TDs by route participation, red-zone role or realistic teammate competition.

For Week 6, the modeling priorities are:

1. **Forecast team QB pass attempts, carries, red-zone opportunities and TD expectation first; then allocate player-level shares.** A model that gives Wilson and McBride very high volume must explicitly show the sum of shares and account for other TEs.
2. **Separate target share from touchdown share.** St. Brown's 11 targets support his pregame role, even though he scored zero touchdowns. Jameson's 4 targets produced 2 TD. A single outcome shouldn't become a new permanent TD-rate estimate.
3. **Do not underweight the premium RB ceiling merely for lineup uniqueness.** Model salary cost, ownership and replacement quality jointly; Gibbs produced a slate-breaking score.
4. **Evaluate QB ceiling separately from the chosen stack partner.** Maye was exceptionally productive without Doubs being involved. Consider a QB + reliable receiver/TE pivot rather than rejecting QB because one cheap teammate's targets are uncertain.
5. **Treat the last few value positions as real risk.** Burden, Tucker and Kittle all had legitimate roles but lacked explosive or TD outcomes; cap low-ceiling selections and audit each value play's path to 20+ points.
6. **Use actual contest ownership, ranks, prize tables and payouts to assess GPP strategy.** Without these I cannot assess duplication, ROI or whether 153.86 even cashed in that specific 23K field.

## Next data to append

When I export the two DraftKings contest result screens, I need to add: **contest ID/name, actual score, final rank, entry count, min-cash threshold, winnings, exact ownership by player**, any official stat corrections, and the resulting combined net P/L after $8 in entry fees.

**Scoring notes:** This uses DraftKings full-PPR rules: 0.04 passing points/yard, 0.1 rushing or receiving point/yard, four points per passing TD, six per rushing/receiving TD, one per reception, +3 bonuses for 300-yard passing / 100-yard rushing / 100-yard receiving, +2 for successful two-point conversions, −1 per lost fumble. Wilson's seven passing yards add **0.28**; Love's successful 2-point **passing** conversion adds **2**; Jones's lost fumble deducts **1**. Chargers DST is 1 sack + 1 Denver fumble recovery (+2) and **0 points from 23 points allowed** = 3. The actual scores remain calculated, not copied from DraftKings contest records.

## Sources

- [DraftKings NFL Classic scoring](https://dknetwork.draftkings.com/2025/08/27/nfl-dfs-beginners-guide-draftkings/)
- [Detroit–Arizona complete player scoring](https://www.statmuse.com/nfl/game/10-11-2026-ari-vs-det-19139)
- [Green Bay–Chicago final stats and two-point conversion](https://www.footballdb.com/games/boxscore/chicago-bears-vs-green-bay-packers-2026101112)
- [Las Vegas–New England game log](https://www.statmuse.com/nfl/game/10-11-2026-lv-at-ne-19132)
- [Cincinnati–Miami Chase Brown workload](https://www.statmuse.com/nfl/ask/chase-brown-receiving-stats-this-season)
- [Minnesota–New Orleans box score](https://www.neworleanssaints.com/game-day/2026/reg-week5/vikings-at-saints/box-score)
- [San Francisco–Seattle final stats](https://www.statmuse.com/nfl/game/10-11-2026-sf-at-sea-19140)
- [Denver–Los Angeles Chargers defense and game stats](https://www.statmuse.com/nfl/game/10-11-2026-lac-vs-den-19137)

*Audit state: completed game-stat and decision breakdown; contest placement and payouts pending.*
