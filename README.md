# NFL DFS Projection Analysis

An ongoing NFL DraftKings research project focused on projection quality, lineup construction, ownership, correlation, leverage, and post-slate review.

The goal is to treat each slate as a forecasting and decision-analysis problem:

```text
player data
    ->
projections and ownership expectations
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

That is why this project studies more than raw projections. It also looks at:

- player ceiling,
- lineup correlation,
- projected ownership,
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

## Current research questions

The project tracks questions such as:

1. How accurate are player projections compared with actual DraftKings scoring?
2. How accurate are ownership projections?
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

## What will be stored each week

Before lock, the project can store:

| Field | Meaning |
|---|---|
| Player | Player name |
| Position | DraftKings roster position |
| Salary | DraftKings salary |
| Projection | Expected DK points |
| Ceiling | Higher-end projected outcome |
| Projected ownership | Expected field ownership |
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
| Projection error | Actual points minus projected points |
| Ownership error | Actual ownership minus projected ownership |
| Ceiling hit | Whether the player reached the defined ceiling range |
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
│   └── evaluation.py
├── weeks/
│   └── 2026_week_03/
│       ├── README.md
│       └── lineup.csv
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
| Projection | An estimate of how many DraftKings points a player is expected to score. |
| Median projection | A central or middle expected outcome. It is useful, but it does not describe the player's full range of possible scores. |
| Ceiling | A higher-end scoring outcome. Tournament lineups need enough players capable of scoring well above their median expectation. |
| Floor | A lower-end estimate of what a player may score if the game does not go well. |
| Ownership | The percentage of contest lineups expected to roster a player. |
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
| Ownership error | Actual ownership minus projected ownership. |
| MAE | Mean Absolute Error. The average size of projection misses without caring whether the projection was too high or too low. |
| RMSE | Root Mean Squared Error. A projection-error measure that gives larger misses more weight. |
| Variance | Natural uncertainty in outcomes. A good decision can still have a bad result because NFL performance is volatile. |
| Process | The information and reasoning used before the result was known. |
| Outcome | What actually happened after the games were played. A good outcome does not automatically mean the process was good, and a bad outcome does not automatically mean the process was bad. |

</details>

## Data policy

Paid projection files from third-party DFS services should not be redistributed in this repository.

The project can use:

- public NFL data,
- DraftKings salary data where redistribution is permitted,
- manually entered personal projections,
- derived statistics,
- model outputs,
- lineup decisions,
- post-slate results,
- aggregated error metrics.

If a paid projection service is used as an input, the repository should store only calculations or conclusions that can be shared without reproducing the provider's proprietary dataset.

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

Eventually, the project can compare outside projections with an independently built blended projection model.

Educational and analytical use only.
