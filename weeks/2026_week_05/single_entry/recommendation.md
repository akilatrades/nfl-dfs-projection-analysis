# One lineup for 4,000–6,000 entries

**October 8 research decision: use this $49,900 build as the current single-entry recommendation for Sunday, October 11.** The requested 4–6k is interpreted as entries. Exact contest and payouts are still unknown. Published salaries need matching to the actual contest, and final availability is pending. No entry has been submitted.

| Slot | Player | Salary |
|---|---|---:|
| QB | Jacoby Brissett | $5,500 |
| RB | Chase Brown | $6,900 |
| RB | Quinshon Judkins | $5,700 |
| WR | Amon-Ra St. Brown | $7,900 |
| WR | Michael Wilson | $6,200 |
| WR | Rome Odunze | $4,700 |
| TE | Dalton Schultz | $4,000 |
| FLEX | Trey McBride | $6,700 |
| DST | Chargers | $2,300 |
| **Total** | **$100 unused** | **$49,900** |

## Why this construction

For this tournament field, the analyst choice is a concentrated scoring path: Brissett with two pass catchers and St. Brown from the opposing team. A productive Arizona passing game can score for all three stack members, while Detroit scoring can sustain Arizona's passing volume. Correlation also concentrates failure risk. This is a construction preference, not proof that double stacks outperform single stacks in this contest.

[DraftKings Network's October 8 research](https://dknetwork.draftkings.com/2026/10/08/nfl-dfs-tournament-picks-high-upside-draftkings-gpp-plays-for-week-5/) lists DET–ARI at 54.5 and Brissett at $5,500. His price saves $1,100 versus Goff and makes Wilson, McBride and St. Brown together affordable. Our individual QB projection actually favors Goff, 20.55 to 18.34. Brissett is the salary-allocation choice, not a claim that he is the better quarterback.

The build holds Warren and Emanuel Wilson because their assumptions depend on unresolved backfield competition. It also keeps the earlier holds on speculative Cincinnati receivers, Diggs and Bagent. These are selection choices, not inactive designations. Brown remains sensitive to Cincinnati's receiving availability, and Odunze remains sensitive to Chicago's quarterback situation.

McBride takes FLEX because he starts later than Schultz. Two tight ends are allowed in this construction; McBride is included as an Arizona pass catcher, not because the model has established that two-TE rosters are better. The Chargers defense is a salary tradeoff. The $100 left over is not evidence of uniqueness. No ownership claim or forced low-owned punt supports this selection.

## What the comparison establishes

The new screen maximizes the existing joint workload stress, excludes Warren/Emanuel and the earlier holds, and requires an opposing skill player. It tests minimum one- and two-pass-catcher stacks for Brissett, Maye and Goff. Six specifications produce five unique rosters: Brissett's one-catcher minimum naturally returns the same double stack.

| Construction | Salary | Base projection | Joint workload stress | QB-team passing stress |
|---|---:|---:|---:|---:|
| **Brissett double + Detroit** | **$49,900** | **133.33** | **131.82** | **123.05** |
| Goff single + Arizona | $49,900 | 132.28 | 130.77 | 123.99 |
| Goff double + Arizona | $49,700 | 130.82 | 129.30 | 120.27 |
| Maye single + Las Vegas | $50,000 | 127.61 | 126.10 | 122.33 |
| Maye double + Las Vegas | $50,000 | 126.53 | 125.02 | 119.18 |

The passing diagnostic applies the same rule to each quarterback's team: QB attempts, passing TD expectation and passing-bonus probability ×0.8; that team's RB/WR/TE targets, receiving TD expectation and receiving-bonus probability ×0.8. It is evaluated on each fixed roster separately from the joint workload stress, without assigning probabilities or re-optimizing. It is not a full simulation of a failed game environment.

Goff's single stack holds up better in that diagnostic. The roughly one-point base advantage for Brissett is too small to establish superiority under these manual assumptions. The recommendation is an analyst choice among researched constructions, not a tournament-EV optimum. The 35-player pool and required bring-back particularly limit Maye's comparison. Field size does not numerically alter the projections or objective; payouts, field lineups and calibrated ownership are missing.

## The main weak point and change triggers

Judkins is Cleveland's listed starting RB, but his saved **18 carries at 4.1 yards/carry** is above the reported first-four-game pace of **14.75 carries and 3.0 yards/carry**. Holding all other inputs constant and using 15 carries at 3.0 lowers his projection by **2.88** and the lineup to **130.45**. That is a sensitivity, not a revised forecast: his recent receiving volume is higher than our saved receiving assumption. See [dated sources](../sources.md). Do not call his role or this lineup safe.

- If Judkins' role or the salary export does not support this allocation, rebuild the entire roster. Do not preserve the double stack by inserting an unsupported cheap player.
- Recheck Brown's receiving assumptions and Chicago's starter before lock. Confirm all nine players are active and on the contest slate; check weather for the outdoor games.
- Reopen Warren/Emanuel only after evaluating the returning backs' likely workloads. An active designation alone does not resolve a committee.
- If Arizona's outlook weakens, the saved Goff single-stack candidate is the first researched alternative. It changes several positions and is not a one-player late swap. Locked players must be preserved in any actual late-swap rebuild.

## Reproduce

Run `python run_single_entry_field.py`. `profile.json` records the target, holds and analyst-selected candidate. `field_comparison.csv` and `field_lineups.csv` preserve alternatives; `recommended_lineup.csv` is the selected roster; `field_manifest.json` hashes inputs, code and outputs. These are research files, not DraftKings upload files. The earlier nine-specification comparison remains available via `python run_single_entry.py`.
