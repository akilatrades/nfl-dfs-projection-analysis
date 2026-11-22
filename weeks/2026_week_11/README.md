# Week 11 — November 22, 2026 DraftKings main slate

For the $20, 147,058-entry contest with $1 million to first, use the [final Sunday Millionaire lineup and simulations](millionaire_final/README.md).

Frozen 2026-11-22T09:15:37-06:00. Early recommendations, before official 10:30 AM Central inactive releases. Main slate locks noon Central. Assuming the same $12 single-entry Fair Catch contests as the user's previous screenshots: 5,882 and 12,254 maximum entries. No current contest ID or payout structure supplied. Nothing was submitted.

**If choosing only one, prefer the Dak build.** The Ward/Gibbs build is a different tournament construction, not a proven higher-EV lineup. It gives up 4.74 mean projected points and roughly 9.4 points at the modeled 95th percentile. It performed relatively better against one projection-conscious hypothetical field; that advantage weakens when Gibbs' assumed field exposure rises. This is a material modeling uncertainty, not an established edge.

| Slot | $60K working contest: Dak | $125K working contest: Ward/Gibbs |
|---|---|---|
| QB | Dak Prescott — $6,700 | Cam Ward — $5,500 |
| RB1 | Emmett Johnson — $6,000 | Jahmyr Gibbs — $10,000 |
| RB2 | Tony Pollard — $6,500 | Emmett Johnson — $6,000 |
| WR1 | CeeDee Lamb — $8,800 | Carnell Tate — $5,500 |
| WR2 | Rome Odunze — $4,600 | Emeka Egbuka — $5,200 |
| WR3 | Elic Ayomanor — $3,700 | Jakobi Meyers — $4,500 |
| TE | Sam LaPorta — $4,400 | Sam LaPorta — $4,400 |
| FLEX | Jonah Coleman — $6,300 | Jonah Coleman — $6,300 |
| DST | Chargers — $3,000 | Jets — $2,600 |
| Salary | $50,000 | $50,000 |
| Sum of mean forecasts | 144.185 | 139.445 |
| Held-out simulation median | 140.95 | 136.86 |
| Held-out simulation 95th percentile | 203.77 | 194.37 |

These percentiles are outcomes of an approximate conditional scoring model, not validated prediction intervals or maximum ceilings. Salary inputs are public published DK salaries, cross-checked where a second board was available, not the official contest CSV.

## Why these players and constructions

- **Dak–Lamb** targets the leading 54.5-point frozen game environment. Pollard and Ayomanor supply plausible Tennessee responses. One receiving partner avoids forcing two cheap TEs to afford a double Dallas stack. A credible single stack can still win a tournament; no claim of a measured optimum.
- **Emmett** remains a role-based play with Walker officially out. His price rose to $6,000. His retained forecast is 23.415, not a copy of last week's 38-point performance. KC line injuries and lower-than-expected work are risks. A 25% reduction is tested.
- **Coleman** combines the Denver favorite script with a published receiving role, not just the prior box score. The model reduces his forecast 15% in the adverse-role test. Keep him in FLEX because Denver kicks at 3:25 PM Central.
- **Pollard** has a current opportunity case with Spears on IR, rather than a recency-only case. No arbitrary extra touches added to the public forecast after the transaction.
- **Gibbs** is explicitly tested at $10,000. The second entry bets on his premium ceiling rather than ruling him out because he is expensive. It retains Emmett/Coleman while moving away from Dallas WR concentration. Egbuka plus LaPorta gives Detroit–Tampa Bay correlation without requiring Goff. This is an alternate allocation of salary, not proof of more first places.
- **Tate** is conditional on active status and a normal expected role after the shoulder absence. Full Friday practice helps; it does not establish a full Sunday route count.
- **Ayomanor** is one cheap WR with real involvement, not a 10-target assumption copied from the week Tate missed. His 9.44 forecast is stressed downward and he is omitted from the second entry.
- **Meyers** is the alternate's most modest receiving-ceiling piece. He is Jacksonville's secondary target rather than a promoted WR1. His forecast remains 9.87. This is an explicit salary compromise; the primary build is preferred if that compromise is unappealing.
- **Egbuka** is conditional on Tampa's QB situation; Godwin's presence is included rather than ignored. LaPorta is a credible TE, not an injury-based punt. Chicago weather limits confidence in Odunze and is stressed separately.
- **DST** is a salary/role trade-off. Chargers are the stronger mean option; Jets are $400 cheaper in the Gibbs build. No opposing offensive player is paired with either defense.

## Current ownership: forecast versus assumptions

| Player | Percentage used | Provenance |
|---|---|---|
| Dak Prescott | 25.0% | Published FTA Sunday forecast |
| Emmett Johnson | 74.8% | Published FTA Sunday forecast |
| Tony Pollard | 29.7% | Published FTA Sunday forecast |
| CeeDee Lamb | 30.3% | Published FTA Sunday forecast |
| Rome Odunze | 10.0% | Analyst assumption; not a published player forecast |
| Elic Ayomanor | 18.0% | Analyst assumption; not a published player forecast |
| Sam LaPorta | 8.0% | Analyst assumption; not a published player forecast |
| Jonah Coleman | 36.5% | Published FTA Sunday forecast |
| Chargers | 9.8% | Published FTA Sunday forecast |
| Cam Ward | 10.0% | Published FTA Sunday forecast |
| Jahmyr Gibbs | 12.0% | Analyst assumption; not a published player forecast |
| Carnell Tate | 27.0% | Published FTA Sunday forecast |
| Emeka Egbuka | 5.0% | Analyst assumption; not a published player forecast |
| Jakobi Meyers | 5.0% | Analyst assumption; not a published player forecast |
| Jets | 5.0% | Analyst assumption; not a published player forecast |

The Dak construction contains substantial chalk. The Gibbs alternative has fewer of the highest published ownership pieces, but that does not prove uniqueness. Neither summed ownership nor the product of individual exposures is a valid duplicate probability. We have no actual opponent entries. Field-generation slot totals normalize unpublished weights; requested input weights, normalized targets and realized marginals differ and are all audited. Gibbs' 12% raw assumption becomes roughly 5% in the two fitted baseline fields, so an extra 20%-target Gibbs sensitivity was essential; it achieved 14.54% realized Gibbs exposure. It is labelled hypothetical, not published.

## Executed comparisons

- 116-player curated pool across all ten games; 16 QBs and 12 defenses, not the entire official DK pool.
- 632 unique solver candidates, plus two explicit portfolio/inactive alternatives, all legal under the saved salary and eligibility inputs.
- 150,000 correlated scoring draws for the original 632, seed 20261123.
- Four separate 50,000-draw adverse-assumption checks: lower forecasts, role uncertainty, Chicago passing weather, lower variance. A separate 100,000-draw mean/correlation sanity check passed; maximum individual mean error about 0.066 points.
- Six final comparisons, 200,000 held-out draws, seed 20261822. Three additional 75,000-draw stresses include the two manual alternatives.
- Two 12,253-opponent synthetic fields, fitted from partly assumed ownership, each evaluated in the original broad comparison with 6,000 score draws and the final comparison with 10,000. Their starting weight temperatures differ but they fit the same targets; they are not independent empirical field models.
- A third full-capacity hypothetical field admits only opponents projecting at least 135 points. Another raises Gibbs' ownership target to 20%. Both have 10,000 final comparison draws. These are assumption tests, not actual historical fields.
- Shared QB failure is a deterministic additional stress, with no made-up injury probability. Exact forecast sums and stress outputs are saved.

The model allocates each team's passing/rushing TDs once and awards the QB those same passing TDs. A mean-one game/team factor and gamma non-TD scores approximate yardage, receptions and DK bonuses. It does not simulate complete stat lines, turnovers lost by offensive players, every yardage bonus threshold, backup substitution paths or real contest payouts. It is not calibrated to this season's opponent field. First-place events are sparse even in 10,000 draws; fine rankings are noisy. Do not turn synthetic shares into real win odds, expected dollars or promises.

## News conditions and exact pivots

1. Check official early inactives at **10:30 AM Central**, plus the actual DK slate/player salaries. Neither selected lineup uses a player already ruled out in the retrieved reports. The early inactive lists had not been published at research time.
2. If Tate is out or a meaningful limit is reported, the saved 49,800-dollar fallback is Ward / Gibbs / Emmett / Ayomanor / Pickens / Meyers / LaPorta / Coleman FLEX / Jets. It was separately scored as candidate 633. Its forecast uses the old baseline for Ayomanor and does not invent an injury boost. It reintroduces shared Ayomanor exposure; that is a deliberate conditional compromise, not equivalent diversification.
3. If Mayfield is out or materially limited, Egbuka can become Jordyn Tyson at the same $5,200, provided Tate is available and Chicago's weather remains acceptable. That pivot is salary/legal checked, not separately Monte Carlo ranked; the changed baseline forecast is 139.835. A bigger role change warrants reconstruction rather than a claim of the same projection.
4. Keep Coleman in FLEX in both entries. Jaguars players and the Jets defense also play later. After early lock, every swap needs the remaining salary, legal slots and official afternoon active lists checked.

## Other saved choices

| ID | Construction | Mean | Modeled 95th percentile | Why retain it |
|---|---|---|---|---|
| 71 | Dak Prescott | 142.095 | 204.90 | One TE, Dak plus Lamb/Pickens; requires Eagles DST and Ayomanor |
| 79 | Dak Prescott | 142.500 | 207.18 | Dak plus Lamb/Pickens, Kelce/LaPorta two TE; stronger upper-tail screen but concentration trade-off |
| 253 | Cam Ward | 140.775 | 198.84 | Ward plus Tate/Ayomanor, Gibbs and Javonte; stronger scalar score tail than alternate but shares the primary cheap WR |

All full nine-player rosters and salary totals for these alternatives are in `recommendations.json`. The chosen pair balances primary forecast strength and avoiding the same weak receiver in both entries. The pair is a judgment call, not a simulated proof of the best portfolio.

## Reproduce and review

Python with NumPy and SciPy is required. From this directory:

```bash
python run.py --phase all --draws 150000 --field-draws 6000
python sensitivity.py
python final_review.py
python gibbs_field.py
python verify.py
```

The more-projection-conscious rejection-sampled field can take several minutes. Generated `.npy` fields are intermediate artifacts recreated by `run.py`; they are not committed. Input player IDs, seeds and candidate recipes are frozen. `candidate_ownership_weight` records the initial exploratory solver penalty so the subsequent refined synthetic-field weights do not silently change candidate IDs.

See [sources](sources.md), [prior lessons](lessons_applied.md), [exact lineups and forecasts](recommendations.json), [CSV](lineups.csv), [final comparison](final_comparison.json), [Gibbs field sensitivity](field_gibbs_chalk_results.json), and [verification](final_verification.json).

Week 10 entered roster, official score, placement and payout are still missing. Its saved recommendations are not treated as entered results.
