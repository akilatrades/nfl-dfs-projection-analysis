# October 11 Week 5 — Correlated Monte Carlo and large-field $5 entry decision

> **Later user confirmation:** The user says this exact $5 / ~23,000-entry Love–Watson + Wilson–Jameson–McBride / Hunter Henry lineup **has been entered** on DraftKings and should stay unchanged absent material new information. This statement is based on the user's confirmation, not a verification of the platform's submitted entry. The earlier pre-lock status below records the time of the initial research decision, before that confirmation. A **separate** [$3 / ~7,000-entry lineup](../contest_3usd_7k_2026-10-11/README.md) is being prepared without editing the $5 roster.

**Status: Sunday pre-lock research, not a submitted DraftKings entry.** Source notes assembled around 9:20 a.m. Central. The user’s target contest is **$5, about 23,000 entrants, single-entry, 11-game DK Classic main slate**. Official contest ID, exact DK salary CSV and upload IDs, payout table, and final Sunday inactives were unavailable when recorded. Our prior [one-Bears-player Love–Watson lineup](../selected_prelock_revision_chicago.md) remains an immutable earlier decision; this document is a subsequent, evidence-driven selection.

## Executive conclusion: a better robust contender

After 13 candidate constructions and about **945,000 seeded slate-path simulations** across the initial ten-candidate 450k experiment and expanded 13-candidate 495k sensitivity run, I favor **Love + Christian Watson, with Michael Wilson + Jameson Williams + Trey McBride**, alongside two role RBs and Hunter Henry. It doesn't top every scoring prior. It **does beat our previously chosen Love/Malik/Metcalf/McBride lineup on the 190-point threshold under every six extended mean/scenario variants** we recorded. This is an **illustrative model-comparison result**, not a validated probability of winning the 23k-entry contest.

[Suggested roster decision CSV](recommendation_prelock_v2.csv), selected at **$50,000**:

| Slot | Player | Team | Source-referenced DK salary |
|---|---|---|---:|
| QB | Jordan Love | GB | $5,700 |
| RB | Chase Brown | CIN | $6,900 |
| RB | D'Andre Swift | CHI | $6,200 |
| WR | Michael Wilson | ARI | $6,200 |
| WR | Christian Watson | GB | $6,400 |
| WR | Jameson Williams | DET | $5,900 |
| TE | Hunter Henry | NE | $3,700 |
| FLEX | Trey McBride | ARI | $6,700 |
| DST | Chargers DST | LAC | $2,300 |
| **TOTAL** | | | **$50,000** |

**Two main game narratives:**
- **CHI–GB:** Love/Watson passing connection, plus Swift as the only Chicago return. Unlike the older Love/Watson/Swift/Odunze version, we are not counting on a Bears RB and Bears WR both winning their share allocations.
- **DET–ARI:** Michael Wilson + McBride receiving market share in a potentially high-volume Arizona game, with Detroit WR Jameson Williams as a real game return and a lower-salary tournament ceiling path than Amon-Ra St. Brown or Gibbs.
- **Other roles:** Chase Brown ($6,900) has a credible receiving role, though CIN receivers' statuses remain contingent; Hunter Henry ($3,700) is the salary-saving TE role, with about 4.5 targets in a [different external model](https://splashplaypodcast.com/dfs/nfl/te-rankings/) and ~10.8 projected DK points; Chargers DST ($2,300) opposes DEN without any conflicting offensive player.

**Important tradeoffs:** Tyler Shough / New Orleans does not enter this lineup; Kittle and the Browns DST are intentionally replaced. Hunter Henry's TD/usage ceiling is less certain than McBride's. Michael Wilson and McBride can compete for Arizona's TDs. Jameson Williams can be volatile if Detroit funnels points to Gibbs. Our simulator models this partially through opposing target-allocation shocks, but not a full play-by-play TD allocation.

## Why the earlier lineup lost confidence

Earlier pick: Jordan Love / Chase Brown / D'Andre Swift / Malik Washington / Christian Watson / DK Metcalf / George Kittle / Trey McBride / Browns DST; $49,900.

Rather than merely citing the old 136.76-point subjective mean, the experiment compared:
- Our stored **subjective football-input means** from the 48-player repo (where McBride 19.19, Swift 18.28, Chase Brown 18.93)
- An unrelated [Shark Snip October 11 public feed](https://sharksnip.com/picks/dfs/nfl) (McBride 13.1, Swift 14.1, Chase Brown 14.6; Juwan Johnson 13.4)
- A 50:50 midpoint between the two (arbitrary weighting, **not empirically fitted**)
- A separate [Splash Play/Spags updated Oct 11 WR screen](https://splashplaypodcast.com/dfs/nfl/wr-rankings/) and [TE screen](https://splashplaypodcast.com/dfs/nfl/te-rankings/): McBride **20.5**, Michael Wilson **18.4**, Jameson Williams **12.3**, Juwan Johnson **11.0**, Hunter Henry **10.8**. The disparity between the external McBride forecasts of 13.1 and 20.5 is big enough to reverse some otherwise plausible lineup rankings. The historical archived scores are *not* recalibrated to make this conflict disappear.

The three explicit criteria are (1) supported roles, (2) meaningful correlations without loading all nine slots onto one game, and (3) resilience when **analyst means or matchup assumptions change**. There is no ownership-adjusted EV optimizer or complete payout simulation yet.

## Monte Carlo methodology (reproducible)

[Executable zero-dependency Node source](../../../../monte_carlo_week5_2026.js), run with:

```bash
node monte_carlo_week5_2026.js > week5_mc_console_results.json
```

The published script contains its own player salary, team/opponent and source-projection snapshot, plus the full 13-lineup list, PRNG seed **20261011**, and six named runs. It uses **seeded 32-bit mulberry32 and Box–Muller normals**, so paired lineups face the **same drawn slate**. Each player's DK-point surrogate is lognormal around the specified projection with assumed log-scale volatility: QB 0.40, RB 0.57, WR 0.70, TE 0.60, rescaled in two broader historical-only tests. D/ST is a bounded linear score instead. The latent factors include a shared game scoring variable, team production, shared QB/pass-game variable, opposing rush/pass game-script tendencies, and negative within-team WR/TE opportunity-share shocks. Small discretionary injury-related downward mixtures produce extra downside.

These parameters were **chosen by judgment**, not fit to weeks of official play-level distributions. The simulator is **not a football-play event model** and the resulting distributions **are not calibrated confidence intervals**. A two-receiver 100% target-share conservation constraint or exact game TD budget is not guaranteed; the shared/negative shocks are only a correlation approximation. Simulated 190-point probabilities are **`P(score ≥ 190 | invented variance and inputs)`**, not probability of winning a $5 23k-field tournament. There are no opponent rosters, actual contest ownership joint distributions, payout schedule, field simulations, or duplicate-lineup penalty.

The model also reflects a **restricted 13-lineup universe**, not an exhaustive DFS slate optimizer, so “best among 13” is a relative ranking, not the odds of beating other contest entries.

## Numerical results: new vs original selected lineup

| Assumed mean/scenario regime | Old `P≥190` | Selected new `P≥190` | Old modeled P95 | New modeled P95 |
|---|---:|---:|---:|---:|
| 50:50 baseline | 2.30% | **2.89%** | 174.48 | **177.70** |
| Shark Snip-only public feed | 0.91% | **1.26%** | 158.66 | **162.80** |
| Our uncalibrated repo means | 5.12% | **5.60%** | 190.49 | **192.88** |
| Splash Play Sunday receiver and TE revisions | 3.16% | **5.01%** | 180.57 | **190.06** |
| Conservative Juwan/Jameson plus stronger McBride | 3.19% | **3.73%** | 180.85 | **182.95** |
| Detroit Gibbs-dominant/rushing script | 2.62% | **2.68%** | **177.16** | 176.64 |

All six named scenarios' inputs, lineups and results are saved in [extended_13_lineups_results.csv](extended_13_lineups_results.csv) and [extended_13_candidate_lineups.csv](extended_13_candidate_lineups.csv). The earlier [ten-lineup, five-assumption results](simulation_results.csv) are preserved separately; do **not** mix their 10-lineup ranking with the subsequent 13-lineup field. An [earlier disagreement sensitivity file](external_disagreement_sensitivities.json) records the intermediate McBride/Juwan check.

### What happens when the game disappoints?

The first blended ten-lineup runs show why the **game factor** matters. When the Detroit–Arizona game factor falls below -0.8, our *original* selected Love/Malik/Metcalf/McBride lineup averaged about 119.3 points; its scoring improved to 126.5 with the game factor above +0.8. The Love/Wilson/Jameson/Juwan game-mini-stack ranged roughly **118.5 to 133.4** under the same directional conditioning. Those are broad latent-factor scenarios, **not modeled probability of a Detroit blowout**.

For the new selected Love/Watson/Wilson/Jameson/McBride/Henry construction, the 13-lineup runner saves its actual conditional AZ and GB figures in the extended CSV. In a Detroit rushing-heavy script, the new construction's modeled P≥190 advantage over the original becomes marginal (**2.68% versus 2.62%**) rather than strong. If both Arizona receiving options and Jameson lose opportunity simultaneously, this build can fail.

### Lessons from Weeks 3 and 4 applied, not just quoted

- **Week 3 Coker / Week 4 Parker:** Injury-related opportunity is not guaranteed to go to one cheap receiver. This build uses Wilson's recent 30 targets over the past two games and McBride's repeat 10-plus targets rather than assuming Doubs 7.5 or rookie TeSlaa eight targets again ([DraftKings Week 5 buzz audit](https://dknetwork.draftkings.com/2026/10/09/nfl-dfs-chalk-plays-week-5/)).
- **Week 3 weak value accumulation:** Hunter Henry at $3,700 is still a weakness, but has more documented stand-alone opportunity than an unsupported two-TD Doubs forecast. Do **not** assert Hunter is guaranteed 20+ points.
- **Week 4 touchdown/target-share error:** Wilson and McBride may consume each other's scoring chances. The simulator includes negative within-team receiver-share shocks; no validated hierarchical TD distribution yet.
- **Week 4 game concentration:** Detroit–Arizona offers a high fantasy scoring total, but the low DET–ARI scenario is tracked. Love–Watson gives a second game ceiling.
- **Week 4 different tournament goals:** These are head-to-head threshold comparisons appropriate for discussing *large-field upside*, but not an actual optimized 23k-field payout calculation.

## Sunday evidence and gates

- [NFL 2026 Week 5 official schedule](https://www.nfl.com/schedules/2026/by-week/week-5): the 11-game Classic main slate excludes 9:30 a.m. ET London and 8:20 p.m. ET Sunday night.
- [SPAGS October 11 WR estimates](https://splashplaypodcast.com/dfs/nfl/wr-rankings/): Wilson 18.4 and Jameson 12.3 modeled points; the public alternate says Wilson 14.7 and Jameson 11.9. These are **projections**, not played results.
- [Pride of Detroit Oct 11 player analysis](https://www.prideofdetroit.com/detroit-lions-gambling-odds/176470/detroit-lions-arizona-cardinals-best-player-prop-bets-nfl-week-5): Jameson six catches for 102 yards last game, in a matchup facing a struggling ARI pass defense. One game does not guarantee repeat.
- [Pro Football Network Oct 11 weather review](https://www.profootballnetwork.com/fantasy-football/nfl-weather-report-week-5-2026/): CLE–NYJ has rain risk, PIT–IND possible showers, CHI–GB and SF–SEA relatively clear; removing Metcalf/Browns DST is weather diversification rather than a claim either cannot score.
- **Before noon CT lock:** verify official DK salary/player-ID file; early inactives normally available around 10:30 a.m. CT. Check Chase Brown, Swift, Hunter Henry, and any unexpected early scratches; later games’ receiver/TE statuses must also be monitored. A roster with late FLEX McBride permits some substitution flexibility, but **not after a locked player's kickoff**.
- The lineup contains **3 GB/CHI and 3 DET/ARI offensive pieces**. There is real upside, but it remains more concentrated than the earlier modest one-off Arizona construction. No claim of guaranteed cash or edge.

## Reproducible versus unknown

- **Actually executed in the connected JavaScript runtime:** 450k initial scenarios + 495k expanded scenarios; additionally three 55k projection-disagreement probes. All 13 salaries, positions, uniqueness, team QB catcher pairing, and avoidance of DST-versus-opposing-offense conflicts were checked in code.
- **Pushed:** model script, 13-lineup candidate CSV, Monte Carlo outputs, the versioned selection and this analysis.
- **Not verified:** actual DraftKings salary download and player IDs, entry acceptance, final inactives, opponent field/ownership simulation, statistical calibration, any cash/first-place projection.
