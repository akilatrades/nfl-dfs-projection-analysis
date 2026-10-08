# Tampa Bay at Dallas — $5 single entry, approximately 19,000 entries

Research decision dated October 8, 2026, before the scheduled 7:15 p.m. Central kickoff. The user supplied the fee, entry limit and approximate field size. DraftKings Showdown is assumed from the ongoing discussion; exact contest ID, payouts and official salary export are unavailable. No entry has been submitted.

## Current selection

| Slot | Player | Salary charged |
|---|---|---:|
| Captain | CeeDee Lamb | $17,700 |
| FLEX | Dak Prescott | $10,400 |
| FLEX | Jalon Daniels | $8,600 |
| FLEX | Cade Otton | $4,400 |
| FLEX | Ryan Flournoy | $3,800 |
| FLEX | Chase McLaughlin | $5,000 |
| **Total** | **$100 remaining** | **$49,900** |

This is an analyst-selected tournament build, not the result of a calibrated 19,000-entry simulation. Lamb's Captain slot expresses the view that Dallas's passing production can concentrate in him. Dak captures that passing production; Flournoy provides a second Dallas receiver at a lower salary. Daniels and Otton provide a Tampa Bay passing pair. McLaughlin fits the salary and benefits when Tampa Bay sustains drives but settles for field goals. Those field goals compete with offensive touchdowns; the pairing is not uniformly positively correlated.

The lineup has three players from each team. Lamb's receptions, yardage bonus and touchdowns offer a plausible path to outperforming Dak in full PPR scoring. Both quarterbacks remain included. We do not force a very cheap player with almost no established offensive role to pay for a more expensive sixth player.

There is no verified ownership dataset here. We cannot establish that this lineup is unusual or estimate its number of duplicates. Leaving $100 unused is not evidence of uniqueness. The larger field motivates an upside-oriented Captain decision; it does not numerically change any forecast in this review.

## Captain comparison and the close alternative

Six hand-constructed legal candidates were compared, not every possible roster. Salary and mean-point arithmetic use a dated [Footballguys public Showdown table](https://www.footballguys.com/dfs/showdown/optimizer/week-5-buccaneers-at-cowboys-draftkings). These external projections are explicitly separate from the repository's manual Sunday model. We have not independently validated the provider's forecasts.

| Captain | Salary | Sum of external means, including Captain multiplier |
|---|---:|---:|
| **Lamb — selected** | **$49,900** | **98.08** |
| Dak | $49,600 | 99.05 |
| Daniels | $48,900 | 93.96 |
| Ferguson | $48,600 | 90.78 |
| Pickens | $49,500 | 92.07 |
| Javonte Williams | $48,800 | 95.79 |

Full candidate membership and the exact numeric snapshot are in `research_snapshot.json`. The displayed totals are expected-point sums, not floors, ceilings, win probabilities or payout estimates. We did not add individual ceiling estimates or import third-party simulated winning percentages.

**First alternative:** Dak Captain; Lamb, Daniels, Otton, Flournoy and Brandon Aubrey FLEX, $49,600. This has the highest external mean among the six constructed candidates. The selection gives up about 0.97 expected points in that snapshot to prefer Lamb's scoring concentration. It is an editorial risk preference, not a mathematically demonstrated advantage.

The two builds share the same five offensive players. Their actual score difference, selected minus alternative, is `0.5 × (Lamb points − Dak points) + McLaughlin points − Aubrey points`. Holding the kicker expectations at the saved values, Lamb needs to exceed Dak by more than 4.64 points for the selected build to lead. Actual kicker scores can change that comparison substantially. If Dallas passing touchdowns spread among several receivers, the Dak Captain alternative becomes more attractive.

## Evidence and uncertainties

- [Tampa Bay's official inactives](https://www.buccaneers.com/news/bucs-cowboys-inactives-rueben-bain-jr-ko-kieft-return-action) identify Baker Mayfield as out and Jalon Daniels as the starter. The selected players are not on the published inactive lists. That report also lists Winfield, Morrison and Dennis out for Tampa Bay and Durant and Porter out for Dallas. This is availability evidence, not an automatic fantasy-point adjustment.
- [DraftKings Network's matchup research](https://dknetwork.draftkings.com/2026/10/07/buccaneers-vs-cowboys-draftkings-showdown-picks/) reports Lamb's 46 targets through four games, including 21 in Week 4, and a Dallas passing-oriented matchup case. One exceptional game must not be treated as his expected weekly workload. Its published market snapshot was Dallas -8.5 and total 47.5, not a verified closing line.
- [Dallas's official staff preview](https://www.dallascowboys.com/news/gut-feeling-staff-predictions-for-cowboys-buccaneers) discusses Flournoy as a secondary receiving option. This is editorial support, not a verified route-share estimate. His target volume is the primary weak point: halving his saved external mean reduces the selected total from 98.075 to 93.34. We do not know the probability of that outcome.
- [Tampa Bay's final injury article](https://www.buccaneers.com/news/buccaneers-cowboys-injury-report-oct-7-week-5) records McLaughlin returning to full participation after a groin/hip issue. Its bullet contains a weekday-label inconsistency; the [October 7 report from Bucs Nation](https://www.bucsnation.com/tampa-bay-buccaneers-injuries/68982/buccaneers-cowboys-final-injury-report-nfl-thursday-night-football) identifies Wednesday, and he is absent from the official inactive list. Residual kicking limitations are not modeled. Any adverse warmup report favors the saved Dak/Aubrey alternative before lock.
- [Bowles's backfield comments](https://www.buccaneers.com/news/todd-bowles-bucs-need-to-split-backfield-reps-three-ways) describe possible work for Irving, Gainwell and Tucker. Tucker played only three offensive snaps in Week 4. That makes him a fragile punt for this single lineup. It does not make him incapable of scoring.
- Salary cross-checks are available in [PropSims' older October 6 table](https://propsims.com/articles/fantasy/2026-week-5-tb-dal-showdown/) for skill players and [RotoWire's Thursday preview](https://www.rotowire.com/football/article/nfl-dfs-week-5-top-picks-lineup-strategy-for-cowboys-vs-bucs-139773) for Aubrey. Some articles list inconsistent Pickens salaries; the saved comparison uses $9,400 from Footballguys and PropSims. The contest's own player list is authoritative.

## Entry checks and arithmetic

The six candidates were checked for six unique players, one Captain, five FLEX, both teams represented and salary at or below $50,000 using Captain salary and points at 1.5 times FLEX. See [DraftKings' Showdown explanation](https://dknetwork.draftkings.com/2020/06/17/advanced-nfl-dfs-showdown-strategy/).

Before entering, match these prices and eligibility to the actual contest and check any late news. A salary mismatch requires rebuilding, not blindly substituting one player. All players are in the same game; do not expect post-kickoff roster flexibility. The candidate scores can be reproduced from the JSON by multiplying the first player's FLEX salary and mean by 1.5, then adding the other five. The Flournoy sensitivity halves only his mean, keeping the roster and other estimates fixed. No game simulation, weather adjustment, payout optimization or exhaustive search is claimed.
