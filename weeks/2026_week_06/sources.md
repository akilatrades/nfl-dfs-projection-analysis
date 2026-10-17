# Week 6 source register

Research retrieved October 17, 2026. Published salaries are provisional until matched to the contest export. No outside fantasy-point projections or ownership percentages were imported.

| ID | Source | Use and boundary |
|---|---|---|
| NFLV | nflverse weekly player stats and schedule (via the sports-market-maker data pull, `data/nfl/`) | Week 1–5 attempts, carries, targets, receptions, yards and touchdowns per player; Week 6 kickoffs, spreads and totals. Public box-score history, not a forecast. |
| INJ | nflverse Week 6 injury file (retrieved Oct 16, before Friday designations) | Only Charbonnet (SEA, not on this slate) carried a designation at retrieval. Practice-report notes below come from the articles. |
| DKN | [DraftKings Network tournament picks, Week 6](https://dknetwork.draftkings.com/2026/10/15/nfl-dfs-tournament-picks-high-upside-draftkings-gpp-plays-for-week-6/) | October 15 salaries for 29 players and three defenses; implied totals; Rice out (KC), Concepcion concussion, Corum sharing with Kyren, Tracy and Harris both involved (NYG). Editorial picks are not inputs. |
| FL | [FantasyLabs main-slate breakdown](https://www.fantasylabs.com/articles/nfl-dfs-picks-week-6-main-slate-draftkings-breakdown-2026/) | Cousins and Huntley salaries; Caleb Williams questionable (full practice Thursday, hamstring); Lamar Jackson day-to-day Friday. Its projection figures are not inputs. |
| FSP | [Fantasy Six Pack game-by-game breakdown](https://fantasysixpack.net/2026-nfl-dfs-week-6-main-slate-game-by-game-breakdown/) | Salaries for 20 more players; Henderson out (NE), Dowdle returns (PIT), Barkley expected back (PHI), Olave did not practice Thursday (NO), Penix expected to start (ATL), Terrell out (ATL). Its "Kenneth Walker, KC" placement agrees with the nflverse team field. |

Slate: the ten Sunday afternoon games on October 18 (1:00, 4:05 and 4:25 ET). Excluded: Thursday SEA–DEN, the London game (HOU–JAX, 9:30 ET), Sunday night DAL–GB, Monday night WAS–SF. Bye: CIN, DET, MIA, MIN.

Team totals are derived from the schedule file's spread and total: (total ± spread) / 2. All football inputs are **shrunk Week 1–5 rates** (src/input_model.py), not analyst assumptions as in Week 5; the DST event inputs are analyst assumptions scaled by the opponent's implied total. Standard deviations are position priors and do not rank lineups.
