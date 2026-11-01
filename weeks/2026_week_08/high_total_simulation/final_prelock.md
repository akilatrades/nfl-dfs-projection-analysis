> **Latest rebuilt shortlist:** See [news_shortlist.md](news_shortlist.md) for five choices after confirmed actives, including Moore/Kincaid/Pickens as eligible candidates and the prior Allen/Moore roster as a benchmark. The latest tournament preference is Allen–Moore–Kincaid / Flowers; the prior balanced Allen/Moore roster remains option 2. Earlier research below is preserved.

# Current preference after direct Moore comparison

**DJ Moore ($5,700) replaces Khalil Shakir; Broncos DST ($2,300) replaces Browns DST. Total $49,800; public-board projection 137.9.** Full roster: Josh Allen, Braelon Allen, Rhamondre Stevenson, Zay Flowers, Drake London, DJ Moore, Brenton Strange, Wan'Dale Robinson (FLEX), Broncos DST.

The earlier six-way final comparison held Shakir fixed and therefore did not establish him as the best Bills stack partner. That constraint was too restrictive after Moore was confirmed active. Moore has a stronger recent healthy-game target concentration, based on only two full games, and still carries shoulder/workload uncertainty. Shakir retains a credible slot role. The change is a modest preference, not a proven contest edge.

A new direct comparison used 100,000 draws in three scenarios (300,000 slate draws). Baseline P90: Moore/Denver 175.9 versus Shakir/Cleveland 174.7. Role-downside means: 128.1 versus 127.5; both Bills receivers receive a 15% stress multiplier. Moore's receiving-TD share of .30 is an analyst assumption; other Bills modeled shares were retained, with residual allocation for unlisted teammates. No actual field, duplicate probability or calibrated win odds. See [moore_check.py](moore_check.py) and [moore_check.json](moore_check.json). The original recommendation and comparison below are preserved for audit.

Sources: [confirmed Bills actives](https://www.buffalobills.com/news/buffalo-bills-inactives-vs-ravens-week-8), [role comparison](https://www.fantasypros.com/2026/10/the-primer-week-8-edition-2026-fantasy-football/), [12:03 ET projections](https://splashplaypodcast.com/dfs/nfl/players/).

---

# Final Allen construction — November 1, 2026

Final review requested at 11:30 AM Central for the $27 NFL $60K Blind Side single-entry contest (maximum 2,591). This is one alternative entry; it supersedes my earlier preference among the five options. The original Allen/Puka roster remains recorded and is playable. No entry was submitted by this workflow.

## Final preference

| Slot | Player | Salary | SPAGS DK projection |
|---|---|---:|---:|
| QB | Josh Allen | 7700 | 23.0 |
| RB | Braelon Allen | 6100 | 19.4 |
| RB | Rhamondre Stevenson | 5600 | 18.9 |
| WR | Zay Flowers | 7200 | 18.8 |
| WR | Drake London | 7000 | 16.8 |
| WR | Khalil Shakir | 5600 | 10.8 |
| TE | Brenton Strange | 4000 | 11.5 |
| FLEX | Wan'Dale Robinson | 4200 | 11.8 |
| DST | Browns | 2600 | 6.1 |
| Total | | 50000 | 137.1 |

Breece Hall is officially inactive, supporting Braelon Allen's workload at $6,100. Buffalo's D.J. Moore and Dalton Kincaid are active: Shakir receives no artificial injury-vacancy boost. Calvin Ridley is absent from Tennessee's inactive list and is treated as available; Wan'Dale's case does not assume Ridley is out. Patriots A.J. Brown and TreVeyon Henderson are out, supporting Stevenson. London is absent from Atlanta's inactive list; Strange is absent from Jacksonville's inactive list. Late-game Patriots inactives are not yet posted in the retrieved league roundup; Stevenson has no injury designation.

Changes versus the original $50,000 Allen option: Coleman to Braelon (+1800), Puka to London (-1600), Henry to Strange (-300), Malik to Wan'Dale (-200), Denver DST to Cleveland (+300). Net zero salary change. Losing Puka's individual ceiling is a real cost; the construction improves the running-back role and reduces reliance on Miami passing production. Wan'Dale remains a cheap, uncertain ceiling piece. Shakir competes with active teammates. Tampa rain/thunderstorms affect London's environment. Cleveland is selected for price and pressure opportunity; defensive TDs are not assumed. Only Stevenson plays late, and he occupies RB, so late-swap options are limited.

## Actual comparison

Six explicit Allen-family alternatives, 100,000 draws in each of four scenarios: 400,000 slate draws. Public SPAGS projections updated November 1 at 12:03 PM ET replace the earlier means for players used in these comparisons. Simulation is the existing simplified TD-constrained score proxy. Team totals, variance assumptions and other TD shares remain frozen from the earlier run. This is an exploratory comparison, not a calibrated contest field simulation.

| Roster | Salary | Projection | Baseline simulated P90 | Assumed role-downside mean |
|---|---:|---:|---:|---:|
| Original Allen/Puka | 50000 | 133.5 | 172.2 | 122.5 |
| Final Allen/London | 50000 | 137.1 | 174.6 | 127.6 |
| Parker/Henry alternative | 49800 | 135.8 | 173.3 | 126.1 |
| London/Douglas alternative | 49900 | 135.6 | 173.2 | 126.9 |
| Three RBs with Bucky/Godwin | 50000 | 137.2 | 174.3 | 130.1 |
| Three RBs with Brown/Godwin | 49900 | 137.0 | 173.5 | 129.9 |

The final choice has slightly better modeled upper-tail output while keeping one Tampa receiver rather than competing Bucky/Godwin pieces. The three-RB variants are better under the specified role stress; the final roster does not dominate every scenario. Differences this small do not demonstrate a contest-winning edge. P90 is an uncalibrated model percentile, not the predicted winning score. No duplication, payout EV or actual opponent-field win probability is estimated.

Braelon's receiving TD share (.12), rushing TD share (.80) and role-downside multiplier (.90) are new analyst assumptions, not fitted workload estimates. Other stress multipliers remain explicit assumptions too. Changing these can change the comparison. The salary, position counts, nine distinct players and absence of offensive/DST opponent conflicts passed program checks. Salaries match public boards; an official export for this contest was not available.

Code: [final_check.py](final_check.py). Frozen results and assumptions: [final_check.json](final_check.json). Run with the pinned dependencies already in this folder: `OPENBLAS_NUM_THREADS=1 python weeks/2026_week_08/high_total_simulation/final_check.py`.

## Sources

- Latest public SPAGS means/salaries, 12:03 PM ET: https://splashplaypodcast.com/dfs/nfl/players/
- Jets official inactive list (Hall out): https://www.newyorkjets.com/news/jets-vs-raiders-nfl-game-inactives-11-1-2026
- Bills official inactive list (Moore and Kincaid active): https://www.buffalobills.com/news/buffalo-bills-inactives-vs-ravens-week-8
- Official league roundup including Titans/Jaguars/Browns: https://amp.nfl.com/news/nfl-week-8-inactives-players-ruled-out-sunday-2026-season
- Patriots official Saturday downgrades: https://www.patriots.com/news/roster-analysis-patriots-downgrade-wr-a-j-brown-rb-treveyon-henderson-to-out-for-week-8-vs-dolphins
- Buccaneers/Falcons official inactive list: https://www.buccaneers.com/news/falcons-bucs-inactives-antoine-winfield-jr-makes-his-return
- Pressure/ownership/weather context (morning forecasts, not observed field): https://covertheslate.com/nfl-week-8-draftkings-main-slate-2026/
