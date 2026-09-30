# Data

This project builds its own NFL DraftKings projections.

The data workflow separates **inputs we know before the slate** from **results we learn after the games**.

That separation is important because the model should be judged using only information that was available before lineup lock.

## Pre-slate inputs

The model can use public football information and our own assumptions, including:

- DraftKings salary,
- expected pass attempts,
- completion rate,
- yards per completion,
- expected passing touchdowns,
- expected interceptions,
- expected carries,
- yards per carry,
- expected rushing touchdowns,
- expected targets,
- catch rate,
- yards per reception,
- expected receiving touchdowns,
- recent DraftKings scoring volatility,
- game total,
- team total,
- injury/news adjustments,
- and role notes.

These inputs create the project's own fantasy-point projection.

## Why the inputs are stored

A final projection by itself does not explain very much.

For example:

```text
Player projection = 18.4 DK points
```

does not tell us why the player projected for 18.4.

The input file lets us trace the number back to assumptions such as:

```text
targets
catch rate
yards per reception
touchdown expectation
```

If the projection misses badly, we can then identify which assumption was wrong.

## Week-level projection input file

Each slate can use a file named:

`projection_inputs.csv`

The offensive-player columns are:

```text
player
position
team
opponent
salary

pass_attempts
completion_rate
yards_per_completion
pass_td
interceptions

rush_attempts
yards_per_carry
rush_td

targets
catch_rate
yards_per_reception
rec_td

fumbles_lost
expected_two_point_conversions

prob_300_pass
prob_100_rush
prob_100_rec

recent_dk_std
team_total
game_total
our_ownership_estimate
role_note
correlation_note
leverage_note
decision
reason
```

Different positions use different columns.

A wide receiver, for example, can leave the passing columns blank.

A quarterback can leave most receiving columns blank.

## DST inputs

DST uses a different set of expected events:

```text
expected_sacks
expected_dst_interceptions
expected_fumble_recoveries
expected_dst_tds
expected_safeties
expected_blocks
expected_points_allowed_score
```

The points-allowed value is entered as an expected DraftKings scoring value because the real DST points-allowed system uses scoring ranges rather than one smooth formula.

## Model outputs

Running:

```bash
python run_projections.py weeks/2026_week_04/projection_inputs.csv
```

creates:

`weeks/2026_week_04/player_pool.csv`

The output includes:

- model projection,
- model floor,
- model ceiling,
- value per $1,000 of salary,
- our ownership estimate,
- role notes,
- correlation notes,
- leverage notes,
- and lineup decision notes.

## Post-slate data

After the games, the project can add:

- actual DraftKings points,
- actual ownership,
- actual carries,
- actual targets,
- actual routes,
- actual touchdowns,
- lineup score,
- contest finish,
- projection error,
- and ownership error.

The post-slate data is used to determine **why** the model was right or wrong and what should change the following week.
