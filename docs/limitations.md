# Model Limitations

This repository is an analytical sports-modeling project, not a production forecasting platform.

## Input risk

Many football assumptions are estimated manually from public information. Errors in expected volume, efficiency, player role, injury status, or touchdown expectations flow directly into the projection.

## Distribution assumptions

Parts of the uncertainty layer use normal or truncated-normal approximations. NFL fantasy outcomes are discrete, skewed, correlated, and can contain heavier tails than those approximations imply.

## Ownership model

The ownership estimate is a relative candidate-pool model. It does not currently reconstruct the full contest field or use a large historical calibration sample.

## Correlation

The core player simulation does not yet model all player-to-player and game-level dependencies. Week 4 contains exploratory correlated lineup analysis, but that layer is not yet fully integrated into the reproducible Python pipeline.

## Sample size

The repository currently contains a limited number of documented slates. Conclusions from early weeks should be treated as provisional until a larger out-of-sample history exists.

## Data lineage

The project uses public football, salary, market, injury, and contest-result inputs. It does not currently implement automated source lineage, timestamp governance, or production-quality data validation across every external input.

## Decision boundary

Projection quality is only one part of tournament performance. Realized results also depend on correlation, ownership, lineup construction, late news, and irreducible game variance.

The project is designed to evaluate the decision process, not to claim deterministic or guaranteed outcomes.
