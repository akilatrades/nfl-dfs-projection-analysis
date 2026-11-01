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
