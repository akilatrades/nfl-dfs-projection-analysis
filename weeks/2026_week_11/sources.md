# Week 11 source log — Sunday, November 22, 2026

Research began about 8:51 AM Central, before the 10:30 AM Central early-game inactive releases. The public pages below were accessed this morning. This is not an official DraftKings salary export or a subscription projection feed.

| Source | Information used | Qualification |
|---|---|---|
| [SPAGS position boards](https://splashplaypodcast.com/dfs/nfl/qb-rankings/) — also `/rb-rankings/`, `/wr-rankings/`, `/te-rankings/`, `/dst-rankings/` | Published DK salaries, point forecasts and implied totals; updated November 22, 8:08 AM ET | Numeric inputs saved in `inputs.json`; not the complete DK pool. Individual player pages can be a day older than the position board. |
| [Fantasy Sports Central cheatsheet](https://fantasysportscentral.com/football/dfscheat.php) | Second forecast for 64 included players, rushing and receiving TD expectations where captured | One snapshot; not all positions have a second source. No artificial second source added. |
| [FTN Week 11 cash picks](https://ftnfantasy.com/top-nfl-dfs-cash-game-picks-for-week-11-2026) | Third forecast for 12 named offensive players | Friday estimates can lag Sunday information. Median of available published forecasts is used, not an average of models assumed independent. |
| [Fantasy Team Advice ownership](https://fantasyteamadvice.com/nfl/dfs-ownership-projections) | Sunday 9:26 AM ET public top three at each position | Only visible forecasts are labelled published. Emmett 74.8%, Coleman 36.5%, Pollard 29.7%, Dak 25%, Lamb 30.3%, Tate 27%, Pickens 24%. Other included players mostly have analyst assumptions. These are broad-slate forecasts, not observed contest ownership. |
| [NFL final injury report](https://amp.nfl.com/news/nfl-week-11-injury-report-2026-season) | Walker and Ferguson out; Beck/Hurts out; Tate, Mayfield and Bowers questionable; Kincaid doubtful | Friday injury designations must be superseded by Saturday transactions and Sunday inactives. No claim that an early-game inactive release had already occurred. |
| [Titans Spears IR transaction](https://www.tennesseetitans.com/news/titans-place-rb-tyjae-spears-on-injured-reserve) | Spears placed on IR November 21; Carter elevated | Replaces the older questionable designation. Related official roster announcement confirms Wan'Dale Robinson on IR. |
| [Titans injury report](https://www.tennesseetitans.com/team/injury-report/) | Tate full Friday practice but still questionable | Active does not establish unrestricted snap count after a shoulder absence. Tate's reduced-role stress is explicit. |
| [Bills official injury report](https://www.buffalobills.com/news/buffalo-bills-injury-report-vs-dolphins-week-11) | Kincaid doubtful; Hawes questionable | Team explicitly says Kincaid still has a chance to play. Do not assume Knox inherits an unrestricted receiving role. |
| [NFL Week 11 capsules](https://media.nfl.com/content/dam/communications/football-communications/2026/capsules/Week%2011%20Capsules.pdf) | Recent usage context, including Ayomanor and Egbuka | Recent production is context, not an automatic projection increase. |
| [Ayomanor FantasyPros](https://www.fantasypros.com/nfl/players/elic-ayomanor.php) | Recent target involvement and matchup context | Recent 10-target game occurred without Tate. Do not forecast that volume unchanged when Tate returns. |
| [Meyers FantasyPros notes](https://www.fantasypros.com/nfl/notes/jakobi-meyers.php) | Secondary receiving role; target share and red-zone involvement | Salary relief with limited ceiling, not a newly promoted alpha. Meyers is a risk in the alternate construction. |
| [Egbuka FantasyPros outlook](https://www.fantasypros.com/nfl/notes/499797/emeka-egbuka-2026-week-11-outlook.php) | Target/first-read involvement, shared work with Godwin | Role and QB health remain risks. No Godwin absence assumed. |
| [My Sports Weather](https://mysportsweather.com/nfl) | Wind/rain details for Chicago, Kansas City and New York | Chicago forecast includes clearing; 10% passing reduction is an adverse scenario, not a measured weather effect. Dallas roof status was not verified. |
| [NOAA Chicago forecast discussion](https://forecast.weather.gov/product.php?format=CI&glossary=1&highlight=on&issuedby=LOT&product=AFD&site=NWS&version=1) | Morning/early afternoon frontal rain and wind | Forecast timing can change. |

## Market snapshot differences

The scoring model freezes the position-board totals: DAL–TEN 54.5; CHI–NO 48.5; DET–TB 47.5; JAX–NYG 45.5; BUF–MIA 44.5; BAL–CAR 43.5; LAC–NYJ and DEN–LV 41.5; ARI–KC 40.5; PHI–PIT 37.5. Other Sunday sources had Dallas at 55, Baltimore–Carolina 44.5, Denver–Las Vegas 40.5 and Detroit–Tampa Bay 45.5. These are differing source/time snapshots, not simultaneously executable odds. Exact frozen implied totals are in `run.py`; totals determine an approximate TD environment rather than forecasted final scores.

## Coverage and data gaps

116 included players: 16 QB, 32 RB, 40 WR, 16 TE, 12 DST. All ten main-slate games have representation, but four starting QBs and eight defenses are absent from this curated search. No claim of an exhaustive full-player-pool optimum. No official contest ID, payout ladder, complete salary export or opponent entries were supplied. The two field capacities are carried forward from last week's screenshots, pending a new contest screenshot.
