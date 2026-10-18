# 2026 Week 6 — single-entry research

> **Sunday, October 18 update:** The Friday provisional Bryce Young decision below has been superseded for the **$5 single-entry / ~23,000 entrants** contest after reviewing newer projections, ownership and official Friday injury designations. See [Sunday contest lineup and pre-lock checks](sunday_2026-10-18/single_entry_5usd_23k.md). The new entry is **provisional, not confirmed entered or locked**.

**Status: pre-slate, October 17.** Nothing entered yet. This week's inputs come from the data rather than my own assumptions: every player's volume and efficiency is their Week 1–5 rate shrunk toward a position baseline (`src/input_model.py`), lines come from the schedule file, and salaries from three published articles (`sources.md`). That is the change from Week 5, where every input was something I typed in. If the fitted inputs do worse than the hand-set ones did, that is worth knowing too.

## What the pool says

54 players with published salaries across the ten afternoon games. The leading mean build and the builds that survive every news scenario land within three points of each other, which is the first time the stress screen has not cost much.

| Build | Salary | Mean | Worst single scenario | All scenarios at once |
|---|---:|---:|---:|---:|
| Stafford stack (Adams, Higbee) + Walker, Kyren, Vele, Coker, Likely, CAR DST | $50,000 | **144.8** | 141.0 | 137.9 |
| Young stack (Coker) + Walker, Kyren, Nacua, Bourne, Likely, Higbee, CAR DST | $49,700 | 144.2 | 141.2 | **141.2** |
| Shough stack (Vele) + Warren, Kyren, Adams, Nacua, Likely, Higbee, CAR DST | $49,900 | 144.3 | 139.8 | 132.9 |
| Allen stack (Shakir) + Walker, Kyren, Adams, Bourne, Likely, Higbee, CAR DST | $49,400 | 142.7 | 139.6 | 139.6 |
| Caleb Williams stack (Burden) | $49,700 | 141.9 | 120.9 | 117.8 |

Full table: `candidate_comparison.csv`; rosters: `candidate_lineups.csv`; the scenario multipliers are in `run_week6_research.py` and were written before any lineup was built.

## What every build agrees on

- **The Rams game.** LA is implied for 32 points against Arizona, the highest team total on the slate by three points. Kyren Williams, Davante Adams or Puka Nacua, and Tyler Higbee at $3,400 appear in nearly every build. The risk is the obvious one: a 12.5-point favourite can also sit its starters in the fourth quarter.
- **Kenneth Walker** at $8,500 is the top RB projection (87 carries and 19 targets in four games) and the model pays for him in every construction.
- **Isaiah Likely** at $4,800 with 48 targets in five games is the best TE value in the pool.
- **Panthers DST** is the cheapest of the three defenses with a salary and faces the lowest-total game; with only three defenses published, this is a pool artefact as much as a view.

## What I need to know before lock

1. **Lamar Jackson** (day-to-day Friday). If he plays, Huntley is out of every build; none of the leading builds use him.
2. **Chris Olave** (did not practice Thursday). Vele's role in the Stafford build depends on Olave sitting; the Young build does not use Vele.
3. **Blake Corum's share.** The Kyren Williams builds assume ~85% of his Week 1–5 workload at worst; if the Friday report suggests a real split, the Walker–Warren constructions replace him.
4. **Caleb Williams** (questionable, full practice Thursday). His builds project lowest even if he plays, so his status matters only for the Bears pass catchers.
5. **Saquon Barkley** back makes Dameon Pierce a non-play; no leading build uses him.

## Provisional decision

If the Friday designations clear items 1–3, the **Young stack build** is the entry: it gives up half a point of mean for a floor that holds under every scenario at once, which is the lesson I took from Weeks 4 and 5. If Olave is out, the Stafford build's extra three points of mean come from a confirmed role, and it becomes the entry instead. Final choice recorded Sunday morning in `sunday_2026-10-18/`.

These are scenario estimates of my own lineups' scores, not win probabilities; the field, ownership and duplication are not modelled.
