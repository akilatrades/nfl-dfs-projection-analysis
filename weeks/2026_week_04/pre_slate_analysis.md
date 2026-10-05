# 2026 Week 4 — Pre-Slate Analysis

This page is completed **before lineup lock**.

The purpose is to record what we believed before the games were played so the post-slate review can separate good process from hindsight.

## Contest

**Contest type:** NFL DraftKings single-entry tournament  
**Entry count:** Not recorded in the archived pre-lock notes  
**Entry fee:** Not recorded in the archived pre-lock notes  
**Salary cap:** $50,000  
**Lineups entered:** 1

### What this means

Because this is a single-entry tournament, the goal is to build one lineup with:

- a strong overall projection,
- enough ceiling to finish near the top,
- useful correlation,
- and only a small number of deliberate lower-owned decisions.

The lineup does **not** need to be different at every position.

The goal is to be different **for a reason**.

---

## Step 0 — Build our own player projections

Before comparing players, create the expected football stat lines in:

`projection_inputs.csv`

The model does not begin with a fantasy-point projection. It begins with assumptions such as:

- pass attempts,
- carries,
- targets,
- catch rate,
- yards per carry,
- yards per reception,
- expected touchdowns,
- and recent fantasy-point volatility.

Then run:

```bash
python run_projections.py weeks/2026_week_04/projection_inputs.csv
```

That creates `player_pool.csv` with:

- our model projection,
- our model floor,
- our model ceiling,
- value per $1,000 of salary,
- and our ownership estimate.

Then run the statistical layer:

```bash
python run_statistical_analysis.py weeks/2026_week_04/player_pool.csv
```

That creates `player_analysis.csv` with position percentiles, 3x/4x hit probabilities, simulation percentiles, and the tournament leverage index.

For the plain-English explanation of those statistics, see:

[Week 4 statistical analysis](statistical_analysis.md)

### Projection check

Before using the numbers, ask:

- Does the expected workload make sense?
- Did an injury or role change alter the volume?
- Is the efficiency assumption too optimistic?
- Is the touchdown expectation reasonable?
- Is the ceiling being driven by real volatility or by a bad input?

The goal is not to make the model look precise. The goal is to make every assumption visible.

---

## Step 1 — Rank the game environments

Before choosing individual players, identify which games have the strongest overall fantasy setup.

A good game environment may have:

- a high expected game total,
- a high expected team total,
- concentrated player roles,
- fast pace,
- aggressive passing,
- or a competitive spread that may keep both teams active for four quarters.

Fill in the table below.

| Game | Game Total | Team A Total | Team B Total | Spread | Why It Could Produce DFS Points | Rank |
|---|---:|---:|---:|---:|---|---:|
| JAX @ CIN | 51.5 | 24.5 | 27.0 | 2.5 | Slate-high baseline total and small spread; strongest two-sided stack environment | 1 |
| NE @ BUF | 48.5 | 21.0 | 27.5 | 6.5 | Strong Buffalo implied total with some blowout risk | 2 |
| DAL @ HOU | 47.5 | 22.5 | 25.0 | 2.5 | Close spread and useful two-sided passing environment | 3 |

### Question to answer

> Which 2–4 games give us the clearest path to a tournament-level stack?

Do not start with the cheapest quarterback or the highest point-per-dollar player.

Start with the games that can create large fantasy scores.

---

## Step 2 — Identify the main stack candidates

A stack intentionally combines players whose fantasy scores can rise together.

The most common example is:

```text
QB + WR
```

because a passing touchdown can score points for both players.

A larger game stack may look like:

```text
QB + WR + opposing WR
```

The opposing player is often called a **bring-back**.

Use this table to compare the main stack ideas.

| Stack | Combined Salary | Our Projection | Our Ceiling | Our Ownership Estimate | Why It Works |
|---|---:|---:|---:|---:|---|
| Burrow + Chase + Higgins + JAX bring-back | Varies by bring-back | See Sunday variance file | High | Popular core | Concentrated exposure to the slate's strongest game environment |
| Lawrence + Jacksonville receiver(s) + CIN bring-back | Lower QB salary | See Sunday variance file | High | Moderate | Uses the cheaper QB side of the same top environment |
| Stroud + Nico + DAL bring-back | Flexible | See Sunday variance file | High | Lower than JAX-CIN core | Main coherent pivot away from the chalkiest game stack |

### Question to answer

> If this game scores well above expectation, which stack benefits most?

---

## Step 3 — Compare ceiling and ownership

Our model projection is the expected DraftKings score produced by our stat assumptions.

Our model ceiling is the higher-end score produced from the player's projection and recent volatility.

Our ownership estimate is our pre-lock forecast of how popular the player will be.

A lower-owned player is interesting when the ceiling stays close to a more popular alternative.

### Strong leverage example

```text
Player A
Projection: 18.8
Ceiling: 31
Ownership: 24%

Player B
Projection: 17.9
Ceiling: 30
Ownership: 9%
```

Player B gives up very little projection and almost no ceiling, but is much less popular.

That is a useful player to investigate.

### Weak leverage example

```text
Player A
Projection: 18.8
Ceiling: 31
Ownership: 24%

Player C
Projection: 12.1
Ceiling: 21
Ownership: 3%
```

Player C is different, but the lineup may be giving up too much upside just to be lower owned.

Use the player-pool file to identify these comparisons.

---

## Step 4 — Choose only 1–2 deliberate leverage decisions

For single entry, the lineup does not need nine low-owned players.

Use this section to record the actual places where we plan to differ from the field.

### Leverage decision record

The working template was superseded by the completed **Final pre-lock thesis** below. The final thesis records the selected leverage construction and the football outcome required for it to succeed.

If there is no strong reason for a second leverage play, do not force one.

---

## Step 5 — Build candidate lineups

The Sunday candidate file is now populated with:
- four initial correlated constructions,
- the raw-ceiling Burrow build,
- the ownership-adjusted Burrow build,
- and the DAL-HOU leverage alternative.

See `lineup_candidates.csv` and `se_variance_analysis_2026-10-04.md`.

### Step 5A — Compare variance, not only average projection

The Sunday pass added an exploratory upper-tail comparison.

Instead of asking only "Which lineup projects the highest?", we also compared how often each construction reached unusually high simulated scores.

This matters because single-entry tournaments reward top finishes, not just average outcomes.



For each candidate lineup, record:

- salary used,
- our projected points,
- our projected ceiling,
- our ownership estimate,
- primary stack,
- leverage decisions,
- and the overall lineup story.

A lineup story is simply the football outcome that would make the lineup succeed.

Example:

> "Detroit scores four touchdowns through the passing game, the opposing offense keeps the game competitive, and our lower-owned WR benefits from increased volume."

If the lineup does not have a clear path like that, it may just be nine unrelated projections.

---

## Step 6 — Run the Difference Test

Before choosing the final lineup, answer:

> **Why is this lineup different from the field?**

A good answer sounds like:

> "We are using a lower-owned WR from one of the slate's strongest game environments because his ceiling is close to the chalk WR above him, and he is directly correlated with our quarterback."

A weak answer sounds like:

> "He is only 3% owned."

Low ownership by itself is not a reason to roster someone.

---

## Step 7 — Check the complete lineup

Before lock, answer each question.

- Does the lineup have a clear primary stack?
- Does the stack come from a strong game environment?
- Does the lineup have enough ceiling?
- Are we sacrificing too much projection to be different?
- Are our lower-owned plays actually capable of tournament-level scores?
- Did salary savings create more upside somewhere else?
- Are we overreacting to late news?
- Are we using too many low-ceiling value plays?
- What football outcome makes this lineup finish near the top?
- Would we still like this lineup if ownership information disappeared?

If the last answer is no, ownership may be driving the lineup too much.

---

## Final pre-lock thesis

**Primary game environment:** JAX @ CIN

**Primary stack:** Joe Burrow + Ja'Marr Chase + Tee Higgins

**Main leverage decision:** Use Jakobi Meyers as the less-obvious Jacksonville bring-back in the current ownership-adjusted SE leader.

**Second leverage decision, if used:** James Cook changes the one-off construction while keeping strong role/ceiling.

**Why this lineup can finish near the top:** The Cincinnati stack can score together in the slate's best game environment, the Jacksonville bring-back benefits if the game stays competitive, and the remaining values are tied to identifiable roles rather than speculative cheap salary.

**What could make the lineup fail:** JAX-CIN underperforms, Cincinnati touchdowns are distributed away from the stack, or the injury-created values receive less work than expected.

**Late-news changes made:** Breece Hall out increased Braelon Allen's importance; Justin Jefferson out increased Jordan Addison's importance; Nico Collins' return strengthened DAL-HOU as the main pivot.

**Current salary used:** $49,800 for the ownership-adjusted leader.

**Current exploratory mean:** 126.9 DK points.

**Current exploratory P95:** 176.4 DK points.

**Current exploratory P(170+):** 6.9%.

**Ownership estimate:** Still provisional; ownership is being used as a soft tiebreaker rather than a precise field forecast.

This section is preserved as the final archived pre-lock thesis.


---

## Sunday correlated simulation note

The detailed Sunday walkthrough is stored in [se_variance_analysis_2026-10-04.md](se_variance_analysis_2026-10-04.md).

The exploratory correlated simulation results are saved for audit, but the current repository Python engine does not yet fully reproduce that correlated layer from raw inputs. The distinction is documented so later review can separate finished code from exploratory analysis.
