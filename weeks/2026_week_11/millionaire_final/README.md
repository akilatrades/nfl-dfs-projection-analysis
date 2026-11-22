# Week 11 Sunday Millionaire

The November 22, 2026 recommendation for one entry in the $20 DraftKings NFL Fantasy Football Millionaire is J.J. McCarthy with Malik Nabers and Isaiah Likely. The contest has 147,058 seats, $2.5 million in prizes and $1 million to first. Final review completed at 11:17 AM Central. Main slate kickoff is noon Central. [DraftKings contest](https://www.draftkings.com/draft/contest/197882014) · [Week 11 contest listings](https://www.draftkings.com/fantasy-football)

| Slot | Player | Salary | Mean DK points | Projected ownership |
|---|---|---:|---:|---:|
| QB | J.J. McCarthy, NYG | $4,800 | 16.1 | 2.6% |
| RB | Emmett Johnson, KC | $6,000 | 23.5 | 56.6% |
| RB | Chuba Hubbard, CAR | $7,500 | 19.7 | 10.8% |
| WR | Malik Nabers, NYG | $7,100 | 15.7 | 12.9% |
| WR | Carnell Tate, TEN | $5,500 | 15.1 | 21.9% |
| WR | Elic Ayomanor, TEN | $3,700 | 9.5 | 19.1% |
| TE | Isaiah Likely, NYG | $5,600 | 14.2 | 10.1% |
| FLEX | Tony Pollard, TEN | $6,500 | 18.5 | 17.9% |
| DST | Pittsburgh Steelers | $3,300 | 8.5 | 8.9% |

Salary totals $50,000. Three running backs require an RB at FLEX, and all three play at noon Central. McCarthy, Nabers and Likely retain their individual late slots at 3:25 p.m. Central.

## Why change the Ward lineup

McCarthy costs $700 less than Ward, with projected ownership of 2.6% to Ward's 9.2% on the same board. Nabers had at least five catches in eight of nine games. Likely had five double-digit-target games entering the week. Two or three McCarthy passing touchdowns concentrated on those receivers can move all three roster slots together. Jacksonville is favored by six and the Giants' implied total is 19.75, so this selection depends on New York beating its scoring expectation. [Giants matchup notes](https://www.giants.com/news/numbers-to-know-giants-jaguars-week-11-jj-mccarthy-cam-skattebo-isaiah-likely-abdul-carter-jevon-holland) · [Likely's receiving role](https://www.giants.com/news/week-11-jacksonville-jaguars-jj-mccarthy-malik-nabers-isaiah-likely-arvell-reese-deonte-banks-greg-newsome-john-harbaugh) · [Field ownership estimates](https://covertheslate.com/nfl-week-11-draftkings-ownership-projections-november-22-2026/)

Dallas–Tennessee led the main slate at 54.5, including 23.5 for Tennessee. Tate is active following his shoulder injury. Tyjae Spears is on IR and Nick Singleton is inactive. Pollard has a credible rushing and receiving role. At $3,700, Ayomanor can earn his place with a modest receiving line. The three Titans compete for touchdowns. A Dallas blowout with few Titans points, or several Ward rushing scores, can sink the entry. The final checks include direct swaps from Pollard to Coleman, Warren or Pickens and from Tate to Egbuka. [Titans inactives](https://www.tennesseetitans.com/news/game-inactives-week-11-titans-at-cowboys) · [Spears transaction](https://www.tennesseetitans.com/news/titans-place-rb-tyjae-spears-on-injured-reserve) · [Sunday totals and weather](https://mysportsweather.com/nfl)

Emmett retains a strong receiving and rushing projection with Kenneth Walker III out. Kansas City is also missing offensive linemen Trey Smith and Jaylon Moore, and Jaydn Ott is available. Hubbard's workload remains attractive with Jonathon Brooks still on IR. Pittsburgh faces Joe Milton III and a Philadelphia offense implied for 17 points. Chicago's rain and gusts added uncertainty to Odunze. The case for the switch comes from the entire nine-player lineup. [NFL inactive lists](https://www.nfl.com/news/nfl-week-11-inactives-players-ruled-out-sunday-2026-season) · [Carolina roster moves](https://www.panthers.com/news/panthers-activate-mike-jackson-from-ir-among-other-moves-isaiah-simmons-ir) · [Running back projections](https://splashplaypodcast.com/dfs/nfl/rb-rankings/)

## Simulation comparison

| Metric | McCarthy entry | Ward screenshot |
|---|---:|---:|
| Projected DK points | 140.74 | 140.14 |
| Median DK points | 137.65 | 137.30 |
| 95th-percentile DK points | 199.67 | 198.04 |
| 99th-percentile DK points | 231.92 | 229.60 |
| Ownership-based field, top 147 | 272 / 24,000 | 122 / 24,000 |
| Near-cap field, top 147 | 141 / 24,000 | 71 / 24,000 |
| Near-cap field, top 15 | 29 / 24,000 | 9 / 24,000 |
| Near-cap field, tied or outright first | 7 / 24,000 | 0 / 24,000 |
| Run/pass, roles and weather stress, top 147 | 112 / 16,000 | 57 / 16,000 |
| Likely reduced-role stress, top 147 | 85 / 16,000 | 48 / 16,000 |

The near-cap field spent an average of $49,706. Its Emmett exposure reached 76.0%, compared with 54.5% in the ownership-based field. The McCarthy roster matched 0 exact opposing rosters in the latter and 0 in the near-cap field. Closely related entries can still tie in the real contest. The 100,000-draw standalone player simulation and the full-field ranks answer different questions.

The initial screen compared 656 distinct legal lineups, including the screenshot, in two fields. Each field includes 147,057 independently generated opposing entries so adding the candidate fills the contest. Opposing entries can share players and duplicate full lineups. All entries receive the same player performances on a simulated Sunday. The initial 6,000 screening draws and the 24,000 draws used to validate the 49 finalists use distinct seeds. The original screen, field exposure audits and results are in [results.json](results.json).

The last comparison covered 31 lineups, including direct changes to both the Giants stack and the three Tennessee slots. Two new opponent fields share a fresh set of 24,000 game outcomes. One follows estimated ownership. The second spends at least $49,400, requires a 124-point projected lineup and adds a 16% chance of explicitly pairing the QB with his RB before standard roster validation. A 16,000-draw sensitivity lets team passing and rushing production move in opposite directions and reduces Tate's production by 20%, Emmett's by 10% and Chicago and New Orleans passing production by 10%. A separate 16,000-draw test reduces Likely's projected mean by 25%. [Final checks](final_check.json)

Scoring uses the repository's shared team passing and rushing touchdowns and a correlated approximation for yardage, receptions and bonuses. Its accuracy in real Millionaire contests has not been calibrated. The field covers 137 modeled players and defenses across ten games. Unknown opponent stacks, multi-entry portfolios, late swaps and actual duplication remain sources of error. The initial 130-point-minimum field drove Emmett's realized ownership to 94.5%. Treat that field as an extreme sensitivity. First-place counts are particularly noisy. No dollar-return estimate or real probability of winning follows from these simulated ranks.

## Sources and timing

Player means take the median of available public DK projections. The initial snapshot uses Sunday SPAGS, Fantasy Sports Central and previously captured FTN where available. The last comparison incorporates the 11:59 a.m. Eastern SPAGS WR, TE and DST update. Individual salaries and matchups were checked against the published boards. [Frozen inputs](inputs.csv) · [Last projection changes](final_updates.csv) · [SPAGS WR](https://splashplaypodcast.com/dfs/nfl/wr-rankings/) · [SPAGS TE](https://splashplaypodcast.com/dfs/nfl/te-rankings/) · [SPAGS DST](https://splashplaypodcast.com/dfs/nfl/dst-rankings/) · [Fantasy Sports Central](https://fantasysportscentral.com/football/dfscheat.php) · [FTN](https://ftnfantasy.com/top-nfl-dfs-cash-game-picks-for-week-11-2026)

Johnson, Tate and Ayomanor use STAT-API's public $20 Millionaire forecasts from Saturday. Other ownership values in the roster use Cover The Slate's Saturday main-slate estimates. The latter's Sunday update confirmed Tate's status and retained those estimates. Neither source has entrants' final lineups before lock. [Contest ownership](https://stat-api.com/tools/ownership/) · [Main-slate ownership](https://covertheslate.com/nfl-week-11-draftkings-ownership-projections-november-22-2026/)

Likely missed Friday practice with a groin issue and carries no game designation. The Giants' inactives are due about 1:55 p.m. Central. If Likely is unexpectedly inactive, Jacksonville's Brenton Strange at $4,100 is a same-game TE replacement, subject to his own availability and the contest's late-swap rules. [Giants injury report](https://www.giants.com/team/injury-report/) · [TE salaries](https://splashplaypodcast.com/dfs/nfl/te-rankings/) · [DraftKings NFL rules](https://www.draftkings.com/help/rules/nfl)

The entry applies prior slate lessons by preserving justified chalk, using two high-volume receivers with the tournament QB, checking returning and injured players, allocating team touchdowns once and checking alternative fields. The original nine survive the early inactive report. The change is a decision about tournament ranking. [Week 11 lessons from earlier slates](../lessons_applied.md)

Run `python simulate.py` and then `python final_check.py` from this directory with NumPy and SciPy installed. The two scripts use the archived Week 11 inputs and candidate list for reproducibility. No entry has been submitted or edited.
