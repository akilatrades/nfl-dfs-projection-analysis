# Week 5 single-entry constructions — October 9 update

**Scope:** DraftKings NFL Classic Sunday afternoon, October 11, assumed from the ongoing project. All target contests have at least **1,000 entries**. Entry fee and exact contest are undecided; do not carry the Thursday $5 fee or earlier $12 assumption into this new profile. This snapshot precedes final Friday reports and official contest salary verification.

The screen now contains **43 players, 62 construction specifications, 60 feasible results and 45 unique rosters**. Six QB families were compared: Maye, Brissett, Goff, Bagent, Rodgers and Stroud. The two infeasible cases are explicitly recorded. These are conditional optima within a curated pool, not a full-slate or contest-payout optimum.

## Three starting builds

| Slot | 1,000–3,000 entries | 4,000–6,000 entries | 15,000–25,000 entries |
|---|---|---|---|
| QB | Drake Maye — $6,300 | Jacoby Brissett — $5,500 | Tyson Bagent — $4,700 |
| RB | Chase Brown — $6,900 | Chase Brown — $6,900 | Chase Brown — $6,900 |
| RB | Jonathan Taylor — $7,800 | Jahmyr Gibbs — $9,800 | Jahmyr Gibbs — $9,800 |
| WR | DK Metcalf — $5,400 | DK Metcalf — $5,400 | Christian Watson — $6,400 |
| WR | Michael Wilson — $6,200 | Michael Wilson — $6,200 | DK Metcalf — $5,400 |
| WR | Rome Odunze — $4,700 | Rome Odunze — $4,700 | Malik Washington — $4,600 |
| TE | Hunter Henry — $3,700 | Hunter Henry — $3,700 | Colston Loveland — $4,600 |
| FLEX | Trey McBride — $6,700 | T.J. Hockenson — $4,800 | Rome Odunze — $4,700 |
| DST | Chargers — $2,300 | Browns — $2,800 | Browns — $2,800 |
| **Salary** | **$50,000** | **$49,800** | **$49,900** |
| **Manual mean estimate** | **133.55** | **133.25** | **130.44** |
| **Worst tested sensitivity** | **125.82** | **124.32** | **120.52** |

These field ranges are planning examples, not sharp mathematical cutoffs. For fields between them, weigh the payout concentration and strength of the final player roles. The larger-field construction is also a starting point for larger contests; exact payouts and ownership could change the choice substantially.

### Smaller field: Maye with Henry

This is the highest-mean specification in the current screen, albeit by a tiny margin. It pays for Brown and Taylor instead of relying on newly opened backfields or Marks' committee role. Maye–Henry supplies one QB pass catcher; no Raiders bring-back is forced. Wilson and McBride provide Arizona exposure without a four-player game stack. Its two-TE allocation is a salary/projection choice, not proof that double TE is best for a smaller tournament.

This is my initial anchor if choosing only one contest near the lower end of the requested range. A 1,000-entry contest still needs a high score to win. This build has meaningful downside, including Brown's target assumption, Henry's scoring role and Arizona receiving production. The scenario results are not a floor or cash probability.

### Middle field: Brissett with Wilson, Gibbs opposite

The Gibbs-constrained Brissett result saves at QB to fund the most expensive running back in the pool. Wilson supplies the QB stack; Gibbs provides an opposing player from Detroit. This is a different allocation from the October 8 Brissett double-stack recommendation, which remains preserved as history. Hockenson's target share needs review as Jefferson and Addison's availability becomes clear. The current Hockenson input is not conditioned on either receiver being out.

The base estimate is just 0.30 below the smaller-field lineup, too little to establish either as better. Gibbs' workload sensitivity is material. His absence from the smaller build is a salary choice, not a recommendation to fade a popular player.

### Larger field: Bagent with Odunze and Loveland, Watson opposite

The Bears double stack concentrates scoring in a particular passing outcome and the lower QB salary funds Gibbs. Watson provides an opposing receiver. The offense needs more than a low-volume, run-heavy Chicago win; Bagent's role is confirmed but his passing efficiency and touchdown production remain uncertain. Malik Washington's production also depends on Miami sustaining passing volume.

This is the higher-concentration challenger, with a 3.10-point lower mean than the smaller-field build and a worse tested downside. It has **not** been shown to have a higher ceiling, win probability or expected payout. It is not labeled lower-owned: no verified ownership projections were used. A bigger field alone is not a reason to sacrifice unlimited expected points or roster a player without a supported role.

## Alternatives actually tested

- Goff with St. Brown and Jameson Williams, Michael Wilson opposite: `jared_goff_two_wr_mean_te1`, $50,000, mean 128.21. This one-TE build also has Brown, Marks, Metcalf, Schultz and Chargers DST. It sacrifices about 5.34 modeled points versus the smaller-field example and depends on Marks' committee workload. Keep it as a Detroit passing scenario, not an automatic large-field upgrade.
- Rodgers with Metcalf and Freiermuth, Taylor opposite: `aaron_rodgers_game_mean_te2`, $49,700, mean 130.92. The remaining players are Brown, Michael Wilson, Odunze, McBride and Browns DST. Pittman's reported absence is relevant, but Rodgers' passing volume and the target distribution remain assumptions.
- Stroud with Collins and Schultz, Pollard opposite: `cj_stroud_game_mean_te2`, $49,500, mean 130.16. Brown, Metcalf, Odunze, McBride and Browns DST complete the roster. This expands the game pool beyond Detroit–Arizona and Chicago–Green Bay. It does not establish that Tennessee will sustain a shootout.
- The best one-TE Maye construction has Marks, Brown, Metcalf, Collins, Odunze, Henry, St. Brown and Browns DST, $50,000, mean 132.56. It gives up about 0.99 points and introduces Marks' committee role. The selected two-TE version is a modest preference, not a statistically significant finding.

All full rosters are in `lineups.csv`; `comparison.csv` includes their four scenario totals. Similar specifications often select the same roster. We do not count those as independent evidence.

## Research corrections and input changes

**Bagent:** the earlier October 8 hold was too conservative and missed already-published starter confirmation. [Chicago's October 7 article](https://www.chicagobears.com/news/tyson-bagent-looking-forward-to-facing-rival-packers) confirms his Week 5 start and reports 25 completions on 34 attempts for 268 yards in Week 4. He is reopened without automatically extrapolating that performance; the original 30-attempt prior remains.

**Judkins:** the original 18-carry, 4.1-YPC assumption overstated his recent rushing baseline while understating receiving involvement. The new analyst scenario uses 16 carries, 3.6 YPC, 3.5 targets, 75% catch rate and 6.4 yards/reception; rushing TD expectation falls from 0.55 to 0.45 and the rushing-bonus probability from 0.22 to 0.10. [Cleveland's player stats](https://www.clevelandbrowns.com/team/players-roster/quinshon-judkins/career) and [PFR's team table](https://www.pro-football-reference.com/teams/cle/2026.htm) previously retrieved show 59 carries for 177 yards and 16 targets through four games. The revised numbers are a judgment between that small sample and a possible workload change, not a fitted forecast.

**Metcalf:** the new scenario uses eight targets instead of seven and 0.45 receiving TD instead of 0.40. [Friday morning reporting on Pittman](https://lastwordonsports.com/nfl/2026/10/09/michael-pittmans-absence-opens-door-for-steelers-receivers/) describes a multiweek absence. The [official injury table](https://www.steelers.com/team/injury-report/) still showed Thursday DNP and blank Friday/game-status columns at retrieval. The target increase is an analyst response to the report, not an official usage forecast. Reverting both changes lowers each selected lineup by 1.74 points; Metcalf appears in all three.

**Schultz:** targets fall from 6.5 to 5.5 and receiving-TD expectation from 0.25 to 0.20 to avoid assuming his role with Collins absent continues after Collins' return. The [Texans' September 30 coach availability](https://www.houstontexans.com/video/press-conferences) discusses Collins' return; [season receiving totals](https://www.pro-football-reference.com/teams/htx/2026.htm) show Collins has only two games in the four-game sample. Tank Dell's activation remains another variable.

Eight added players: Rodgers, Stroud, Collins, Loveland, Freiermuth, Pollard, Marks and Allen. Their explicit workload and efficiency assumptions are in `projection_inputs.csv`; the change log distinguishes additions from the 11 revised numeric cells. All 43 rows remain **manual, uncalibrated football assumptions**, even when informed by sourced observations. Most existing priors are carried forward; they have not all been individually refitted to recent usage.

## Salary and availability evidence

All observations below were reviewed October 9 before final Friday reports. Published salaries are not an official contest export.

| Source | Used for |
|---|---|
| [DK Network October 8 main-slate picks](https://dknetwork.draftkings.com/2026/10/08/nfl-dfs-picks-best-draftkings-fantasy-football-plays-for-week-5/) | Rodgers $5,300, Stroud $5,900, Collins $7,500, Loveland $4,600, Freiermuth $3,900, Marks $4,800, Allen $5,400. Salary evidence, not imported fantasy projections. |
| [Splash Play Week 5 table](https://splashplaypodcast.com/dfs/nfl/2026-week-5/) | Pollard $5,600; cross-check selected published salaries. Its October 6 projections are not the model inputs. |
| [Fantrax October 9 slate discussion](https://fantraxhq.com/draftkings-week-5-main-slate/) | Recent Loveland opportunity supports adding him for review, not guaranteeing a repeated target share. |
| [Cincinnati injury table](https://www.bengals.com/team/injury-report/) | Chase limited Thursday, Higgins DNP; keep replacement receivers on hold. The page has an incorrect Chiefs heading; use its Cincinnati/Miami table. |
| [Pittsburgh injury table](https://www.steelers.com/team/injury-report/) | Dowdle limited Wednesday/Thursday; Warren remains held pending workload clarity. |
| [Seattle injury table](https://www.seahawks.com/team/injury-report/) | Charbonnet and Holani limited Thursday; Emanuel remains held pending activation and backfield clarity. |
| [Minnesota injury table](https://www.vikings.com/team/injury-report/) | Jefferson and Addison limited Thursday; do not automatically boost Hockenson as if both are out. |
| [October 9 morning injury roundup](https://dknetwork.draftkings.com/2026/10/06/nfl-injury-report-week-5/) | Pollard full Thursday; Hall week-to-week/DNP; Diggs DNP. This is a secondary, AI-attributed roundup, cross-checked with team reports where available. |
| [Houston backfield analysis](https://www.profootballnetwork.com/fantasy-football/fantasy-football-week-5-start-em-sit-em-2026/) | Marks' recent 42% snap share versus Montgomery's 58%; retain a committee assumption. |

Allen is included for later re-optimization **only if Hall is confirmed out**; he remains excluded from this primary screen. Tinsley, Meyers, Diggs, Warren and Emanuel are also held as research choices, not declarations that they are inactive. Burrow and Jayden Daniels remain in the stored pool but are outside the six researched stack families until receiving options are adequately supported.

## Method, limitations and reproducibility

Run `python run_week5_field_sizes.py` from the repository root. `profile.json` records field bands, holds and the three analyst selections. `recommended_lineups.csv` contains the selected rosters. `manifest.json` captures input/code/output hashes and infeasible cases. Earlier October 8 and Thursday Showdown snapshots are preserved; this directory is the current Sunday research snapshot.

For each QB, test minimum one pass catcher with optional bring-back, minimum two with required bring-back, and a Gibbs-constrained build. The first two templates have mean and maximin objectives. Every template is run with a maximum of one TE and with the usual maximum of two. Goff also gets the explicitly locked St. Brown/Jameson pair. No constraint makes a selected player low-owned.

The maximin screen uses four columns: base projection; the previous joint workload stress; all RB workload/TD/bonus inputs reduced 20%; and the current QB team's passing attempts/TD/bonus plus receiving targets/TD/bonus reduced 20%. The latter two are separate diagnostics, applied consistently across QB families. They are not combined with each other, probability weighted, or claimed to capture every possible downside. The prior joint stress still covers only its original six player/role cases and is asymmetric; do not interpret it alone as lineup robustness.

The two failed specifications require a Maye double stack and a Raiders bring-back with only one TE. This pool needs Henry for the double stack and Bowers for the bring-back, so the one-TE restriction makes those cases infeasible. This is a limitation of the pool, not a conclusion that real-world Maye double stacks are impossible.

Field sizes are **analyst construction labels**. The model does not simulate contest opponents, joint scoring tails, ownership, duplication, payouts or win probabilities. More game concentration can amplify both good and bad outcomes; it does not by itself prove better tournament value. No new weather adjustment has been made.

Next checks: final Friday statuses; Sunday inactives and relevant outdoor wind/weather; official contest salary export and player IDs; actual contest size and payout curve; credible ownership estimates before making any differentiation claim. Rebuild with confirmed roles, especially Cincinnati, Pittsburgh, Seattle, New York Jets and Minnesota. Use the actual contest's lock rules for any late swap; the current full-roster re-optimizations do not model already-locked players.
