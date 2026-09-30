# 2026 Week 4 — Statistical Analysis Plan

This page explains the statistical work used for Week 4.

The goal is not to make the project look complicated. The goal is to answer a few practical questions with numbers instead of guesswork.

The analysis starts **after** our own player projections have been created.

The Week 4 workflow is:

```text
our football assumptions
    ->
our player projections
    ->
statistical player analysis
    ->
candidate lineups
    ->
final single-entry lineup
    ->
post-slate review
```

## 1. Position percentiles

Raw projections can be hard to compare across positions.

For example, an 18-point quarterback projection and an 18-point tight end projection do not mean the same thing because the player pools are different.

The project therefore calculates percentile ranks **within each position**.

Example:

```text
WR projection percentile = 90
```

means the player's projection is higher than about 90% of the wide receivers in the Week 4 player pool.

The project calculates percentiles for:

- model projection,
- model ceiling,
- value per $1,000 of salary.

### Why this helps

It makes it easier to answer:

> Is this player actually strong for his position, or does the raw number only look good by itself?

---

## 2. Salary-based hit probability

A common DFS shortcut is to talk about **3x** or **4x** salary value.

For a $6,000 player:

```text
3x target = 18 DK points
4x target = 24 DK points
```

Instead of only asking whether the projection is above or below that number, the project estimates the probability of reaching it.

The first version uses the player's:

- model projection,
- model ceiling,
- estimated scoring volatility.

Example output:

```text
Model projection: 18.0
4x target: 24.0
Probability of reaching 4x: 24%
```

That does **not** mean the player will score 24 points 24% of the time with perfect accuracy.

It means our current statistical model estimates a 24% chance based on the assumptions we supplied.

### Why this helps

Tournament lineups care about upside.

Two players can have similar average projections while one has a much better chance of producing a score that can materially help a tournament lineup.

---

## 3. Monte Carlo player simulation

The project also runs repeated random simulations of each player's fantasy outcome.

The default is:

```text
50,000 simulated outcomes per player
```

For each player, the model saves:

- simulated median,
- 75th percentile,
- 90th percentile,
- 95th percentile,
- 99th percentile.

### What a percentile means

If a player's simulated 95th-percentile score is 31 DK points, the interpretation is:

> In this model, only about 5% of simulated outcomes were above 31 points.

That gives us a fuller picture than one expected score.

### Current limitation

The first version uses a normal approximation based on the player's projection and estimated volatility.

Real NFL fantasy outcomes are not perfectly normal.

Touchdowns, injuries, game script, and role changes can create uneven distributions.

This is a baseline model that can be improved after we collect more historical data.

---

## 4. Tournament leverage index

Low ownership by itself is not useful.

A player becomes interesting when he combines:

- real upside,
- with lower expected popularity.

The project creates a simple research metric:

```text
Tournament Leverage Index
=
Probability of reaching 4x
/
Our ownership estimate
```

Example:

```text
Player A
4x probability = 30%
Ownership estimate = 20%

Leverage index = 1.5
```

Another player:

```text
Player B
4x probability = 24%
Ownership estimate = 6%

Leverage index = 4.0
```

Player B has a lower raw 4x probability, but much more upside relative to how popular we expect him to be.

### Important

This is a **project-specific metric**.

It is not an industry-standard DFS statistic.

It should not be used alone.

A player still needs a believable role, good football environment, and enough absolute ceiling.

---

## 5. Sensitivity analysis

A projection is only as good as its assumptions.

Sensitivity analysis asks:

> Which assumptions matter most?

For one player, the model can move selected inputs up and down by 10%.

Example for a wide receiver:

```text
targets
catch rate
yards per reception
receiving touchdown expectation
```

The model then recalculates the projection.

Example output:

```text
+10% targets       -> +1.8 DK points
+10% catch rate    -> +1.4 DK points
+10% yards/rec     -> +0.7 DK points
+10% TD expectation-> +0.3 DK points
```

That tells us the projection is mainly being driven by expected volume.

### Why this helps

If late news changes the player's expected targets, we immediately know whether the projection should move a little or a lot.

It also helps identify fragile projections.

A fragile projection changes dramatically when one uncertain assumption moves slightly.

---

## 6. Lineup-level simulation

Once the final lineup is created, the project can simulate the total lineup score.

The baseline lineup simulation reports:

- mean score,
- median score,
- 75th percentile,
- 90th percentile,
- 95th percentile,
- 99th percentile.

This lets us compare candidate lineups using more than total projection.

Example:

```text
Lineup A
Projection: 145
95th percentile: 185

Lineup B
Projection: 142
95th percentile: 194
```

Lineup A has the better average projection.

Lineup B has the better simulated upper tail.

For a tournament, that trade-off can matter.

### Current limitation

The first lineup simulation treats player outcomes as independent.

Real DFS players are not fully independent.

A QB and WR on the same team can benefit from the same touchdown.

An RB and his DST can benefit from the same favorable game script.

The current simulation is therefore a baseline.

A later version should estimate real historical player correlations and simulate connected outcomes together.

---

## What Week 4 will produce

After `projection_inputs.csv` is filled out, run:

```bash
python run_projections.py weeks/2026_week_04/projection_inputs.csv
```

That creates:

`player_pool.csv`

Then run:

```bash
python run_statistical_analysis.py weeks/2026_week_04/player_pool.csv
```

That creates:

`player_analysis.csv`

The main statistical fields will include:

| Field | Meaning |
|---|---|
| `projection_percentile` | How strong our projection is versus the same position |
| `ceiling_percentile` | How strong our ceiling is versus the same position |
| `value_percentile` | How strong the salary-adjusted projection is versus the same position |
| `prob_3x` | Estimated probability of reaching 3x salary value |
| `prob_4x` | Estimated probability of reaching 4x salary value |
| `tournament_leverage_index` | 4x upside relative to our ownership estimate |
| `sim_p90` | 90th-percentile simulated fantasy score |
| `sim_p95` | 95th-percentile simulated fantasy score |
| `sim_p99` | 99th-percentile simulated fantasy score |

## What we should not do

The statistical model should not become a reason to ignore football context.

A player should not enter the final lineup only because:

- his leverage index is high,
- his ownership is low,
- his 4x probability looks good,
- or his simulation has a large upper tail.

The numbers help organize the decision.

They do not replace questions such as:

- Is the player actually on the field enough?
- Is the expected workload realistic?
- Is the game environment strong?
- Is the player correlated with our stack?
- Is late news already reflected in the inputs?
- Is the model relying on an uncertain touchdown assumption?

The purpose of the statistical layer is to make the Week 4 decision process more measurable and easier to review after the slate.
