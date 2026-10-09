# 2026 Week 5 — single-entry research

**Current October 9 scope: single-entry contests with at least 1,000 entries, Sunday October 11.** See the [new field-size constructions](single_entry_2026-10-09/README.md) for three starting lineups, updated assumptions and 43-player research. Entry fee, exact contest and official salary export remain undecided.

The analysis below is the earlier general baseline, retained for comparison. Its provisional leader has not been selected as the final single-entry lineup.

The model compares 35 researched players across six quarterback families. Salaries come from published articles, not a contest export. Every football input is an explicit analyst assumption converted by the existing projection engine. These are initial decision scenarios; they are not fitted Week 1–4 forecasts or an established predictive edge.

## Earlier baseline build

| Slot | Player | Salary |
|---|---|---:|
| QB | Jacoby Brissett | $5,500 |
| RB | Chase Brown | $6,900 |
| RB | Jaylen Warren | $6,700 |
| WR | Amon-Ra St. Brown | $7,900 |
| WR | Michael Wilson | $6,200 |
| WR | Rome Odunze | $4,700 |
| TE | Dalton Schultz | $4,000 |
| FLEX | Emanuel Wilson | $5,300 |
| DST | Browns | $2,800 |
| **Total** | | **$50,000** |

This is the leading mean and individual-stress build **within this limited pool and these assumptions**. The Brissett–Michael Wilson pairing provides the QB stack; St. Brown supplies exposure to the other side. The search selected this bring-back even when it was optional. Emanuel occupies FLEX because his game starts later than the other selected running backs.

The base expectation is **137.08 points**, falling to **132.34** in the worst separately tested workload scenario. Neither figure is a floor, percentile or win probability. The combined stress case is **127.14**; `candidate_comparison.csv` reports it separately.

Warren's workload depends on Dowdle's availability. Emanuel's workload depends on Seattle's backfield, including Charbonnet's possible activation. Brown's receiving assumption depends on Cincinnati's receiver status. This roster needs those facts resolved before an entry decision.

## Why this version does not force Gibbs

Gibbs remains a priority player to evaluate, but salary allocation matters. Locking him into the search produces a **$49,900** alternative: Brissett / Brown / Warren / Michael Wilson / Tinsley / Odunze / Schultz / Gibbs / Browns. Its base expectation is **135.36** under our assumptions and it relies on a speculative Cincinnati receiver. It is saved in `gibbs_alternative.csv`.

This is not evidence that fading Gibbs is profitable. His 21.5-carry, 5.5-target input is an uncalibrated assumption; a stronger workload forecast or a confirmed cheap receiver could change the result. Do not turn a modest modeled point difference into a conviction claim.

## Search and scenario design

`run_week5_research.py` compares 24 specifications: six QBs, two objectives and required-versus-optional bring-backs. Duplicate rosters across specifications are retained so their stability is visible; these are not 24 independent lineups.

The objectives are maximum summed mean projection and maximum minimum summed projection across the base case and six **separate** downside cases:

| Scenario | Assumption change |
|---|---|
| Gibbs volume down | Carries, targets, TD expectations and yardage-bonus probabilities ×0.80 |
| Dowdle returns | Warren equivalent workload inputs ×0.75 |
| Cincinnati receivers return | Tinsley/Meyers targets, receiving TDs and bonus probability ×0.60; Brown receiving inputs ×0.80 |
| Bagent volume down | Passing/rushing volume, TD expectations and passing-bonus probability ×0.80 |
| Wilson committee | Emanuel equivalent workload inputs ×0.75 |
| Diggs limited | Targets, receiving TDs and receiving-bonus probability ×0.70 |

These magnitudes are stress choices, not historically estimated effects. They have no assigned probabilities. `joint_downside` combines all six changes as an additional diagnostic, outside the selection objective. There is no calibrated correlation, contest-field or ownership simulation here.

Every build has one QB, two RB, three WR, one TE, one RB/WR/TE FLEX and one DST, nine unique players and salary ≤$50,000. Additional **strategy** constraints require one QB pass catcher, at most four players per team, at least two games, no offense opposing its own DST, and at most one speculative-role receiver. These are declared search choices, not all official contest requirements. A bring-back can be any opposing RB/WR/TE and is not mandatory in the optional screen.

Full re-optimizations excluding Bagent, Cincinnati backup receivers, Warren, Gibbs, Emanuel or Diggs are in `contingency_lineups.csv`. These are distinct what-if cases, not automatic late-swap instructions: already-locked players and official IDs are not modeled.

## What to resolve before calling any lineup final

1. Import the actual contest salary CSV, player IDs and game set; expand beyond this curated pool.
2. Verify final injuries and roles, especially PIT/SEA backfields, Cincinnati receivers and Chicago QB. Remove inactive players and rebuild all affected inputs.
3. Check relevant weather and line movement near lock; no weather adjustment is included today.
4. Match the selected single-entry contest, with at least 1,000 entries, to its actual payout structure. The current mean/stress optimizer does not estimate expected payout.
5. Freeze inputs, source timestamps and intended entries before kickoff. Save actual ownership, ranks and payouts afterward.

Research evidence and conflicting-source decisions are in [sources.md](sources.md). The NFL schedule has eleven Sunday afternoon games, with initial kickoff at **noon Central / 1 p.m. Eastern**. Thursday, London, Sunday night and Monday are outside this research slate.

## Reproduce

```bash
pip install -r requirements.txt
python run_week4_audit.py
python run_week5_research.py
python -m unittest discover -s tests -p test_optimizer.py -v
```

The optimizer uses [SciPy MILP](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.milp.html), demands solver-certified optimality at zero relative gap, and rejects infeasible searches rather than silently returning a partial roster. `run_manifest.json` captures input/code hashes and the model boundary. Generated CSVs are research tables, not DraftKings upload files.
