# Sunday Week 5 — Process review before the $5 / ~23,000-entry single-entry decision

**Timestamp:** October 11, 2026, morning, before official main-slate inactives and the noon CT lock.

This is an **incremental research revision**. It does not overwrite the October 9, October 10, or earlier October 11 snapshots. Compare [the earlier $5 contest builds](../contest_5usd_23k_README.md) with [our five new roster previews](independent_preview.csv). It is not a DK upload file; **published salaries are arithmetic-checked, not verified against the contest export**, and no result is a calibrated P90/P99, tournament cash probability or payout EV.

## Decision we are revising

The previous $5 / 23k short list leaned on Maye–Doubs, Braelon Allen, or Goff–St. Brown–TeSlaa with two Arizona bring-backs. Several pieces may work, but our research process was **too quick to assume that injury-driven opportunity is concentrated onto the individual we chose**.

This is the same failure mode flagged in Week 3 with Jalen Coker and in Week 4 with Parker Washington. The Week 4 [reproducibility audit](../../../2026_week_04/audit_2026-10-08/README.md) limits any claim of proven game-level calibration; the available input snapshots are incomplete/mixed. The point of the lessons is to improve *decisions*, not pretend two completed weeks prove an edge.

## What changes now

| Earlier process mistake | Concrete Week 5 control | What changed |
|---|---|---|
| Week 3: cheap QB and multiple independent salary punts | Require a deliberate QB + pass-catcher story; audit every sub-$5k WR's target/carry/TD path | Focus on Maye–Henry, Brissett–Wilson/McBride, and Goff–St. Brown/LaPorta, not automatic cheap WR |
| Week 3: Coker role inflated by news | Regression stress on injury-opportunity players | Doubs baseline **7.5 targets → 5.5**, expected receiving TD **0.35 → 0.27**; Allen **18.5 → 16 carries**, **4.0 → 3.2 targets** plus TD/bonus reduction |
| Week 4: Parker weak run-back | Bring-back not required in a generic QB build | Goff–St. Brown–LaPorta can be examined *without* a weak Arizona addition |
| Week 4: player shares wrong in good game thesis | Explicit exposure and joint DET–ARI downside scenarios | Brissett–Wilson–McBride concentration is a deliberate high-pass-volume bet, not three independent projections |
| Week 4: lower ownership sacrificed points | No arbitrary low-owned punting; compare forecast plus cost of chalk | Preserve Gibbs, Wilson, McBride as possible good chalk; test Goff/LaPorta leverage *with a credible role* |
| Week 4: same roster across contests | $5, approx. 23k field own review and pre-lock freeze | Do not copy the 4k–6k entry or submit multiple contenders in a single-entry contest |

### External data versus manual hypotheses

The reports support an uncertain but real role reshuffle for New England: [DraftKings Oct 11 Doubs review](https://dknetwork.draftkings.com/2026/10/11/romeo-doubs-fantasy-football-start-or-sit-advice-for-week-5/) says Week 4 produced **six catches on nine targets, two TDs**, but only **11 total targets in Weeks 1–3**. [Patriots' roster news](https://www.patspulpit.com/new-england-patriots-analysis/140161/patriots-roster-moves-raiders-game-nfl-week-5-mack-hollins-brenden-schooler-reggie-gilliam) says Hollins is on injured reserve and Chism also receives additional opportunities. The exact **5.5 target baseline is a conservative analyst sensitivity**, not an empirically refitted forecast. We separately preserve the 7.5-target upside hypothesis in the Oct 11 opening snapshot.

For Allen, [Breece Hall's absence](https://www.cbssports.com/nfl/news/nfl-week-5-inactives-injury-tracker-updates/live/) and the [39.5 CLE–NYJ game total](https://dknetwork.draftkings.com/2026/10/11/cleveland-browns-at-new-york-jets-prediction-pick-for-nfl-week-5-on-sunday-10-11-26/) indicate a mixed situation. The 16-carry, 3.2-target scenario is **our stress adjustment**, not confirmed workload. The [Oct 10 leverage report](https://www.compoundingedges.com/nfl/news/draftkings-nfl-dfs-leverage-report-for-10-11-26) projects persistent rain and concentrated Allen ownership, which strengthens the case for a sensitivity, not a mandatory fade.

Two outside ownership screens disagree substantially: the October 10 Fantasy Alarm screen projected Gibbs 33.5%, McBride 31.3% and Michael Wilson 33.1%; a [separate Oct 10 leverage screen](https://www.compoundingedges.com/nfl/news/draftkings-nfl-dfs-leverage-report-for-10-11-26) shows McBride 67.9%, Wilson 57.2% and Gibbs 20.3%. **Neither is actual ownership in our 23k single-entry contest**. Do not use point-precise ownership multiplication to imply lineup uniqueness.

## Forecast impact of role conservatism

| Player | Opening Sunday subjective mean | Conservative scenario | Change |
|---|---:|---:|---:|
| Romeo Doubs | 12.49 | **9.32** | -3.16 |
| Braelon Allen | 15.44 | **12.96** | -2.49 |

Point means come from the project's current DraftKings arithmetic engine, with the noted input changes. These are **not measured external projections** and no standard errors are implied.

The opening Sunday Maye–Doubs candidate had roughly **139.83** mean points under the earlier **7.5-target, 0.35 receiving-TD** Doubs inputs. Keeping that *same lineup* but regressing his targets/TD produces roughly **136.66**. A formerly high-scoring lineup now relies more heavily on the unproven Doubs role than its aggregate score disclosed. That is the kind of weak-link check we should have performed before Week 4.

## Independent pre-lock candidate screen: known salary references

An independent exhaustive comparison over the documented 48-player curated pool, using the updated Doubs/Allen assumptions, compared QB families and salary-valid lineups. The five representative **role-aware preview builds** are stored in [independent_preview.csv](independent_preview.csv). The new Python runner [run_week5_process_review.py](../../../../run_week5_process_review.py) is also committed for local reproduction, and adds objective mean plus **separate** RB/QB/DET–ARI/uncertain-role downside scenarios and one-TE vs two-TE searches. That Python runner has **not been executed or integration-tested within this chat**, and its generated CSVs/manifest are not claimed as present.

| Hypothesis | QB + main pass catchers | Key DET–ARI exposure | Salary | Manual mean |
|---|---|---|---:|---:|
| Brissett / supported pass volume | Brissett–Wilson–McBride | Wilson and McBride | $49,600 | **138.33** |
| Love / Watson pivot | Love–Watson | McBride | $50,000 | **138.28** |
| Maye / Gibbs, **without Doubs** | Maye–Henry | Gibbs and Wilson | $49,800 | **135.02** |
| Goff / strong-role Detroit | Goff–St. Brown–LaPorta | Goff, St. Brown, LaPorta | $49,800 | **133.89** |
| Maye–Doubs regression control | Maye–Doubs | Wilson and McBride | $50,000 | **136.66** |

Note: projected totals are model means, and **0.05 points is not meaningful precision**. Our position-level standard deviations are generic priors and *cannot* establish which has the best P99. Opposing DST conflicts, exactly nine different players, position structure, $50k cap and QB pass-catcher pairing were independently checked on the preview records; official game-slate ID/salary matching is still pending.

### Modeled dependence on the chalk game

A more honest differentiation measure than counting Arizona players is **how much of each lineup's modeled mean depends on Detroit–Arizona**. Using the source player's own DK means (not independent probabilities):

| Preview | DET–ARI modeled DK points | Total lineup modeled mean | Share |
|---|---:|---:|---:|
| Brissett / Wilson / McBride | 54.22 | 138.33 | **39.2%** |
| Goff / St. Brown / LaPorta | 52.33 | 133.89 | **39.1%** |
| Maye / Gibbs / Wilson | 42.32 | 135.02 | **31.3%** |
| Love / Watson + McBride | 19.19 | 138.28 | **13.9%** |

This is a **concentration accounting identity**, not estimated correlation, payout odds or game-failure probability. The Goff build is just as dependent on DET–ARI production as Brissett's despite having less popular individual roster components. The Love version diversifies away from that game, but loads more outcomes onto CHI–GB. This addresses the JAX–CIN lesson: choose a *different scoring story*, not just a different set of names inside the same game.

### Roster thesis, weak links and selection

**Brissett + Wilson + McBride (highest conditional manual mean):** The real thesis is *Arizona throws heavily and these two established pass catchers capture the scoring*. It is not a requirement that Detroit–Arizona hits 54.5. Wilson and McBride still contend with each other for team targets; their expected targets total **19.75** against Brissett's assumed **35 pass attempts**. Both can hit, but the game/team/player share dependence is unresolved. This build has substantial game and ownership concentration; use only after those roles and the overall field strategy are accepted.

**Goff + St. Brown + LaPorta (genuine leverage):** We keep an NFL-high total game with a quarterback some third-party screens project much lower-owned than its popular receivers. LaPorta's six-target assumption is more defensible as a studied role than the $3,400 TeSlaa punt in the original five-man stack, but his 11.24 mean is a weakness, not a guarantee of a 25-point TE ceiling. The optimizer can leave out an Arizona run-back to avoid Week 4's forced-Parker mistake. This is an *alternative game script*, not demonstrably highest expected payout.

**Maye + Gibbs without Doubs:** Retains premium Gibbs chalk and Maye rushing ceiling without assuming Doubs' nine-target game repeats. Hunter Henry (5-target assumption, 8.91-point mean) is a different weak link to investigate; not an automatic upgrade or a free ceiling gain.

**Love + Watson pivot:** Separate possible QB-led game explosion with McBride as a one-off from the popular game. Watson's 7.5-target analyst prior, 15.49 mean, and Bears–Packers game script all need scrutiny before entry; Swift and Odunze within the same roster can compete for Chicago TDs. It is *not* a safe anti-chalk lineup merely because Love is less owned.

**Doubs-control lineup:** Hold for sensitivity and archival comparison, not our default. Its model penalty demonstrates why one Week 4 game plus a new injury does not validate seven or eight targets for one receiver.

### My conditional selection order for one entry in a 23k field

1. **First evaluate Goff–St. Brown–LaPorta versus Brissett–Wilson–McBride**, not simply which mean is higher. Goff provides a more distinctive scoring path; Brissett has stronger manual volume totals but concentrated popular receivers. Neither has verified lineup duplication/P99.
2. **Keep Gibbs viable** through the Maye–Henry version; do not automatically fade Gibbs because he is popular. Confirm Henry's opportunity rather than exchanging one forced stack partner for another.
3. **Do not use the original Goff–TeSlaa five-man stack as a core lineup.** TeSlaa received eight targets last week but was not in our trained/reproducible player pool; treating him as an automatic $3,400 20-point producer repeats the Parker/Coker problem.
4. Re-check final inactives (CIN WRs, Swift, other role shifts), weather, source salary discrepancies and **the exact DraftKings contest** after morning official releases before calling any entry final.

We do not have the contest payout table, official DK ID export, calibrated upper-tail model or lineup-level ownership joint distribution. **No specific candidate is proven to be the strongest 23,000-field play.**

## Changes for the next slate

- Log projected **team pass attempts and each receiver's share** so two stacked WR/TE players aren't estimated independently.
- Require dated evidence for routes/targets rather than extrapolate one game.
- Save at least two scenarios for every post-injury value (baseline and upside).
- Track selected lineup, lock time, actual rank, ownership, score, winnings and in-game injury exits, not only raw DK score.
- Compare each week's decision to baseline heuristic, e.g., top reliable target-share starters plus one QB stack.
- Maintain a separate game/team/player hierarchical simulation research path. Until calibrated, call model-stated P90/P99 only *proxies*, not measured contest finish probabilities.
