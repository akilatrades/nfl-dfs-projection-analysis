# Week 5 2026 — $3 / ~7,000-entry single-entry main-slate decision

**Entry update:** I entered this $3 / ~7,000-field Goff stack and the separate $5 / ~23,000-field Love–Watson stack. This analysis was originally written before I submitted the $3 entry, and I have kept those pre-lock assumptions unchanged. Both rosters are saved in my [entry log](../entered_lineups_2026-10-11.md). Exact contest ID and prize payout structure not provided, so the 7,000-entry field size affects our qualitative construction, not a calibrated payout optimization.

## Selection

| Slot | Player | Opponent | Published DK salary |
|---|---|---|---:|
| QB | Jared Goff | ARI | $6,600 |
| RB | Chase Brown | MIA | $6,900 |
| RB | Aaron Jones Sr. | NO | $6,500 |
| WR | Amon-Ra St. Brown | ARI | $7,900 |
| WR | Luther Burden III | GB | $4,900 |
| WR | Tre Tucker | NE | $4,800 |
| TE | Sam LaPorta | ARI | $4,900 |
| FLEX | George Kittle | SEA | $5,200 |
| DST | Chargers DST | DEN | $2,300 |
| **TOTAL** | | | **$50,000** |

[Selected roster CSV](selected_prelock.csv). The lineup is **name/salary checked only** against published main-slate prices; final contest-specific DraftKings player IDs, actual DK contest salary export and player statuses are still unverified. Roster validation: exactly 1 QB / 2 RB / 3 WR / 1 TE / 1 WR-RB-TE FLEX / 1 DST; nine different players; no offensive players against the selected DST; Goff has two Lions pass-catching stack partners. Kittle (late kickoff) is at FLEX.

**Only two shared names** with my $5 lineup (Love / Chase Brown / Swift / Michael Wilson / Christian Watson / Jameson Williams / Hunter Henry / Trey McBride / Chargers DST): Chase Brown and Chargers DST. Do **not** infer lineup-score independence just because player overlap is low: both entries depend on Lions–Cardinals production in different ways.

## Why this beats simply reusing the $5 game script

The $5 entry counts on Love–Watson and the Arizona Wilson–McBride + Detroit Jameson mini-game. This $3 alternative concentrates on **Detroit's passing touchdowns**: Jared Goff plus Amon-Ra St. Brown and Sam LaPorta. Detroit carries a ~30-point implied team total in the slate's highest-total game at ~54.5, so QB+WR+TE is a **plausible fantasy-scoring configuration**, but not guaranteed (Gibbs can take rushing TDs).

Complementary player roles are independently grounded:
- **Aaron Jones $6,500**: since Week 2 averaging ~108 scrimmage yards, Saints allow substantial RB yardage/scoring. [FantasyPros Oct 11](https://www.fantasypros.com/2026/10/nfl-dfs-values-picks-targets-advice-week-5-2026/).
- **Luther Burden $4,900**: six Week 4 targets, 24% seasonal target share, 29% first-read target share and ~2.01 yards per route run. He is *not* merely a low-priced punt. Strongest caveat is the Packers' slot coverage and backup Chicago QB Tyson Bagent. [PrizePicks Oct 11](https://www.prizepicks.com/playbook-article/bears-vs-packers-prediction-spread-nfl-picks-today-sunday-october-11).
- **Tre Tucker $4,800**: 23 targets in four games (including eight in Week 4) and 32.6% of Raiders' air yards against Patriots missing multiple cornerbacks. Tight-end volume and low team WR concentration remain risks. [DraftKings Network Oct 10](https://dknetwork.draftkings.com/2026/10/10/tre-tucker-fantasy-football-start-or-sit-advice-for-week-5/).
- **Chase Brown $6,900**: kept as a one-off due to workload; CIN Chase/Higgins illness/injury uncertainty still awaits official pregame status. No claim of a proven increase in rushing volume from absent receivers.
- **George Kittle $5,200**: stable TE premium independent of Goff; with LaPorta, a second tight end at FLEX adds correlation-independent points but also the usual TE volatility. Two tight ends are allowed and were compared historically in the repo.
- **Chargers DST $2,300**: legal against Denver, no competing DEN offense included. Sharing this defense with the entered lineup is acceptable only as a deliberate strong-cost roster-choice assumption; it creates shared outcome risk.

We **rejected** the mechanically higher initial Goff lineup that had Swift + Odunze + Burden (three Chicago offensive pieces). That repeated the Week 4 problem of stacking unsupported teammate production from the same team. Replacing Swift with Aaron Jones and one Chicago WR with Tre Tucker gives this final lineup just **one** Chicago player.

## Quantitative slate-path screen

[Reproducible zero-dependency Node script](../../../../monte_carlo_week5_7k_2026.js) and [recorded simulation outputs](simulation_comparison.csv) extend the original Week 5 correlated-score surrogate. Three additional $3 candidate variations were checked against the existing Goff and Brissett alternatives and the already entered $5 lineup. The new run used **5 × 80,000 = 400,000 correlated simulated slate paths** in total across alternate mean/scenario regimes with a fixed deterministic seed 20261011.

The simulator is NOT calibrated to actual weekly distributions: lognormal player volatility, latent game/team/pass-volume factors, partial within-team target-share competition and injury shocks are all analyst assumptions. There is **no contest field simulator, opponent ownership joint model, duplicate-lineup estimator, contest payout structure, or first-place probability**. Model probability of 170+ is a hypothetical threshold frequency only.

| Assumption set | Selected $3 lineup mean input | Sim P95 | Model frequency ≥170 |
|---|---:|---:|---:|
| Equal blend of repo subjective and external projection feed | 127.63 | 181.70 | 8.32% |
| Repo manual priors | 132.56 | 189.44 | 10.99% |
| External feed only | 122.70 | 174.16 | 6.04% |
| Burden down to 10 projected points (instead of 14.7) | 122.93 | 174.72 | 6.23% |
| Detroit passing downgraded (Goff 15, ARSB 13, LaPorta 10.5) | 116.16 | 164.46 | 3.76% |

For comparison, the **Brissett + Wilson + McBride** prior alternative had blended P95 ~178.67 and model frequency ≥170 of 7.31%; the previous Goff–Amon-Ra–LaPorta version with Swift/Odunze/Malik had blended P95 ~178.09 and 7.10%. All differences are conditional on strong modeling assumptions and do not measure the probability of cashing in a ~7k-entry contest.

The **Odunze-for-Burden fallback** leaves $200 unused, with blended P95 **176.36** and model 170+ frequency **6.78%**. It becomes marginally preferable in the invented Burden 10-point-downside stress, but is not a mandatory swap. Preserve the selected candidate unless meaningful new information invalidates Burden's role.

The alternative **Judkins/Jones + Browns DST** lineup (Goff, Judkins, Jones, ARSB, Burden, Tucker, LaPorta, Kittle, Browns DST) uses $49,300 and avoids any player duplication except game exposure with the first $5 lineup. However, it has a slightly lower blended tail and exposes Judkins to heavy CLE–NYJ rain; not a better default.

## Inactives gate before noon Central

1. At approximately **10:30 a.m. Central**, check final 1 p.m. ET NFL inactives for Chase Brown, Aaron Jones, Luther Burden, Tre Tucker, relevant defense and any replacement depth changes; avoid submitting blindly before confirmation.
2. Check the exact **DraftKings Classic Sunday MAIN contest salary export** and 7k single-entry rule; site-specific contest may differ from third-party referenced prices.
3. Detroit/Arizona and SF/SEA late participants must be confirmed for later kickoff. LaPorta/Kittle late starts are legitimate FLEX considerations.
4. The $3 lineup was subsequently entered along with the $5 lineup. I still need to save the exact contest IDs and entry receipts for the post-slate audit.
5. Post-slate: compare realized scores and ownership to the saved projections; track each contest rank and payout, and note any injury exits; do not turn one good result into a claim of predictive edge.

## Sources and evidence timestamps

- [NFL official Week 5 status report](https://www.nfl.com/news/nfl-week-5-injury-report-player-statuses-for-all-15-games)
- [4for4 October 9 slate market overview](https://www.4for4.com/2026/w5/squirrel-patrols-week-5-nfl-main-slate-dfs-gpp-picks)
- [FantasyPros October 11 Week 5 opportunity/value](https://www.fantasypros.com/2026/10/nfl-dfs-values-picks-targets-advice-week-5-2026/)
- [Tre Tucker DK Network Week 5 role](https://dknetwork.draftkings.com/2026/10/10/tre-tucker-fantasy-football-start-or-sit-advice-for-week-5/)
- [Bears' Luther Burden and game-script breakdown](https://www.prizepicks.com/playbook-article/bears-vs-packers-prediction-spread-nfl-picks-today-sunday-october-11)
- [Shark Snip Oct 11 public player/salary projection feed](https://sharksnip.com/picks/dfs/nfl), including Goff $6,600, Aaron Jones $6,500, Burden $4,900, Tucker $4,800 and LaPorta $4,900. This provider's modeled ownership is not the actual ownership of the 7k contest.
