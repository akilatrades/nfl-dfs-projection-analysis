# Methodology

## Objective

The project treats NFL DFS as a forecasting and decision-analysis problem rather than a collection of isolated lineup picks.

The core research question is whether a transparent pre-event process can improve through repeated measurement of:

- projection error,
- ownership error,
- uncertainty calibration,
- lineup correlation,
- salary allocation,
- and decision quality under incomplete information.

## Projection model

Player projections begin with expected football statistics. Depending on position, inputs can include:

- pass attempts and completion rate,
- yards per completion,
- carries and yards per carry,
- targets, catch rate, and yards per reception,
- expected touchdowns and turnovers,
- recent fantasy-point volatility,
- probabilities for DraftKings yardage bonuses,
- and DST event expectations.

The projection engine converts those expected statistics into DraftKings fantasy points using explicit scoring constants.

This approach makes the model decomposable. A forecast miss can be investigated through its underlying volume, efficiency, touchdown, or scoring assumptions.

## Uncertainty

The first-stage floor and ceiling estimates use recent fantasy-point volatility around the point projection. The statistical layer then estimates salary-based 3x and 4x hit probabilities and generates simulation percentiles.

The current simulation is intentionally simple and transparent. It is not presented as a full play-by-play football simulator.

## Ownership estimate

The project creates a candidate-pool popularity estimate from projection, value, and ceiling percentiles. It is designed as a relative research signal, not as a fully calibrated forecast of the entire contest field.

Actual ownership is recorded after lock when available so the estimate can be evaluated and improved.

## Game environment and correlation

Lineup construction is evaluated at both the player and game level. The research process considers:

- implied scoring environment,
- role concentration,
- spread and game competitiveness,
- stack correlation,
- bring-back logic,
- salary opportunity cost,
- and ownership leverage.

Lower ownership is not treated as sufficient justification for a play. A lower-owned construction should retain a credible upper-tail path.

## Sensitivity analysis

Key projection inputs can be perturbed by a fixed percentage to measure how much each assumption changes the final projection. This helps identify which assumptions drive model risk.

## Pre-event / post-event separation

Pre-slate assumptions, candidate lineups, and the final thesis are recorded before the event. Actual results and review notes are stored separately.

This separation is intended to reduce hindsight bias and distinguish a poor result from a poor decision process.

## Exploratory correlated analysis

Week 4 includes a saved correlated upper-tail analysis for candidate lineups. That work is retained as an exploratory research record.

The repository's core Python engine does not yet fully reproduce that correlated layer from raw inputs, so the exploratory results are not represented as a production-ready model component.
