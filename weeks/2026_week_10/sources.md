# Week 10 source record — November 15, 2026

Sources were retrieved before the noon America/Chicago main-slate lock. Different sites may share feeds; three forecasts are not three independent measurements. Named public facts are extracted; full articles are not republished.

## Forecasts and published salaries

- SPAGS position boards, November 15 9:10 AM ET snapshot: [QB](https://splashplaypodcast.com/dfs/nfl/qb-rankings/), [RB](https://splashplaypodcast.com/dfs/nfl/rb-rankings/), [WR](https://splashplaypodcast.com/dfs/nfl/wr-rankings/), [TE](https://splashplaypodcast.com/dfs/nfl/te-rankings/), [DST](https://splashplaypodcast.com/dfs/nfl/dst-rankings/). Salary, team, opponent and point estimates are saved by player in `inputs.json`.
- [FantasySportsCentral Week 10](https://fantasysportscentral.com/football/dfscheat.php): second forecast where captured and salary cross-check. Includes off-slate games; those games were explicitly excluded. DST cross-checks and current replacement QBs were reconciled before the final model run.
- [FTN Week 10 cash projections](https://ftnfantasy.com/top-nfl-dfs-cash-game-picks-for-week-10-2026): third forecast for the public top-three positional previews. These are cash-oriented means, not tournament win probabilities. Warren's 17.4 is materially above the other forecasts; median, not maximum, is used.
- [dfsroto](https://dfsroto.win/projections): quality cross-check only. Its QB/role listings disagreed with newer official starter news and some new workload assumptions. It is not blended into the base means.
- [FSN](https://footballsportsnews.com/nfl/dfs/draftkings/week-10-2026/): reviewed but not used for baseline means. It includes off-slate Burrow/Chase and materially higher means for some players. A page covering Week 10 is not automatically the Sunday main slate.

Salaries for the selected players agree across published boards. The official contest draft-group/player-ID export was unavailable: direct public DraftKings requests returned HTTP 403. The CSV is a human-readable recommendation, not a DK upload file.

## Ownership

- [FantasyTeamAdvice](https://fantasyteamadvice.com/nfl/dfs-ownership-projections), first captured at 11:20 AM ET. Latest check at 11:55 AM ET: Emmett 67.9%, Jefferson 31.0%, Bijan 29.9%, Olave 21.9%, Lamb 21.8%, Warren 20.2%. The late check is effectively unchanged at the precision used in the recommendation. Model inputs preserve the earlier snapshot rather than silently overwriting it.
- Other player ownership inputs are explicitly labeled analyst assumptions. They are not obtained from the paywalled rows, and they are not actual ownership in either user's contest.

## Markets, schedule and weather

- [BetMGM public football board](https://www.betmgm.com/en/sports/football-11/betting): market cross-check. The page's relative-day label was stale; matchups were reconciled against the NFL schedule.
- [NFL official Sunday schedule/inactives](https://amp.nfl.com/news/nfl-week-10-inactives-players-ruled-out-sunday-2026-season).
- [MySportsWeather](https://mysportsweather.com/nfl): main-slate totals and kickoff weather. `run.py:GAMES` freezes the research working totals, which can differ from another book by 0.5–1 point. BUF-NYJ has modest wind/gust risk; CLE has modest wind/rain risk. NO is indoors. Dallas has a retractable roof; roof closure was not independently verified, so no unconditional outdoor-weather penalty is imposed.
- [FantasyPros game-stack research](https://www.fantasypros.com/2026/11/nfl-dfs-lineup-advice-picks-predictions-week-10-2026/): SF-DAL and NO-CAR opportunity/matchup review.

## Official role changes and availability

- [NFL final injury report](https://amp.nfl.com/news/nfl-week-10-injury-report-2026-season): Walker ruled out; other final designations. [NFL Friday player table](https://www.nfl.com/injuries/league/2026/REG10): Pickens full practice, no final designation; Ferguson out. Club pages with blank Friday/UNSPECIFIED rows were not treated as a fresh downgrade.
- [Vikings inactives](https://www.vikings.com/news/inactives-packers-week-10-2026): Addison/Jennings/Hockenson/Murray out; Cousins starts. Jefferson's mean is not automatically inflated to absorb every missing target.
- [Saints inactives](https://www.neworleanssaints.com/news/new-orleans-saints-inactives-carolina-panthers-2026-nfl-week-10): Fuaga/McCoy out; selected Saints not on the list. OL losses remain a risk for Shough.
- [Panthers inactives](https://www.panthers.com/news/week-10-inactives-at-new-orleans-cornerback-will-lee-inactive-for-saints-games): Will Lee out; practice-squad corners starting. Chuba is available. This supports the Olave matchup but does not guarantee a ceiling.
- [Falcons inactives](https://www.atlantafalcons.com/news/atlanta-falcons-week-10-inactives-vs-kansas-city-chiefs): Branch/Deablo out; London/Bijan/Pitts available.
- [Colts receiving-room changes](https://www.colts.com/news/after-trading-keenan-allen-and-josh-downs-who-s-left-at-wide-receiver-for-the-colts): Allen traded to SF, Downs to KC; Warren opportunity and several WR replacements. Treadwell already had substantial snaps, so his route share cannot simply be inflated from the trades.
- [Colts inactives](https://www.colts.com/news/colts-rule-announce-6-inactive-players-for-week-10): Mallory out; Warren available.
- [Bills inactives](https://www.buffalobills.com/news/buffalo-bills-inactives-list-at-jets-week-10): selected offensive starters available; Spencer Brown upgraded active, despite earlier doubtful designation.
- [49ers report](https://www.49ers.com/team/injury-report/week/REG-10): Evans out, Deebo cleared, several DBs questionable. Keenan Allen's arrival is receiving competition for Kittle/CMC, not a reason to assume all missing Evans volume transfers to one player.
- [Texans inactives](https://www.houstontexans.com/news/texans-inactives-week-10-vs-cleveland-browns): Harrison, Montgomery, Hunter, Rutledge and Teller inactive. Houston's offensive-line/receiving losses support a low-cost Browns DST case; Houston's own defensive losses matter when considering Texans DST.
- [Browns official depth chart](https://www.clevelandbrowns.com/news/browns-announce-unofficial-depth-chart-for-week-10-vs-the-texans): Watson is QB1, superseding stale Sanders-based projection lists.

## Selected-role checks

- [Olave](https://splashplaypodcast.com/dfs/nfl/players/chris-olave/), [Emmett](https://splashplaypodcast.com/dfs/nfl/players/emmett-johnson/), [Warren](https://splashplaypodcast.com/dfs/nfl/players/tyler-warren/), [Meyers](https://splashplaypodcast.com/dfs/nfl/players/jakobi-meyers/), [Pickens](https://splashplaypodcast.com/dfs/nfl/players/george-pickens/). Modeled targets/carries are forecasts, not promises. Some individual pages retain an older November 14 snapshot than the November 15 position boards; current board means govern the baseline.
- [Meyers outlook](https://www.fantasypros.com/nfl/notes/493178/jakobi-meyers-2026-week-10-outlook.php), [Pitts outlook](https://www.fantasypros.com/nfl/notes/493121/kyle-pitts-2026-week-10-outlook.php), [weekly role notes](https://www.fantasypros.com/nfl/notes/weekly-flex.php): modest Meyers volume, Wan'Dale target/red-zone role, variable Kincaid routes, Moore's reduced route share, and Pitts' recent catchable-target problem. These risks were reviewed rather than inferred from salary alone.

The contest screenshot supplies fees, guarantees and entry capacities, not a payout ladder, draft-group ID or final field. No payout EV or actual duplication rate can be calculated from it.
