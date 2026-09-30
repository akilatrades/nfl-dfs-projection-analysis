# NFL DFS Projection Analysis

An ongoing NFL DraftKings research project focused on projection quality, lineup construction, ownership, correlation, leverage, and post-slate review.

The goal is to treat each slate as a forecasting and decision-analysis problem:

```text
public player/team data
    ->
our projection model
    ->
our ownership estimate
    ->
lineup decisions
    ->
actual results
    ->
error analysis
    ->
updated process
```

The project is not built around posting winning or losing lineups. The focus is whether the **decision process** was sound, where the projections were wrong, where lineup construction reduced ceiling, and what should change on the next slate.

## What these lineups are for

The lineups in this project are built for **NFL DraftKings Daily Fantasy Sports (DFS) contests**.

In DFS, a user does not draft one season-long team. Instead, a new lineup is created for a specific group of NFL games, called a **slate**.

For the type of DraftKings lineup used in this project, the lineup contains:

```text
1 Quarterback (QB)
2 Running Backs (RB)
3 Wide Receivers (WR)
1 Tight End (TE)
1 FLEX
1 Defense / Special Teams (DST)
```

The **FLEX** spot can be filled by an RB, WR, or TE.

Each player has a salary. The lineup must stay under the contest salary cap. The Week 3 lineup used the full **$50,000 salary cap**.

DraftKings awards fantasy points based on what the selected players do in the actual NFL games. The lineup competes against other lineups entered into the same contest.

This project is currently focused on **single-entry tournament analysis**.

A **single-entry** contest allows each participant to enter only one lineup. A **tournament** pays based on finishing position, so the goal is not only to build a lineup with a solid average projection. The lineup also needs enough upside to finish near the top of the field.

That is why this project studies more than one expected fantasy-point number. It also looks at:

- player ceiling,
- lineup correlation,
- our ownership estimate,
- leverage,
- game environment,
- salary allocation,
- late news,
- and post-slate projection error.

The exact DraftKings scoring and contest rules can vary by contest, so the contest page should always be treated as the final source for live rules.

## How to read this project

The project is designed to be followed in this order:

```text
README
  ->
understand the contest and the terms
  ->
review the weekly pre-slate decisions
  ->
review the actual results
  ->
measure projection and ownership errors
  ->
document what should change next week
```

Each week is another observation in the same ongoing research project. The goal is to improve the process over time instead of treating every slate as an isolated win or loss.

## Our projection model

This repository now generates its **own fantasy-point projections**.

The model begins with football assumptions that we can see, explain, change, and later test.

For an offensive player, the basic process is:

```text
expected opportunity
    ->
expected efficiency
    ->
expected football statistics
    ->
DraftKings fantasy points
```

### Example: wide receiver

Suppose we estimate:

```text
8 targets
65% catch rate
12 yards per reception
0.40 expected receiving touchdowns
```

The model first estimates receptions:

```text
8 targets × 65%
= 5.2 receptions
```

Then receiving yards:

```text
5.2 receptions × 12 yards
= 62.4 receiving yards
```

The touchdown input can be fractional because it represents an **expected value**. A projection of 0.40 receiving touchdowns does not mean the player will score 0.40 touchdowns in a real game. It means the model is treating the player's touchdown expectation as 0.40 before the game is played.

Those expected statistics are then converted into DraftKings fantasy points.

### How the fantasy-point conversion works

The first version of the model uses the standard DraftKings NFL scoring structure for offensive players:

| Event | DraftKings points used by the model |
|---|---:|
| Passing yard | 0.04 |
| Passing touchdown | 4 |
| Interception thrown | -1 |
| Rushing yard | 0.10 |
| Rushing touchdown | 6 |
| Reception | 1 |
| Receiving yard | 0.10 |
| Receiving touchdown | 6 |
| Fumble lost | -1 |
| Two-point conversion | 2 |
| 300+ passing yards | +3 bonus |
| 100+ rushing yards | +3 bonus |
| 100+ receiving yards | +3 bonus |

For the yardage bonuses, the model uses a **probability** rather than automatically awarding the bonus from the mean projection.

Example:

```text
Probability of 100+ receiving yards = 20%
Bonus value = 3 points

Expected bonus contribution:
20% × 3
= 0.6 projected points
```

That is more realistic than giving a full three-point bonus simply because a player's average projection happens to be near 100 yards.

DST uses expected sacks, turnovers, touchdowns, safeties, blocks, and an expected points-allowed scoring value.

DraftKings scoring reference used for the model:
https://dknetwork.draftkings.com/2025/08/27/nfl-dfs-beginners-guide-draftkings/

### What goes into our projections

Depending on position, the model can use:

- expected pass attempts,
- completion rate,
- yards per completion,
- expected passing touchdowns,
- expected interceptions,
- expected carries,
- yards per carry,
- expected rushing touchdowns,
- expected targets,
- catch rate,
- yards per reception,
- expected receiving touchdowns,
- recent fantasy-point volatility,
- and the probability of reaching DraftKings yardage bonuses.

The inputs are built from public football information and our own assumptions.

The important part is that every projected point can be traced back to an assumption.

If a projection looks wrong, we can ask:

> Was the expected volume wrong, was the efficiency assumption wrong, or was the scoring conversion wrong?

That gives us something we can actually improve.

### Projection, floor, and ceiling

The model produces three main numbers:

**Model projection**  
Our expected DraftKings score based on the stat assumptions.

**Model floor**  
A lower-end estimate based on the player's recent fantasy-point volatility.

**Model ceiling**  
A higher-end estimate based on the same volatility.

The first version uses a simple statistical range around the projection. As more weeks are collected, this can be replaced with a full player-outcome simulation.

### Our ownership estimate

Ownership is also treated as **our estimate**, not as a number that is assumed to be correct.

Before lock, we estimate how popular a player may be based on factors such as:

- salary,
- our projection,
- our value calculation,
- our ceiling,
- game environment,
- position alternatives,
- role changes,
- and late news.

After the slate, we compare our estimate with the player's actual contest ownership.

That creates another forecast we can measure and improve.

## Current research questions

The project tracks questions such as:

1. How accurate are our model projections compared with actual DraftKings scoring?
2. How accurate are our ownership estimates?
3. Does salary efficiency lead to strong tournament lineups, or can it sacrifice ceiling?
4. How much does lineup correlation matter in single-entry tournaments?
5. When does leverage improve a lineup, and when is it being forced?
6. How should late injury/news updates change projections without creating false certainty?
7. Which types of mistakes are model errors, and which are normal variance?

## Lineup construction process

The Week 3 review led to a revised order of operations:

```text
1. Identify strong game environments
2. Build for correlated ceiling
3. Use projections to compare players
4. Evaluate ownership
5. Add only 1-2 deliberate leverage decisions
6. Check whether the complete lineup has enough upside
```

This order matters.

A lineup should not begin with "Who is the best point-per-dollar play?" and then fill eight remaining positions independently. Tournament scoring is driven by the combined ceiling of the lineup and by how those players can succeed together.

## Week 3 case study

The first documented case study is the 2026 Week 3 $50 single-entry lineup:

| Position | Player |
|---|---|
| QB | Tyler Shough |
| RB | Kenneth Walker III |
| RB | Jaylen Warren |
| WR | Amon-Ra St. Brown |
| WR | Jalen Coker |
| WR | Devaughn Vele |
| TE | Dalton Schultz |
| FLEX | Breece Hall |
| DST | Vikings DST |

Salary used: **$50,000**

The post-slate review found several process issues:

- Tyler Shough was selected mainly for salary efficiency instead of prioritizing a higher-ceiling game environment.
- The lineup did not contain enough meaningful correlation.
- The late-news upgrade on Jalen Coker was treated too aggressively; more opportunity did not guarantee concentrated target volume.
- Breece Hall was used as leverage, but the leverage case was stronger than the ceiling case.
- Devaughn Vele and Dalton Schultz helped make the salary work but lowered the lineup's overall tournament ceiling.
- Kenneth Walker III, Jaylen Warren, and Amon-Ra St. Brown were stronger parts of the process.
- A Lawrence/Parker construction had been identified before lock as a stronger game-environment thesis, but it was not the lineup ultimately entered.

See [Week 3 review](weeks/2026_week_03/README.md) for the full case study.

## Week 4 pre-slate workflow

Week 4 is the first slate where the revised process is being used **before** lineup lock.

The pre-slate work is stored in:

**[Week 4 pre-slate analysis](weeks/2026_week_04/pre_slate_analysis.md)**

The Week 4 files are designed to answer four questions before the result is known:

1. Which games offer the strongest fantasy environments?
2. Which player combinations provide useful correlation?
3. Where can we gain ownership leverage without giving up too much ceiling?
4. Why is the final lineup different from the field?

The Week 4 folder also contains:

- `game_environments.csv` — ranks the games before individual players are selected.
- `projection_inputs.csv` — stores the football assumptions used to create our projections.
- `player_pool.csv` — stores our model projection, floor, ceiling, value, ownership estimate, role, and decision notes.
- `lineup_candidates.csv` — compares possible single-entry constructions.
- `final_lineup.csv` — records the final pre-lock lineup and the reason for each roster spot.

The goal is to record the decision process first and judge the outcome second.

## What will be stored each week

Before lock, the project can store:

| Field | Meaning |
|---|---|
| Player | Player name |
| Position | DraftKings roster position |
| Salary | DraftKings salary |
| Model projection | Our expected DraftKings points calculated from the projection inputs |
| Model ceiling | Our higher-end scoring estimate |
| Our ownership estimate | Our pre-lock estimate of expected field ownership |
| Team total | Expected team scoring environment |
| Game total | Expected combined game scoring |
| Role notes | Expected snaps, routes, carries, targets, etc. |
| Correlation notes | Which lineup pieces can succeed together |
| Decision | Play, fade, neutral, or lineup-specific use |
| Reason | Why the decision was made before results were known |

After the slate, the project can add:

| Field | Meaning |
|---|---|
| Actual DK points | Final DraftKings fantasy score |
| Actual ownership | Contest ownership |
| Projection error | Actual points minus our model projection |
| Ownership error | Actual ownership minus our ownership estimate |
| Ceiling hit | Whether the player reached our defined ceiling range |
| Process grade | Whether the original reasoning was supported by the information available before lock |
| Review notes | What should change next time |

The goal is to preserve the distinction between a **bad result** and a **bad decision**.

A strong decision can lose because NFL outcomes are volatile. A weak decision can also win. The review process should judge the information and logic that existed before the slate, then separately measure the actual outcome.

## Project structure

```text
nfl-dfs-projection-analysis/
├── README.md
├── data/
│   └── README.md
├── src/
│   ├── projections.py
│   └── evaluation.py
├── run_projections.py
├── weeks/
│   ├── 2026_week_03/
│   │   ├── README.md
│   │   └── lineup.csv
│   └── 2026_week_04/
│       ├── pre_slate_analysis.md
│       ├── game_environments.csv
│       ├── projection_inputs.csv
│       ├── player_pool.csv
│       ├── lineup_candidates.csv
│       └── final_lineup.csv
└── requirements.txt
```

Each new slate is added to the same project. The methods, definitions, and evaluation code are updated as the research develops.

## Glossary

<details>
<summary><strong>Open glossary</strong></summary>

| Term | Plain-English meaning |
|---|---|
| DFS | Daily Fantasy Sports. A new fantasy lineup is built for a specific slate of games rather than for an entire season. |
| Slate | The group of NFL games included in a particular DraftKings contest. |
| Contest | The DraftKings competition the lineup is entered into. |
| Lineup | The group of players selected for one contest entry. |
| Salary | The DraftKings cost assigned to a player. |
| Salary cap | The maximum combined salary allowed for the lineup. The Week 3 lineup used a $50,000 cap. |
| QB | Quarterback. One QB is used in the lineup format tracked here. |
| RB | Running back. Two RB spots are used. |
| WR | Wide receiver. Three WR spots are used. |
| TE | Tight end. One TE spot is used. |
| FLEX | A flexible roster spot that can be filled by an RB, WR, or TE. |
| DST | Defense / Special Teams. This roster spot uses an NFL team's defense and special-teams unit. |
| Single Entry (SE) | A contest where each participant can enter only one lineup. |
| Tournament / GPP | A contest where payouts depend on finishing position. High finishes matter much more than simply being above average. GPP is a common DFS term for this type of prize-pool tournament. |
| Cash game | A contest where a larger share of the field is paid and the goal is more about beating a cutoff than finishing first. This project is focused on tournaments, not cash-game lineup building. |
| Field | All of the other lineups entered into the same contest. |
| Model projection | The DraftKings score produced by our own stat-based projection model. |
| Expected value | The average result implied by the model before the game is played. This can include fractional values, such as 0.40 expected touchdowns. |
| Projection input | A football assumption used by our model, such as targets, carries, catch rate, or expected touchdowns. |
| Ceiling | A higher-end scoring outcome. Tournament lineups need enough players capable of scoring well above their median expectation. |
| Floor | A lower-end estimate of what a player may score if the game does not go well. |
| Ownership | The percentage of contest lineups that roster a player. Before lock, this has to be estimated. |
| Our ownership estimate | Our pre-lock forecast of how popular a player will be in the contest. |
| Actual ownership | The percentage of the real contest field that ultimately rostered a player. |
| Chalk | A player expected to be highly owned. |
| Leverage | A lower-owned player or construction that can gain ground on the field if a popular alternative fails, provided the lower-owned option still has enough upside. |
| Correlation | The relationship between fantasy outcomes. Two players are positively correlated when the same football events can help both score. |
| Stack | A lineup construction that intentionally combines correlated players, often a quarterback with one or more pass catchers. |
| Bring-back | An opposing player added to a stack because a high-scoring, competitive game can benefit both teams. |
| Game environment | The overall fantasy setup of one NFL game, including scoring expectations, pace, player roles, and how likely the game is to stay competitive. |
| Value | Projected fantasy points relative to salary. A player can be good value without necessarily having enough tournament ceiling. |
| Point-per-dollar | A simple way to compare projected fantasy production with salary. It is useful, but tournament decisions should not rely on it alone. |
| Salary efficiency | Another way to describe how much projected production a lineup gets for the salary spent. |
| Late news | Injury, inactive, depth-chart, or role information that becomes available close to lineup lock. |
| Target | A pass thrown toward a specific receiver. |
| Target share | The percentage of a team's pass attempts directed at a player. |
| Route | A pass pattern run by a receiver on a passing play. More routes usually create more chances to earn targets. |
| Red-zone opportunity | A carry or target near the opponent's goal line, where touchdowns are more likely. |
| Lineup lock | The point when a contest or player can no longer be changed under the contest rules. |
| Projection error | Actual DraftKings points minus projected DraftKings points. |
| Ownership error | Actual ownership minus our pre-lock ownership estimate. |
| MAE | Mean Absolute Error. The average size of projection misses without caring whether the projection was too high or too low. |
| RMSE | Root Mean Squared Error. A projection-error measure that gives larger misses more weight. |
| Variance | Natural uncertainty in outcomes. A good decision can still have a bad result because NFL performance is volatile. |
| Process | The information and reasoning used before the result was known. |
| Outcome | What actually happened after the games were played. A good outcome does not automatically mean the process was good, and a bad outcome does not automatically mean the process was bad. |

</details>

## Data and model inputs

The project is built around **our own projections**.

The repository can use public information such as:

- NFL box scores and game logs,
- player usage,
- team play volume,
- targets and carries,
- snap and route information when available,
- DraftKings salaries,
- game totals and team totals,
- injury and inactive news,
- and actual contest results after the slate.

These inputs are converted into our own expected stat lines and our own DraftKings projections.

The repository should store the assumptions that created a projection whenever possible. That makes the model auditable: another person can see why a player projected the way he did instead of seeing only a final fantasy-point number.

## Planned analysis

As more slates are added, the project can calculate:

- mean absolute projection error,
- root mean squared projection error,
- projection error by position,
- ownership calibration,
- ceiling-hit rate,
- chalk performance,
- leverage performance,
- stack performance,
- game-environment performance,
- salary efficiency versus actual ceiling,
- results before and after late-news adjustments.

Eventually, the project can replace the first simple projection ranges with full outcome simulations, build an ownership model from our historical contest data, and test whether each version of our model improves out-of-sample.

Educational and analytical use only.
