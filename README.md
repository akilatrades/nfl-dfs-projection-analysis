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

## Current research questions

The project tracks questions such as:

1. How accurate are player projections compared with actual DraftKings scoring?
2. How accurate are ownership projections?
3. Does salary efficiency lead to strong tournament lineups, or can it sacrifice ceiling?
4. How much does lineup correlation matter in single-entry tournaments?
5. When does leverage improve a lineup, and when is it being forced?
6. How should late injury/news updates change projections without creating false certainty?
7. Which types of mistakes are model errors, and which are normal variance?

## Core terms used throughout the project

**Projection**  
An estimate of how many DraftKings points a player is expected to score.

**Ceiling**  
A player's higher-end scoring outcome. Tournament lineups need enough players capable of producing scores well above their median expectation.

**Ownership**  
The percentage of lineups in a contest expected to roster a player.

**Chalk**  
A player expected to be highly owned.

**Leverage**  
Using a lower-owned player or construction that can gain ground on the field if a popular alternative fails. Leverage is useful only when the lower-owned option still has a realistic ceiling.

**Correlation**  
The relationship between players' fantasy outcomes. For example, a quarterback and one of his pass catchers can score points together when the same passing touchdown benefits both players.

**Stack**  
A lineup construction that intentionally combines correlated players, commonly a quarterback with one or more pass catchers and sometimes an opposing player.

**Value**  
Projected fantasy points relative to salary. Value matters, but a cheap player can still be a weak tournament play if the role does not provide enough ceiling.

**Single Entry (SE)**  
A contest where each user can enter only one lineup. The project treats SE differently from large-field multi-entry tournaments because there is less need to force extreme leverage.

## Lineup construction process

The Week 3 review led to a revised order of operations:

```text
1. Identify strong game environments
2. Build for correlated ceiling
3. Use projections to compare players
4. Evaluate ownership
5. Add only 1-2 deliberate leverage decisions
6. Check the lineup as a complete portfolio of outcomes
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
