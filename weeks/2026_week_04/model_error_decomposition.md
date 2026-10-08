# 2026 Week 4 — Model Error Decomposition

> **October 8 audit correction:** The sample below combines different projection snapshots and covers only selected players. A small net stack error does not establish calibration, and injury exclusion cannot identify injury-free performance. See the [reproducibility audit](audit_2026-10-08/README.md) for reconciled outputs, missing inputs and corrections to these interpretations. The original narrative remains below as research history.

**Slate date:** October 4, 2026  
**Purpose:** Extend the post-slate review from narrative results into a quantitative diagnosis of what the model got right, what it got wrong, and what should change in the projection/simulation architecture.

## Executive finding

The strongest Week 4 lesson is that the **game-environment thesis was materially better calibrated than the player-level allocation of fantasy points inside that environment**.

For the core JAX-CIN construction, the committed pre-slate model projections available in the repository were:

| Player | Pre-slate projection | Actual DK points | Error |
|---|---:|---:|---:|
| Joe Burrow | 19.81 | 28.72 | +8.91 |
| Ja'Marr Chase | 15.41 | 5.70 | -9.71 |
| Tee Higgins | 14.35 | 29.70 | +15.35 |
| Parker Washington | 15.42 | 2.00 | -13.42 |
| **Combined** | **64.98** | **66.12** | **+1.14** |

The combined stack was only **1.14 DK points above projection**, even though the player-level errors were extremely large.

This is important.

It suggests the model was directionally correct that JAX-CIN was the slate's best environment, but was too confident about **which players inside the game would capture the production**.

That is a different problem from simply "the projection was bad."

## 1. Aggregate calibration versus allocation error

The model can be approximately right at the game or stack level while still being wrong at the player level.

Week 4 is a clean example:

- Burrow exceeded his pre-slate projection by about **8.9 points**.
- Higgins exceeded his projection by about **15.4 points**.
- Chase fell about **9.7 points below projection**, primarily because of the concussion.
- Parker Washington fell about **13.4 points below projection**.

The four-player absolute-error total was about **47.4 DK points**, despite the combined stack total missing by only about **1.1 points**.

### Interpretation

The model currently treats player means and volatility as the main simulation objects.

A better architecture should explicitly separate:

1. **game scoring environment**,  
2. **team offensive production**,  
3. **how that production is allocated among teammates**, and  
4. **player-specific injury / role / efficiency variance**.

This would allow the model to represent a slate where the Cincinnati passing game hits, but Higgins captures far more of the production than Chase.

## 2. Injury variance must be modeled separately from projection error

Ja'Marr Chase scored 5.70 DK points after leaving with a concussion.

That should not be treated like a normal model miss.

A post-slate calibration table should therefore use at least two error classes:

- **football/model error** — workload, efficiency, touchdown allocation, game script;
- **exogenous availability error** — in-game injury, ejection, weather interruption, etc.

Without that split, the model can appear less accurate than the underlying football assumptions actually were.

### Recommended change

Add fields to the weekly actual-results workflow:

```text
availability_status
injury_exit
injury_quarter
model_error_ex_injury
```

The goal is not to erase bad outcomes. It is to avoid retraining the model as though an in-game concussion were evidence that the pregame target-share estimate was systematically too high.

## 3. Parker Washington is the clearest repeatable-process miss

Parker Washington is more useful for model improvement than Chase because his miss was not primarily injury-driven.

Pre-slate projection:

```text
15.42 DK points
```

Actual:

```text
2.00 DK points
```

Error:

```text
-13.42 DK points
```

The model correctly identified JAX-CIN as a high-upside environment, but the bring-back allocation failed.

### Research question

Was Parker's projection driven by:

- too many expected targets,
- too high a route participation assumption,
- too much touchdown expectation,
- insufficient uncertainty around Jacksonville target distribution,
- or an incorrect assumption that a high-scoring game would necessarily funnel production through him?

Future projections should expose those assumptions explicitly rather than hiding them inside a single mean fantasy score.

## 4. Stable-role one-offs were easier to calibrate

James Cook is a useful contrast.

Pre-slate model projection:

```text
16.72 DK points
```

Actual:

```text
16.30 DK points
```

Error:

```text
-0.42 DK points
```

This does not prove the model is generally excellent on running backs, but it supports a useful hypothesis:

> Stable, established workloads may be easier to project than target-share allocation among multiple pass catchers in correlated game stacks.

That hypothesis should be tested across future weeks.

## 5. Lineup simulation was directionally useful

The raw-ceiling single-entry lineup had:

```text
Simulated mean: 130.6
P95:            178.7
Actual:         153.62
```

The actual score was:

```text
+23.02 points above simulated mean
```

but still below the simulated P95.

The ownership-adjusted single-entry lineup had:

```text
Simulated mean: 126.9
P95:            176.4
Actual:         137.52
```

The actual result was:

```text
+10.62 points above simulated mean
```

Again, the realized outcome was comfortably inside the modeled upper range.

### Interpretation

The upper-tail framework was more informative than raw mean projection alone.

However, Week 4 also shows that the simulator needs better **within-game allocation dependence**. A single game factor is not enough if all pass catchers receive production independently after the game environment is set.

## 6. Counterfactual injury sensitivity

The $50 SE / Milly lineup scored:

```text
153.62 DK points
```

If Chase had merely scored his pre-slate mean projection instead of 5.70:

```text
153.62 - 5.70 + 15.41 = 163.33
```

If Chase had reached the model ceiling of roughly 25.65:

```text
153.62 - 5.70 + 25.65 = 173.57
```

This is not a claim about what would have happened without the injury.

It is a sensitivity check showing that the lineup's tournament path remained live before the injury variance.

The more repeatable process concern remains the Parker Washington allocation and the decision to use the same lineup in contests with very different field sizes.

## 7. Portfolio construction was a separate error source

The $50 SE and $20 Millionaire used the same lineup.

That means the portfolio concentrated:

- the same primary game environment,
- the same Cincinnati stack,
- the same Jacksonville bring-back,
- the same injury-created values,
- and the same one-off ceiling bets

across two contests with very different payout structures.

This is not a projection problem.

It is a **portfolio-objective problem**.

Future lineup selection should optimize separately for:

### Single entry

- strong median,
- strong P90/P95,
- coherent correlation,
- modest leverage,
- lower duplication concern.

### Large-field GPP

- P99 / first-place path,
- stronger leverage,
- lower lineup duplication,
- willingness to sacrifice some median projection,
- alternate slate stories.

## 8. Recommended model architecture

Week 4 suggests moving toward a hierarchical simulation.

### Layer 1 — Game environment

Simulate:

- total plays,
- game pace,
- scoring environment,
- pass/rush balance,
- competitiveness / blowout state.

### Layer 2 — Team production

Conditional on the game:

- pass attempts,
- completions,
- passing yards,
- passing TDs,
- rush attempts,
- rushing yards,
- rushing TDs.

### Layer 3 — Player allocation

Distribute team opportunities with uncertainty:

- target share,
- reception share,
- air-yard share,
- red-zone share,
- carry share,
- touchdown share.

A Dirichlet-style share model or correlated logistic-normal share model would be more realistic than simulating each receiver independently.

### Layer 4 — Player efficiency

Conditional on volume:

- catch rate,
- yards per reception,
- yards per carry,
- touchdown conversion.

### Layer 5 — Availability shock

Separate low-probability events:

- in-game injury,
- ejection,
- sudden role loss.

These should be tracked separately from ordinary football variance.

## 9. New diagnostics to calculate every week

Starting with future slates, save:

| Diagnostic | Purpose |
|---|---|
| player projection error | Basic calibration |
| absolute error | Magnitude of miss |
| error excluding injury exits | Cleaner football calibration |
| stack-level projected vs actual points | Test environment thesis |
| within-stack allocation error | Test target/TD distribution |
| projected vs actual team pass volume | Volume calibration |
| projected vs actual targets/carries | Role calibration |
| projected vs actual ownership | Leverage calibration |
| lineup mean/P90/P95 vs actual | Simulation calibration |
| contest-specific lineup overlap | Portfolio concentration |

## 10. Week 5+ implementation priorities

1. **Build a forecast-error table automatically after every slate.**
2. **Track injury exits separately from ordinary model error.**
3. **Add stack-level calibration metrics.**
4. **Model target/carry shares as distributions, not fixed point estimates.**
5. **Replace independent player simulation with hierarchical game/team/player simulation.**
6. **Estimate lineup-level duplication rather than only individual ownership.**
7. **Select lineups using contest-specific objective functions.**
8. **Commit exact entered lineups before lock.**

## Bottom line

Week 4 did not show that the game-environment process failed.

It showed something more specific:

> The model was close on the total fantasy production of the core JAX-CIN stack, but too uncertain and too poorly structured in how that production was distributed across individual players.

That is a productive failure because it points directly to the next modeling improvement.

The next version should become better at answering:

```text
If this game hits, WHO captures the points?
```

rather than only:

```text
Will this game hit?
```

