# Week 5 — $12 single entry, 4,000–6,000 entries

**Active scope: one lineup for a target field of 4,000–6,000 entries, interpreted from the user’s “4-6k contest” request.** Entry fee: $12. Exact contest identity, payout structure and official salary export remain unverified. The field range informs analyst construction preferences; it is not an input to a calibrated tournament model.

## Current recommendation — $49,900

See [the lineup and decision record](recommendation.md) and [the reproducible roster](recommended_lineup.csv). Select **Brissett / Brown / Judkins / St. Brown / Michael Wilson / Odunze / Schultz / McBride / Chargers DST**. This provisional build uses an Arizona double stack with St. Brown returning from Detroit, and holds Warren and Emanuel Wilson pending backfield clarity. The earlier comparisons below remain research baselines. No entry has been submitted.

## Decision approach

Choose one complete lineup after checking workload, salary and correlated scoring paths. Accept strong popular players. Do not sacrifice role quality merely to lower ownership, force an opposing player into a stack, or assume a single-entry tournament should be played like a cash contest. Winning upside still matters; the right balance depends on the actual field and payout curve.

The present tool compares expected points and workload stresses. It does not estimate cash probability, tournament win probability, ownership-adjusted value or expected payout. None of the estimates below are a fantasy-point floor.

## Earlier single-entry screen

Hold Tinsley and Meyers pending confirmation of replacement receiving roles. Hold Diggs pending clarification after consecutive missed practices. Hold Bagent until the starter is confirmed. These holds are **research choices**, not claims that the players are inactive. Consequently, Daniels and Burrow stack families are deferred in this pass: the saved pool does not contain an adequately verified alternative pass catcher for either. They can return as the pool and injury evidence improve.

Current evidence: [Bengals](https://www.bengals.com/team/injury-report/) list Chase limited and Higgins DNP Thursday; [Washington](https://www.commanders.com/team/injury-report/) lists Diggs DNP and Daniels full; [Chicago](https://www.chicagobears.com/team/injury-report/) lists Caleb Williams DNP. Retrieved October 8. Published salary sources and other observations are in [the source register](../sources.md).

## Comparison results

Each row is a complete legal research roster from the same manual inputs, with the new holds. The three objectives produce nine specifications, some with identical rosters.

| QB family | Highest-mean build | Worst separate stress for that build | Joint-stress build: base / stressed |
|---|---:|---:|---:|
| Brissett | 137.08 | 132.34 | 133.45 / 131.93 |
| Maye | 135.44 | 130.70 | 132.26 / 130.75 |
| Goff | 134.91 | 130.16 | 132.28 / 130.77 |

The Brissett highest-mean roster remains the earlier $50,000 build. Its joint stressed expectation is **127.14**, because Warren, Emanuel Wilson and Brown can lose workload together. The alternative Brissett construction gives up **3.63** baseline points but improves the combined stress result by **4.79**.

### Brissett alternative with less reliance on the PIT/SEA backfield assumptions

| Slot | Player | Salary |
|---|---|---:|
| QB | Jacoby Brissett | $5,500 |
| RB | Chase Brown | $6,900 |
| RB | Jonathan Taylor | $7,800 |
| WR | DK Metcalf | $5,400 |
| WR | Michael Wilson | $6,200 |
| WR | Rome Odunze | $4,700 |
| TE | Dalton Schultz | $4,000 |
| FLEX | Trey McBride | $6,700 |
| DST | Browns | $2,800 |
| **Total** | | **$50,000** |

This is a **comparison candidate**, not a new lock. It concentrates on Arizona passing production and does not include an opposing Detroit player. That is permitted by the search. Its full-game concentration and two-TE allocation need review, and its apparent resilience partly reflects which stresses were chosen.

Specifically, the scenario set tests PIT/SEA/CIN workload changes but does not symmetrically stress every player's role or a failed Arizona passing environment. This can favor Brissett and the Arizona receivers. A 1–2-point advantage between families is too small to treat as established superiority under these manual priors. There is no new evidence here that Brissett is a better real-world quarterback play than Maye or Goff.

## Remaining checks before entry

1. The user supplied a 4,000–6,000-entry target. Match the exact $12 contest to its prize curve and game set; import its salary export.
2. Recheck [Dowdle](https://www.steelers.com/team/injury-report/) and [Charbonnet](https://www.seahawks.com/team/injury-report/). Limited practice does not establish game availability or projected workload.
3. Replace the manual workload priors with documented recent usage, then test comparable target/attempt and TD uncertainty across all three QB families.
4. Reopen Cincinnati and Washington stacks when their receiving roles are adequately supported. Check weather and final inactives before freezing the entry.

These steps are prerequisites for a stronger recommendation, not work represented as already completed. No large-field multi-entry portfolio or Millionaire-specific recommendation is part of this active scope.

## Reproduce

Run `python run_single_entry.py` for the earlier comparison and `python run_single_entry_field.py` for the current recommendation, from the repository root. `profile.json` records the contest scope and temporary holds; `comparison.csv` and `lineups.csv` contain the results; `manifest.json` records their input/code hashes. All salaries remain published references pending contest verification.
