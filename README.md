# NFL DFS Projection & Decision Analysis

[![tests](https://github.com/akilatrades/nfl-dfs-projection-analysis/actions/workflows/tests.yml/badge.svg)](https://github.com/akilatrades/nfl-dfs-projection-analysis/actions/workflows/tests.yml)

Python research framework for NFL DraftKings single-entry tournament analysis. The project converts explicit football assumptions into player projections, quantifies uncertainty and ownership-related trade-offs, evaluates correlated lineup construction, and preserves pre-event decisions for post-event error analysis.

The objective is not to present individual lineups as predictive certainty. It is to build an auditable forecasting and decision process in which assumptions, model outputs, lineup choices, and realized errors can be reviewed independently.

## Analytical workflow

```text
Public football / market inputs
        |
        v
Expected opportunity and efficiency assumptions
        |
        v
Player projections
        |
        +--> Floor / ceiling estimates
        +--> Position percentiles
        +--> Salary-based hit probabilities
        +--> Ownership estimate
        +--> Sensitivity analysis
        |
        v
Game-environment and correlation analysis
        |
        v
Candidate lineup comparison
        |
        v
Pre-lock decision record
        |
        v
Actual results and post-slate error analysis
```

## Model components

| Area | Implementation |
|---|---|
| Projection engine | Converts expected passing, rushing, receiving, and DST inputs into DraftKings points |
| Uncertainty | Projection ranges plus simulation-based upper-tail summaries |
| Ownership | Transparent candidate-pool popularity estimate derived from project metrics |
| Relative strength | Position-specific projection, ceiling, and value percentiles |
| Tournament metrics | 3x / 4x hit probabilities and a project-specific leverage index |
| Sensitivity | Recalculates projections after controlled changes to key assumptions |
| Game environment | Ranks games using totals, team totals, spread, role concentration, and context |
| Lineup analysis | Evaluates salary, projection, ceiling, correlation, ownership, and lineup thesis |
| Validation | Compares pre-lock projections and ownership estimates with realized results |
| Audit trail | Stores pre-slate assumptions separately from post-slate review |

## Research design

The model starts from expected football statistics rather than importing a finished fantasy-point projection. Inputs can include pass attempts, completion rate, carries, targets, catch rate, yards per carry, yards per reception, touchdown expectations, recent volatility, and bonus probabilities.

This design keeps the projection explainable: a forecast miss can be traced back to volume, efficiency, scoring conversion, or uncertainty assumptions rather than treated as an opaque model error.

See [docs/methodology.md](docs/methodology.md) for the analytical framework and [docs/limitations.md](docs/limitations.md) for the current model-use boundary.

## Case studies

The repository keeps weekly research records so the process can be evaluated without hindsight.

- [2026 Week 3 review](weeks/2026_week_03/README.md) — initial single-entry process review and identified construction errors.
- [2026 Week 4 pre-slate analysis](weeks/2026_week_04/pre_slate_analysis.md) — assumptions and lineup thesis recorded before lock.
- [2026 Week 4 statistical analysis](weeks/2026_week_04/statistical_analysis.md) — percentile, hit-probability, simulation, and sensitivity outputs.
- [2026 Week 4 post-slate review](weeks/2026_week_04/post_slate_review_2026-10-04.md) — realized results and process evaluation.

The Week 4 correlated upper-tail work is explicitly classified as exploratory because the saved analysis is not yet fully reproduced by the repository's core Python pipeline. It is retained as research history rather than represented as a production-ready model component.

## Repository structure

```text
.
├── .github/workflows/
├── data/
├── docs/
├── src/
│   ├── evaluation.py
│   ├── game_environment.py
│   ├── input_model.py
│   ├── lineup_analysis.py
│   ├── projections.py
│   └── statistical_analysis.py
├── tests/
├── weeks/
│   ├── 2026_week_03/
│   └── 2026_week_04/
├── run_baseline_inputs.py
├── run_game_environments.py
├── run_projections.py
├── run_statistical_analysis.py
├── pyproject.toml
└── requirements.txt
```

## Reproduce the core analysis

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install pytest
pytest
python run_projections.py weeks/2026_week_04/projection_inputs.csv
python run_statistical_analysis.py weeks/2026_week_04/player_pool.csv
```

Windows activation:

```text
.venv\Scripts\activate
```

## Validation and controls

The project includes automated unit tests for projection arithmetic, value calculations, percentile logic, hit probabilities, deterministic simulation behavior, sensitivity analysis, and input validation.

Pre-slate and post-slate records are kept separate to reduce hindsight bias. Model assumptions are stored alongside outputs whenever practical, and exploratory analysis is labeled separately from reproducible production code.

## Current limitations

The current framework remains a research model. Important limitations include manually estimated football inputs, a simplified ownership model, normal / truncated-normal approximations in parts of the uncertainty layer, incomplete field-level ownership calibration, and a correlated lineup simulation layer that is not yet integrated into the core reproducible engine.

No model output should be interpreted as a guaranteed contest outcome.

Educational and analytical use only.
