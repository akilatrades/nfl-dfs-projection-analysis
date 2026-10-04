# Week 4 Saturday Player Pool Build

**Contest focus:** DraftKings NFL main-slate single-entry and large-field GPP  
**Status:** Preliminary injury-adjusted research pool  
**Date:** October 3, 2026

## Process

The Week 3 review changed the order of operations:

```text
injuries / availability
-> game environment
-> correlated ceiling
-> projections
-> ownership
-> leverage
-> final lineup
```

## Single-entry pool

### Quarterback
- Joe Burrow
- Trevor Lawrence
- Josh Allen
- C.J. Stroud
- Patrick Mahomes
- Brock Purdy

### Running back
- Braelon Allen
- James Cook
- Derrick Henry
- Chase Brown
- Christian McCaffrey
- Kyren Williams
- Kenneth Walker III
- Ashton Jeanty

### Wide receiver
- Ja'Marr Chase
- Tee Higgins
- CeeDee Lamb
- Nico Collins
- Puka Nacua
- Jordan Addison
- Garrett Wilson
- Rashee Rice
- Parker Washington
- Jakobi Meyers
- George Pickens
- Jaxon Smith-Njigba

### Tight end
- George Kittle
- Trey McBride
- Brock Bowers
- Dalton Schultz
- Dalton Kincaid
- Mark Andrews

### Primary SE stack families
1. JAX @ CIN
   - Burrow + Chase/Higgins + Jacksonville bring-back
   - Lawrence + Jacksonville receiver + Chase/Higgins
2. DAL @ HOU
   - Stroud + Collins/Schultz + Lamb
   - Dak + Lamb/Pickens + Collins/Schultz
3. BUF vs NE
   - Allen + Buffalo pass catcher
4. KC @ LV
   - Mahomes + Rice + Bowers/Jeanty
5. DEN @ SF
   - Purdy + Kittle + Denver bring-back

### SE philosophy
Prioritize projection, role stability, and correlation. Use only one or two deliberate leverage decisions.

## Large-field GPP pool

### Quarterback
- Trevor Lawrence
- C.J. Stroud
- Dak Prescott
- Patrick Mahomes
- Brock Purdy
- Matthew Stafford
- Josh Allen

### Running back
- Christian McCaffrey
- Kyren Williams
- Kenneth Walker III
- Ashton Jeanty
- Derrick Henry
- James Cook
- Chase Brown
- Braelon Allen

### Wide receiver
- Tee Higgins
- Nico Collins
- CeeDee Lamb
- George Pickens
- Rashee Rice
- Puka Nacua
- Ja'Marr Chase
- Jakobi Meyers
- Parker Washington
- Brian Thomas Jr.
- Jordan Addison
- Jaxon Smith-Njigba

### Tight end
- Brock Bowers
- George Kittle
- Dalton Schultz
- Dalton Kincaid
- Mark Andrews
- Trey McBride

### Preferred GPP stack families
1. Lawrence + Jacksonville receiver + Higgins
2. Stroud + Nico Collins + CeeDee/Pickens
3. Mahomes + Rashee Rice + Bowers/Jeanty
4. Stafford + Puka + Philadelphia value
5. Purdy + Kittle + Denver bring-back

### GPP philosophy
Weight ceiling, correlation, and lower-owned paths more heavily. Avoid combining every obvious chalk piece in the same lineup.

## Current analysis takeaway

- Single entry: JAX-CIN is the cleanest primary environment.
- Large-field GPP: DAL-HOU and less-obvious JAX-CIN constructions provide stronger differentiation.
- Braelon Allen is the most important injury-created value after Breece Hall was ruled out.
- Nico Collins' return makes Houston more attractive but forces a re-check of Dalton Schultz's target projection.
- Philadelphia target concentration must be re-projected with DeVonta Smith and Dallas Goedert out.

## Next steps

1. Refresh projection inputs for injury-driven role changes.
2. Re-run the projection model and statistical layer.
3. Import the latest ownership source.
4. Compare our projections against the field.
5. Prune to the final SE and GPP pools.
6. Build candidate lineups.


---

# Sunday, October 4 Update — From Player Pool to Lineup Construction

The Saturday player pool was intentionally broad. Sunday morning moved from "who is worth researching?" to "which complete single-entry constructions make sense?"

## What changed

The main changes were:

1. **JAX-CIN remained the primary game environment.**
2. **DAL-HOU became the main leverage alternative.**
3. **Braelon Allen and Jordan Addison were treated as role-based value, not just cheap salary.**
4. **The lineup process stopped treating every value play equally.**
5. **Complete lineups were compared with upper-tail / variance analysis instead of only median projection.**
6. **Ownership was used as a tiebreaker, not as the first reason to select a player.**

## Sunday single-entry shortlist

### Primary Cincinnati stack

```text
Joe Burrow
+ Ja'Marr Chase
+ Tee Higgins
+ Jacksonville bring-back
```

This construction became the preferred single-entry family because the game offers the strongest combined scoring environment and the Cincinnati pieces can reach their ceiling together.

Two Jacksonville bring-backs were compared:

- **Parker Washington** for the stronger raw projection / ceiling version.
- **Jakobi Meyers** for the less-obvious ownership-adjusted version.

### Main pivot

```text
C.J. Stroud
+ Nico Collins
+ George Pickens bring-back
```

This is the preferred major game-environment pivot if JAX-CIN becomes too concentrated in the field.

## Value rules learned from Week 3

The Sunday process uses a stricter value filter.

A value player must have:

- a believable snap / route / touch role,
- enough ceiling to matter in a tournament,
- and a reason the salary has not caught up.

Cheap salary by itself is no longer enough.

That is why Braelon Allen and Jordan Addison were treated as stronger values than uncertain replacement receivers.

## Current ranking

1. Burrow + Chase + Higgins + Jakobi Meyers — preferred ownership-adjusted SE construction.
2. Burrow + Chase + Higgins + Parker Washington — highest raw exploratory ceiling.
3. Stroud + Nico Collins + George Pickens — strongest major pivot.

See [Sunday single-entry variance analysis](se_variance_analysis_2026-10-04.md) for the full beginner-friendly walkthrough and simulation notes.

## Final caution

This remains a **pre-lock** research snapshot.

Official inactive news and any meaningful last-minute role changes can still move players in or out of the final lineup.
