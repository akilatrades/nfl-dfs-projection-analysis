# Week 8 — November 1, 2026 single-entry decision

## Contest and status

NFL $60K Blind Side [Single Entry], $27 entry, maximum 2,591 entrants. Screenshot showed 1,839 entered; I plan around the capacity rather than assuming overlay. Payout ladder was not supplied. Recommendation only; no entry has been submitted by this workflow. Published salaries are checked arithmetically, not matched to an official contest ID export. Early-game final inactives must be checked before noon Central; Stevenson plays in the late window.

## Recommended roster

| Slot | Player | Salary |
|---|---|---:|
| QB | Dak Prescott |6300|
| RB | Chase Brown |6300|
| RB | Rhamondre Stevenson |5600|
| WR | CeeDee Lamb |8100|
| WR | Ja'Marr Chase |7700|
| WR | Garrett Wilson |6300|
| TE | Brenton Strange |4000|
| FLEX | Mark Andrews |3400|
| DST | Broncos |2300|
| Total ||50000|

The two-TE lineup keeps three established WRs and a direct Dak–Lamb link. It avoids allocating four positions to one game and does not force an Arizona return player. Brown and Chase compete for some Cincinnati touchdowns; this roster needs sufficient team production, not an assumption that both always benefit equally.

Stevenson has a confirmed opportunity change with Henderson OUT, but the forecast is not manually inflated. Strange is full practice with no game designation. Andrews is the weak offensive position: a reported 66.1% route share and 18.3% target share offer a plausible receiving role, but other reports flag declining usage. He is a salary tradeoff, not a safe ceiling claim. Denver faces Kansas City; cheap defense is not synonymous with good defense.

## What actually ran

`python weeks/2026_week_08/screen.py` ran successfully using Python / SciPy 1.17.0. It saved a 33-player curated pool and 19 candidate screens. This is NOT the full DK slate optimizer or the repository's first-principles projection engine. Public FantasySportsCentral point forecasts are the common baseline; FTN and HIVE are cross-checks, not blended coefficients.

Constraints: nine distinct players; one QB and DST; 2–3 RB, 3–4 WR, 1–2 TE; $50,000 cap; at least one QB teammate WR/TE; maximum three offensive players per team; no DST against a rostered offensive opponent. No mandatory bring-back. Additional one-TE and Dak-with-Gibbs variants are explicit comparisons. Candidate JSON preserves all rosters.

| Screen | Original additive forecast | Selection objective |
|---|---:|---:|
| Dak baseline |141.93|141.93|
| Dak sensitivity — selected |140.38|137.83|
| Burrow baseline |140.77|140.77|
| Maye baseline |140.35|140.35|
| Lawrence baseline |139.86|139.86|
| Lamar baseline |137.57|137.57|
| Allen baseline |135.22|135.22|
| Dak + Gibbs |138.34|138.34|
| Dak one-TE sensitivity |139.61|135.49|

Precision is arithmetic, not forecast certainty. The selected roster gives up 1.55 baseline points versus the leading Dak lineup, which uses Jonah Coleman and Wan'Dale Robinson to fit Puka. The one-TE sensitivity alternative uses Bucky, Parker Washington and Malik Washington. It is competitive, not ruled out by a meaningful calibrated statistical difference.

## Sensitivity definition and limitations

For the selection objective only, Stevenson and Pollard forecasts were multiplied by 0.85, Wan'Dale by 0.75, Jonah by 0.65 and Malik by 0.85. These are discretionary analyst stress assumptions, NOT fitted workload probabilities or a confidence interval. Other players are not assumed certain. The selected roster still depends on Andrews and Strange; targeted Andrews reduction of 25% costs 2.13 points, and Strange reduction of 20% costs 2.24 points before any reoptimization. A later change in these assumptions can change the preferred roster.

No field simulation, calibrated joint scoring distribution, duplication model or payout EV was run. Pool restrictions especially underrepresent Buffalo pass catchers; the Allen screen is not an exhaustive evaluation of Allen. No claim of best tournament win probability.

## Football/news checks and prior lessons

- Patriots Saturday report rules Henderson and A.J. Brown OUT. That supports Stevenson and Henry opportunity; it does not automatically validate a cheap Patriots WR.
- Titans rule Spears and Tate OUT; Pollard has no game designation. Wan'Dale still faces a weak team passing environment. I considered both without assuming missing targets all flow to one player.
- Dallas–Arizona and Baltimore–Buffalo are high-total environments. I prefer Dak's salary and Lamb's established role to more speculative stack attachments.
- Jacksonville forecast includes wind around 16 mph with gusts around 24 and rain risk. This affects Strange too; it is a remaining risk, not ignored.
- Miami has rain risk. No automatic cancellation or major downgrade is assumed.
- I did not chase last week's Jameson touchdowns or automatically retain Irving because he scored 27.
- Gibbs was explicitly included in a comparison, rather than faded solely for popularity.
- No player with an OUT designation is selected based on reports checked. Final active lists remain a separate prelock verification.

## Conditional changes

If I decide Andrews' declining role is unacceptable before lock, a salary-valid alternative is Garrett Wilson to Malik Washington ($4,400), Andrews to Hunter Henry ($4,300), and Broncos to Steelers ($3,300): total $50,000. This changes the thesis and projected distribution and requires rechecking Miami weather. It is a contingency, not a second recommendation.

If any selected early-game player is inactive, rework the roster before that game's lock; do not substitute by name alone. Place the latest-starting eligible player at FLEX when reassigning positions. Current FLEX Andrews and other early players all lock early; Stevenson is the only late offensive player in the primary roster.

## Sources — retrieved November 1, 2026

- Baseline published salaries/forecasts: https://fantasysportscentral.com/football/dfscheat.php
- Cross-check: https://ftnfantasy.com/nfl/top-nfl-dfs-cash-game-picks-for-week-8-2026
- Cross-check: https://www.hivefantasy.com/dfs/nfl
- DraftKings matchup/salary analysis: https://dknetwork.draftkings.com/2026/10/31/nfl-dfs-picks-best-draftkings-fantasy-football-plays-for-week-8-2/
- Patriots: https://www.patriots.com/news/week-8-injury-report-patriots-at-dolphins-x9227
- Titans: https://www.tennesseetitans.com/news/week-8-injury-report-titans-at-bengals
- Cardinals/Dallas: https://www.azcardinals.com/news/injury-report-week-8-vs-cowboys
- Jaguars: https://www.jaguars.com/team/injury-report/
- Jets: https://www.raiders.com/news/las-vegas-raiders-new-york-jets-week-8-injury-report
- Andrews role: https://www.fantasypros.com/nfl/notes/480141/mark-andrews-2026-week-8-outlook.php
- Weather: https://mysportsweather.com/nfl

Archive the final entered roster, official salaries, actual ownership, cash line, rank and payout after the slate. This pregame record must not be rewritten using outcomes.
