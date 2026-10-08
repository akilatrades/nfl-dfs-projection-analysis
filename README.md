# NFL DFS Projection & Decision Analysis

[![tests](https://github.com/akilatrades/nfl-dfs-projection-analysis/actions/workflows/tests.yml/badge.svg)](https://github.com/akilatrades/nfl-dfs-projection-analysis/actions/workflows/tests.yml)

Can explicit assumptions about opportunity, scoring and lineup correlation improve an NFL projection process?

The lesson from the saved Week 3–4 reviews is to check a player's individual role before using them for lineup correlation or lower ownership. There are too few completed weeks to establish a forecasting edge. I keep the pre-event assumptions and post-event review together so errors are visible.

## Current results

The project currently includes completed research through **2026 Week 4**.

Week 3 showed that the original process relied too much on finding individually cheap or efficient players. After that review, the process was changed to put more weight on strong games, players who can score well together, overall upside, and only a small amount of lower-owned differentiation.

Week 4 was the first full test of that revised process.

| Week 4 contest | Number of entries | Lineup score |
|---|---:|---:|
| $50 Single Entry | 4,545 | **153.62 DK points** |
| $27 Single Entry | 3,239 | **137.52 DK points** |
| $20 Millionaire | 161,764 | **153.62 DK points** |

### What the simulation expected

Before the games, the strongest high-upside lineup had:

- an average simulated score of **130.6 points**
- a 95th-percentile score of **178.7 points**
- a 99th-percentile score of **208.5 points**

A 95th-percentile result means only about **5% of simulated outcomes scored higher**. A 99th-percentile result means only about **1% scored higher**.

The actual $50 single-entry lineup scored **153.62 points**. That was better than the simulated average, but it did not reach the extreme high-end outcomes the model showed were possible.

### What worked

Several important players produced strong scores:

- Joe Burrow: **28.72**
- Tee Higgins: **29.70**
- Kyren Williams: **36.70**
- T.J. Hockenson: **27.90**

That suggests the overall idea of targeting a strong game environment and combining it with high-upside individual plays was reasonable.

### What did not work

Ja'Marr Chase scored only **5.70 points** after leaving with a concussion. The project treats that mainly as injury-related randomness rather than evidence that the pre-game decision was bad.

Parker Washington scored **2.00 points** and is a more important process-review case because he was intentionally chosen as the Jacksonville player paired with the Cincinnati stack. That result raises the question of whether his individual role and scoring upside were strong enough, even if the lineup correlation made sense.

The ownership-adjusted $27 lineup scored **137.52 points**, lower than the raw-ceiling version. The current lesson is simple: **do not give up too much expected scoring upside just to make a lineup less popular.**

### Current takeaway

The revised process produced a better-structured lineup and the model identified a lineup with real upside. However, there are still too few completed weeks to say that the model has a proven long-term advantage.

The Week 4 records also do not yet include final contest rank, the cash line, or actual player ownership. Those fields will be important in future weeks because they show not only how many points the lineup scored, but how well it performed against the actual field.

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

## What I learned / what I would do differently

A high simulated ceiling is not validation. I would build a longer record with contest rank, cash line, actual ownership and forecast error against a simple baseline before describing any advantage. The existing weekly files preserve the assumptions and reviews needed for that comparison.
