# Week 10 — November 15, 2026 single-entry research

## Decision

Two $12 DraftKings Classic Sunday-main recommendations, one for each contest. Plan against the advertised capacities, not presumed overlay. These are recommendations, not a claim of submitted entries.

| Slot | $60K Fair Catch — 5,882 maximum | Salary | $125K Fair Catch — 12,254 maximum | Salary |
|---|---|---:|---|---:|
| QB | Tyler Shough | 5600 | Dak Prescott | 6400 |
| RB | Chuba Hubbard | 7200 | Bijan Robinson | 8200 |
| RB | Emmett Johnson | 4700 | Emmett Johnson | 4700 |
| WR | Chris Olave | 7000 | George Pickens | 6300 |
| WR | Justin Jefferson | 6800 | Jakobi Meyers | 4200 |
| WR | Drake London | 6600 | Wan'Dale Robinson | 4500 |
| TE | Tyler Warren | 4400 | Tyler Warren | 4400 |
| FLEX | Travis Kelce | 4700 | CeeDee Lamb | 8800 |
| DST | Colts | 3000 | Browns | 2500 |
| Total | | **50000** | | **50000** |

Base additive forecasts are **143.435** and **137.810** DK points. Decimal precision describes arithmetic, not forecast confidence. The latest-starting Dallas receiver is placed at FLEX to preserve late swap choices. The Shough entry is entirely in the early window.

| Conditional score model, separate 200K-draw seed | Shough entry | Dak entry |
|---|---:|---:|
| Simulated mean | 143.47 | 137.76 |
| 10th percentile | 103.67 | 98.35 |
| 95th percentile | 202.47 | 196.77 |
| 99th percentile | 235.01 | 230.61 |
| Probability of 200+ **model score** | 5.62% | 4.33% |

These are full-game-conditional scenario outputs, not measured future percentiles or contest win probabilities. The larger-field lineup surrenders 5.6 additive points for a distinct Dallas double-stack outcome. The simulations do **not** establish that this tradeoff maximizes real payout EV. It is a contest/portfolio judgment with explicit uncertainty.

The screenshot showed 10,879/12,254 and 5,245/5,882 entered, respectively. Both are substantial tournament fields. The larger-field construction deliberately uses a different passing-TD allocation thesis; this is not a cash-game recommendation.

## Why these constructions

**Shough–Olave with Chuba:** NO-CAR has a working total of 48.5, a close spread and an indoor venue. Published role research supports fast pace and substantial passing volume. Olave's established target share is a better basis than guessing that every newly available target flows to a cheap replacement. Carolina's official inactive report leaves practice-squad corners starting, strengthening the matchup while New Orleans' OL losses remain a real risk. Chuba supplies a credible opposing workload rather than a mandatory weak run-back.

**London–Emmett–Kelce secondary game exposure:** This entry also needs productive KC-ATL scoring. London is an established target earner, Emmett has a documented Walker-out opportunity, and Kelce supplies receiving upside without requiring Mahomes to be the lineup QB. Emmett rushing TDs and Kelce receiving TDs can coexist, but they still compete for team scoring. This is three-player game concentration, not three independent reasons the lineup is safe.

**Dak–Lamb–Pickens:** SF-DAL's 55.5 total is the strongest main-slate environment. Lamb's target role and Pickens' downfield role justify comparing a double stack. Pickens' full Friday practice/no final designation is a better current signal than club pages missing their Friday rows; Sunday afternoon actives are still required. The first-place path is Dallas throwing multiple touchdowns, principally through these receivers. Javonte dominating rushing TDs, or the 49ers controlling possession, would hurt it. A San Francisco run-back is not forced at the expense of another weak role.

**Meyers and Wan'Dale:** These are modest point forecasts at useful salaries, not claimed WR1 breakouts. Meyers has a documented target/red-zone role against Tennessee; Wan'Dale has a PPR role with Tate out. JAX-TEN adds an opposing-receiver mini-correlation. Both can fail to supply a ceiling, so Meyers is explicitly reduced in the role stress. Missing Tate targets are not automatically credited to Wan'Dale.

**Warren:** Indianapolis traded Allen and Downs, creating an opportunity change supported by official reporting. That does not guarantee Warren inherits the departed WR targets. His forecast is the median of 12.73, 13.7 and 17.4, not the most optimistic number. A 15% reduction is part of the adverse-role sensitivity.

**Defenses:** Colts face Miami's new McCord-led offense in a low-total game. Browns face a Houston offense missing Harrison and two interior OL starters in the official inactive list. Cleveland is still an underdog defense, not a safe source of points. Its selection is a football judgment over a salary-near-identical Raiders variant; a 0.095-point model difference is not meaningful evidence of superiority.

**Premium RBs and alternatives:** Bijan and CMC were both forced into searches, alongside Cook, Chuba and other credible RB choices. The final pair retains Bijan once and Chuba once. CMC-Purdy-Kittle has an attractive simulated tail but concentrates substantial salary in one QB-led offense, including returning/new receiver competition. It was compared directly with simpler Purdy-Kittle constructions. Neither CMC nor Bijan was excluded merely for being popular.

**Weak roles rejected:** The stronger additive one-TE Shough candidate uses Treadwell to fit Bijan/Chuba/Jefferson together. Treadwell's existing snaps and uncertain new target allocation make him a genuine weak link, not automatic value from the Colts' trades. The selected two-TE variant gives up roughly two mean points to replace that salary punt with more established roles. Pitts-based Dallas variants were also compared; their recent catchable-target concern is a reason not to use Pitts just to make salary fit. The selected larger-field entry uses one TE/four WRs instead.

## What actually ran

- A **102-player curated pool**, spanning all ten main-slate games and all twenty current starting quarterbacks. It excludes the Germany game, Sunday night and Monday. It is not the complete official DK salary pool.
- **414 distinct legal candidates** from integer-program searches: QB families, one/two stack partners, one/two TEs, optional/required opposing pieces, Bijan/CMC forced-in, Emmett fade, conservative-source, variance and no-thin-WR alternatives.
- **150,000 common scoring scenarios** for the candidate screen, followed by **200,000 separate-seed scoring scenarios** for the final recommendations.
- Three **75,000-draw sensitivities**: lower available forecasts, adverse workload assumptions and reduced variance. Common random numbers support comparisons; they are not three independent pieces of evidence.
- Hypothetical **5,882- and 12,254-entry field comparisons**, with **10,000 shared outcomes per field assumption**. Base and flatter popularity targets are fitted approximately; a stronger-opponent scenario requires at least 130 projected points. The first field prototype overstated Emmett exposure and was replaced before selection.
- Salary/position/unique-player/DST-conflict validation for all candidates; separate-seed mean checks and correlation checks. No external bet or DFS entry was submitted.

The mean is the median of captured SPAGS/FSC/FTN forecasts where available. With two values, the median is their midpoint. Some pool players have one forecast. Model parameters for TD rates and variance are analyst assumptions, not historically fitted estimates. Public mean forecasts include DK scoring; this is not the repository's first-principles projection engine or an exact stat-line simulator.

## Simulation mechanism and limitations

Each game and team has shared mean-one lognormal scoring factors. Team offensive-TD expectation is frozen from the market team total, with a declared 65% passing split. Team passing/rushing TD counts are allocated once to named players and an unrostered residual, leaving at least 10% of expectation outside the curated pool. The QB receives the same team passing-TD count. Non-TD points use position-specific gamma distributions with explicit zero-production events for WR/TE. DST uses a centered sack/turnover/TD approximation.

This incorporates shared team outcomes and TD allocation competition. It still approximates yards, PPR and bonuses, omits explicit interception/fumble negatives in the offense distribution and does not fit historical tail frequencies. Its apparently precise P95/P99 values are scenario outputs, not calibrated future quantiles.

The QB-failure check separately scales the QB to 15% of forecast, his WR/TE teammates to 65%, and his RB teammates to 90%. No probability is attached to that scenario. It addresses the omitted shared-downside mechanism from Week 8 without pretending the Lamar first-play thumb injury was predictable. Baseline injury frequencies/backup-QB effects remain an unimplemented calibration task.

The synthetic fields are sampled from the curated pool with declared stack/FLEX/bring-back preferences, salary restrictions and popularity inputs. Marginal exposures differ from their targets even after fitting; audits preserve that error. The stronger field is a deliberate stress, not an observation of either actual contest. First-place event counts are small and rankings change across assumptions. **Do not interpret their simulated first-place shares as actual win odds, use ownership products to assert uniqueness, or infer payout EV without the payout ladder.**

The final pair has different QBs, different main game scripts and only Emmett/Warren in common. Those two shared value roles can still sink both entries. We deliberately retain useful chalk and seek differentiation in correlated combinations rather than making every spot low owned.

## Files and reproduction

- [Exact recommendations and stresses](recommendations.json); [human-readable slots](lineups.csv), not an upload file.
- [Final role/projection inputs](inputs.json), [candidate rosters](candidates.json), [screen metrics](simulation_metrics.json), [sensitivity outputs](sensitivity_results.json).
- [Final field comparisons](recommendation_field_results.json), [field scenario follow-up](field_followup_results.json), and field audit files. Synthetic binary field arrays are generated locally from saved seeds and are not necessary to store in Git.
- [Sources](sources.md), [all prior lessons mapped to actions](lessons_applied.md), [manifest/hashes](manifest.json), [simulation verification](simulation_sanity.json).

Requires Python 3.11+ with NumPy and SciPy (including `scipy.optimize.milp`). From this directory:

```bash
python run.py --phase screen --draws 150000
python sensitivity.py
python run.py --phase field --field-draws 10000
python field_followup.py
python select.py
python verify.py
```

Recorded salary checks use published boards. Official DK draft-group/player-ID matching was unavailable (public endpoint HTTP 403), so confirm names/prices in the contest builder. Afternoon inactives and any material late-news change require a documented amendment; questions alone are not a reason to keep changing the lineup.

Main lock: **noon Central, November 15**. Dallas players start **3:25 PM Central**; their final inactive list should be checked when released around **1:55 PM Central**. Keep Lamb at FLEX. No automatic future monitoring has been set up.

## Results status

Week 7's official result and Week 8's provisional review were already in GitHub. No Week 9 DFS result is invented. For Week 10, actual entered rosters, official scores, final field sizes, ranks, payouts, ownership and the cash line remain blank until the user's contest evidence is available. Preserve these pre-lock inputs when conducting the postmortem.
