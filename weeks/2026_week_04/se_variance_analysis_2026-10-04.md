# Week 4 Sunday Single-Entry Variance Analysis

**Date:** October 4, 2026  
**Contest type:** DraftKings NFL main-slate single-entry tournament  
**Purpose:** Document the Sunday lineup-analysis process in beginner-friendly language before the slate locks.

## Why this analysis was added

Week 3 showed a specific process problem: we let cheap value influence the lineup too early.

That can create a lineup that looks efficient on a point-per-dollar basis but does not have enough connected upside to finish near the top of a tournament.

For Week 4, the order of operations was changed to:

```text
1. Confirm injuries and expected roles
2. Rank game environments
3. Choose a primary stack
4. Add strong one-off players
5. Use value only when the role is believable
6. Compare ownership and leverage
7. Compare the full lineups with variance / upper-tail analysis
8. Make only 1-2 deliberate leverage decisions
```

The important lesson is:

> We do not start by asking, "Who is cheap?"

We start by asking:

> "What football game script can realistically create a first-place DFS score?"

---

## Step 1 — Confirm the slate and late-week role changes

The Sunday pass began by checking the games that are actually on the DraftKings main slate and then reviewing the injury changes that materially affect volume.

The most important role changes for the lineup process were:

- Breece Hall out -> Braelon Allen becomes a major value candidate.
- Justin Jefferson out -> Jordan Addison becomes more attractive because his established role can absorb additional targets.
- Nico Collins returning -> Houston's passing game becomes more interesting, while Dalton Schultz's target expectation needs to be reconsidered.
- DeVonta Smith and Dallas Goedert out -> Philadelphia has available targets, but the replacement distribution is less certain.

### Why this matters

Not all injury value is equal.

A player is stronger injury-created value when:

1. he was already playing meaningful snaps,
2. his new role is easy to identify,
3. the offense is good enough to create scoring chances,
4. and the price has not fully adjusted.

That is why Braelon Allen and Jordan Addison were treated differently from a random backup receiver who might receive extra routes but still have an uncertain target share.

---

## Step 2 — Rank the games before choosing players

The existing Week 4 game-environment model ranked the strongest games as:

| Rank | Game | Baseline total | Why it matters |
|---:|---|---:|---|
| 1 | JAX @ CIN | 51.5 | Highest total and small spread; strongest two-sided stack environment |
| 2 | NE @ BUF | 48.5 | Strong Buffalo implied total; some blowout risk |
| 3 | DAL @ HOU | 47.5 | Close spread and useful two-sided passing environment |
| 3 | DEN @ SF | 47.5 | Close spread with a strong San Francisco team total |
| 5 | KC @ LV | 47.5 | Strong Kansas City scoring environment |

The Sunday discussion narrowed the single-entry focus further:

### Primary target: JAX @ CIN

This remained the first game to build around because:

- the total was the strongest on the slate,
- both teams had usable passing-game pieces,
- the game could stay competitive,
- and several stack combinations fit the salary cap.

### Main leverage alternative: DAL @ HOU

This became the most important pivot because:

- C.J. Stroud was cheaper than the expensive QB tier,
- Nico Collins was available again,
- Dallas supplied useful bring-back options,
- and the game offered a path to a high-scoring passing environment without simply copying the most obvious JAX-CIN construction.

### Secondary targets

BUF-NE and KC-LV remained useful for one-offs and alternate stacks, but they did not beat the two games above in the final Sunday single-entry comparison.

---

## Step 3 — Separate good chalk from fragile chalk

A major Week 3 lesson was that "chalk" is not automatically bad.

The better question is:

> Why is the player popular?

### Good chalk

A popular player can still be a strong tournament play when the popularity is supported by:

- a clear workload,
- a good game environment,
- a price that is too low for the role,
- and a real ceiling.

Examples from the Sunday process included:

- Braelon Allen after Breece Hall was ruled out.
- Jordan Addison after Justin Jefferson was ruled out.
- Strong Cincinnati/Jacksonville pieces in the highest-total game.

### Fragile chalk

A popular value play becomes more dangerous when the field is assuming a role that is not actually secure.

This is the type of mistake we wanted to avoid after Week 3.

The new rule is:

> Do not play a cheap replacement only because the optimizer likes the salary.

The player still needs a believable football role.

---

## Step 4 — Build complete game-stack stories

Instead of comparing isolated players, the Sunday pass created complete lineup stories.

### JAX-CIN constructions

Examples:

```text
Joe Burrow + Ja'Marr Chase + Tee Higgins
    +
Jacksonville bring-back
```

or

```text
Trevor Lawrence + Jacksonville receiver(s)
    +
Cincinnati bring-back
```

The idea is simple:

If Cincinnati throws for multiple touchdowns and Jacksonville keeps the game competitive, several players in the same lineup can reach their ceiling together.

### DAL-HOU construction

```text
C.J. Stroud + Nico Collins
    +
Dallas bring-back
```

This is a different slate story.

It does not need JAX-CIN to fail completely. It only needs DAL-HOU to exceed expectations enough to separate from the more popular construction.

---

## Step 5 — Add variance analysis

A normal projection answers:

> What score do we expect on average?

A tournament lineup needs another question:

> How often can this lineup produce an unusually high score?

That is why the Sunday pass focused on the upper tail of the lineup distribution.

### Plain-English Monte Carlo explanation

A Monte Carlo simulation repeats the same model many times with random variation.

Instead of saying:

```text
This lineup projects for 128 points.
```

we want a distribution such as:

```text
Average outcome: 128
90th percentile: 160
95th percentile: 171
99th percentile: 200+
```

That tells us much more about tournament upside.

### What P90 / P95 / P99 mean

If a lineup has:

```text
P95 = 178
```

then approximately 5% of the simulated outcomes were above 178 points.

Higher is generally better for a tournament, but it cannot be used by itself.

The lineup still needs sensible football assumptions.

---

## Step 6 — Add correlation

The previous repository baseline lineup simulation treated player outcomes as independent.

That is a useful first model, but it misses an important DFS concept.

Example:

If Joe Burrow throws a touchdown to Ja'Marr Chase:

- Burrow scores fantasy points.
- Chase scores fantasy points.
- Both players succeed from the same real football event.

Their fantasy outcomes are positively correlated.

The Sunday exploratory pass therefore treated stacks and bring-backs as connected rather than as nine fully independent players.

### Correlation types considered

The Sunday reasoning used three basic ideas:

1. **QB + pass catcher: strong positive correlation**
2. **Opposing bring-back in a shootout: smaller positive game-level correlation**
3. **Unrelated one-offs: mostly independent**

The purpose was not to pretend we knew the exact true correlation coefficient.

The purpose was to avoid a clearly unrealistic assumption that a quarterback and his receiver have nothing to do with each other.

---

## Step 7 — Compare the original four lineups

The first variance-aware comparison used the four lineup families built Saturday night.

| Candidate | Primary construction | Mean | P90 | P95 | P(170+) |
|---|---|---:|---:|---:|---:|
| A | Lawrence / Parker / Strange + Higgins | 125.3 | 156.3 | 167.4 | 4.25% |
| B | Burrow / Higgins + Parker | 128.5 | 159.9 | 171.1 | 5.37% |
| C | Stroud / Nico + CeeDee | 125.0 | 156.5 | 167.7 | 4.27% |
| D | Mahomes / Rice + Bowers | 122.7 | 151.9 | 162.5 | 2.97% |

### What changed

Before variance analysis, the Lawrence build had been the early single-entry favorite.

After comparing the upper tails, the Burrow construction moved ahead.

That is exactly why we added this step.

A lineup can look attractive by salary and median projection but still lose when the complete correlated ceiling is compared.

---

## Step 8 — Expand the candidate search

The Sunday pass then explored stronger versions of the top game environments.

### Raw-ceiling leader

```text
QB   Joe Burrow        $6,800
RB   Kyren Williams    $5,900
RB   Braelon Allen     $5,200
WR   Ja'Marr Chase     $8,100
WR   Tee Higgins       $6,100
WR   Jordan Addison    $5,300
TE   T.J. Hockenson    $3,300
FLEX Parker Washington $6,500
DST  Rams DST          $2,600

Salary: $49,800
```

Exploratory simulation snapshot:

```text
Mean:        130.6
P90:         165.3
P95:         178.7
P99:         208.5
P(150+):      20.9%
P(160+):      13.0%
P(170+):       7.8%
```

### Why it scored well

The lineup combines:

- a concentrated Burrow + Chase + Higgins stack,
- Parker Washington as the Jacksonville bring-back,
- Braelon Allen as clear injury-created value,
- Jordan Addison as another established-role injury beneficiary,
- and enough salary left for useful standalone ceiling.

This was the strongest raw upper-tail construction in the Sunday exploratory pass.

---

## Step 9 — Apply an ownership / duplication adjustment

The raw-ceiling leader also has an obvious weakness:

It is easy for other players to build.

A single-entry tournament does not require a completely unique lineup, but duplication matters when a lineup contains several obvious popular pieces.

So the Sunday pass tested a version that gives up a small amount of raw ceiling for a less obvious construction.

### Ownership-adjusted Sunday leader

```text
QB   Joe Burrow       $6,800
RB   James Cook       $7,400
RB   Braelon Allen    $5,200
WR   Ja'Marr Chase    $8,100
WR   Tee Higgins      $6,100
WR   Jordan Addison   $5,300
TE   T.J. Hockenson   $3,300
FLEX Jakobi Meyers    $5,000
DST  Rams DST         $2,600

Salary: $49,800
```

Exploratory simulation snapshot:

```text
Mean:     126.9
P95:      176.4
P(170+):    6.9%
```

### Why this lineup became the current single-entry leader

It keeps the main Cincinnati ceiling thesis:

```text
Burrow + Chase + Higgins
```

but changes the Jacksonville bring-back from the more obvious Parker Washington to Jakobi Meyers.

It also uses James Cook instead of Kyren Williams.

The important idea is not that "lower ownership is always better."

The idea is:

> Give up only a small amount of upper-tail projection when the lineup becomes meaningfully less obvious.

This is the type of leverage trade-off we want in single entry.

---

## Step 10 — Keep a major game-stack pivot

The best major alternative was the DAL-HOU build.

```text
QB   C.J. Stroud      $5,700
RB   James Cook       $7,400
RB   Chase Brown      $6,100
WR   Nico Collins     $7,200
WR   George Pickens   $6,300
WR   Jordan Addison   $5,300
TE   T.J. Hockenson   $3,300
FLEX Braelon Allen    $5,200
DST  Seahawks DST     $3,500

Salary: $50,000
```

Exploratory simulation snapshot:

```text
Mean:     128.0
P95:      173.3
P(170+):    6.1%
```

This lineup is not the current raw-ceiling leader.

Its value is strategic:

If JAX-CIN becomes extremely concentrated in the field, DAL-HOU gives us a coherent alternate route rather than random contrarian players.

---

## Current Sunday ranking

At this stage of the analysis:

1. **Burrow / Chase / Higgins + Jakobi Meyers** — preferred ownership-adjusted single-entry construction.
2. **Burrow / Chase / Higgins + Parker Washington** — highest raw simulated ceiling.
3. **Stroud / Nico Collins + George Pickens** — strongest major game-stack pivot.

This ranking can still change if Sunday inactive news materially changes a role.

---

## Important reproducibility note

The repository's committed Python statistical engine currently supports:

- player-level simulations,
- position percentiles,
- salary hit probabilities,
- leverage calculations,
- and the original independent lineup simulation workflow.

The **Sunday 100,000-run correlated lineup numbers are an exploratory analysis snapshot from the lineup work documented in this file**.

They are saved so the reasoning can be audited later, but the current repository code does **not yet fully reproduce this correlated simulation from raw player inputs**.

That is an important distinction.

We should not pretend an exploratory result is already a finished production model.

### Next model-development step

The next coding improvement should be a reproducible correlated lineup simulator that:

1. reads player means and volatility from a CSV,
2. assigns game and team factors,
3. applies QB/pass-catcher correlation,
4. applies bring-back correlation,
5. runs a fixed random seed,
6. saves the exact simulation settings,
7. and writes the lineup distribution to CSV.

Once that exists, the Sunday exploratory numbers can be regenerated directly from the repository.

---

## Final pre-lock checklist

Before submitting the actual lineup:

- [ ] Confirm official inactive lists.
- [ ] Confirm Braelon Allen's expected lead-back role.
- [ ] Confirm Nico Collins has no unexpected workload restriction.
- [ ] Confirm the Jacksonville pass-catcher roles.
- [ ] Re-check any meaningful game-total movement.
- [ ] Re-check ownership assumptions.
- [ ] Do not add a cheap value play only because a late projection jumps.
- [ ] Keep one clear primary stack.
- [ ] Use only 1-2 deliberate leverage decisions.
- [ ] Write down the final lineup before lock so the post-slate review cannot be rewritten with hindsight.

## Main lesson from the Sunday pass

The most important result is not one lineup.

It is the process change:

```text
good game environment
    ->
correlated stack
    ->
strong role-based value
    ->
upper-tail simulation
    ->
small ownership adjustment
    ->
final lineup
```

That process is much closer to the type of decision-making this project is trying to measure.
