# Data

This folder is for datasets used by the NFL DFS projection-analysis project.

The project separates **pre-slate information** from **post-slate results** so later review does not accidentally rewrite the original decision process using hindsight.

## Pre-slate data

Examples include:

- DraftKings salary,
- projection,
- ceiling projection,
- projected ownership,
- game total,
- team total,
- role information,
- injury/news adjustments,
- lineup correlation notes.

## Post-slate data

Examples include:

- actual DraftKings points,
- actual ownership,
- final player usage,
- projection error,
- ownership error,
- contest result.

## Recommended player-level columns

```text
season
week
player
position
team
opponent
salary
projection
ceiling
projected_ownership
actual_points
actual_ownership
game_total
team_total
pre_slate_role_note
decision
decision_reason
```

The project can grow this schema as additional data becomes available.

## Proprietary projection data

Do not commit full paid projection spreadsheets from third-party DFS services unless redistribution is explicitly permitted.

Derived calculations, personal notes, model outputs, and manually entered decision variables can be stored without reproducing the original proprietary file.
