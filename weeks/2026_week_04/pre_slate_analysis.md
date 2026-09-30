# 2026 Week 4 — Pre-Slate Analysis

This page is completed **before lineup lock**.

The purpose is to record what we believed before the games were played so the post-slate review can separate good process from hindsight.

## Contest

**Contest type:** NFL DraftKings single-entry tournament  
**Entry count:** TBD  
**Entry fee:** TBD  
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
| TBD |  |  |  |  |  |  |
| TBD |  |  |  |  |  |  |
| TBD |  |  |  |  |  |  |

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
| TBD |  |  |  |  |  |
| TBD |  |  |  |  |  |
| TBD |  |  |  |  |  |

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

### Leverage decision 1

**Player / construction:** TBD  
**Our ownership estimate:** TBD  
**Popular alternative:** TBD  
**Why the ceiling is still strong:** TBD  
**What football outcome makes this work:** TBD

### Leverage decision 2

**Player / construction:** TBD  
**Projected ownership:** TBD  
**Popular alternative:** TBD  
**Why the ceiling is still strong:** TBD  
**What football outcome makes this work:** TBD

If there is no strong reason for a second leverage play, do not force one.

---

## Step 5 — Build candidate lineups

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

**Primary game environment:** TBD

**Primary stack:** TBD

**Main leverage decision:** TBD

**Second leverage decision, if used:** TBD

**Why this lineup can finish near the top:** TBD

**What could make the lineup fail:** TBD

**Late-news changes made:** TBD

**Final salary used:** TBD

**Final model projection:** TBD

**Final model ceiling:** TBD

**Final ownership estimate:** TBD

This section should be completed before the lineup locks.
