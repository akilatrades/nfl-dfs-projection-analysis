# Week 5 Saturday injury-scenario refresh — October 10, 2026

**Slate:** DraftKings NFL Classic Sunday October 11, 2026, eleven afternoon games; **single-entry fields with at least 1,000 entrants**. Thursday, London, Sunday night and Monday night are excluded. The exact contest, entry fee, and official salary/player-ID export remain unverified.

This is a **provisional Saturday scenario screen**, not a final entry, a fitted forecast, a prediction of payout, or a verified projection of ownership. The October 9 analysis remains unchanged at [single_entry_2026-10-09](../single_entry_2026-10-09/README.md).

## New inputs: observed news versus subjective changes

| Observed event, sourced October 10 | Decision in our analyst model |
|---|---|
| Marvin Harrison Jr. will not play Sunday against Detroit while Arizona considers a trade | Michael Wilson: targets **8.5 to 9.0**, expected receiving TD **0.40 to 0.45**. Trey McBride: targets **10.0 to 10.75**, expected receiving TD **0.45 to 0.50**. Brissett's team pass attempts/TDs unchanged to avoid double-counting. |
| Chicago lists Kyle Monangai **OUT**; Swift finished with a full Friday practice and no game designation | Add D'Andre Swift at **$6,200** (published salary, not contest CSV): 18.5 rush attempts, 4.4 YPC, 0.55 rushing TD, 4.5 targets, 72% catch, 6.8 yards/reception, 0.12 rec TD, bonus probabilities 0.22 rush / 0.02 rec. This is a possible workload, not guaranteed usage. |
| Seattle lists Zach Charbonnet **OUT**; George Holani **questionable**; Seattle recently signed Joe Mixon | Reopen Emanuel Wilson from the October 9 hold **without boosting** his 16 carry / 3 target model input. Committee uncertainty remains material. |
| Pittsburgh officially lists Michael Pittman Jr. **OUT**; Rico Dowdle **questionable** | Keep Metcalf's existing eight-target analyst prior. Jaylen Warren remains held in this screen pending Dowdle and role resolution. |
| Cincinnati lists both Ja'Marr Chase and Tee Higgins **QUESTIONABLE** | Continue holding speculative replacement receivers Tinsley and Meyers; keep Chase Brown's assumption but stress it if both wideouts return. |
| Chicago named Tyson Bagent Week 5 starter despite Caleb Williams being listed questionable | Keep Bagent in the QB pool, without assuming his recent efficiency repeats. |

Sources: [Reuters Harrison report](https://www.reuters.com/sports/report-cards-finalizing-trade-wr-marvin-harrison-jr--flm-2026-10-10/), [Bears official injury update](https://www.chicagobears.com/news/injury-update-bears-rb-kyle-monangai-ruled-out-qb-caleb-williams-questionable-for-packers-game), [Seattle injury table](https://www.seahawks.com/team/injury-report/), [Steelers injury table](https://www.steelers.com/team/injury-report/), [Bengals injury table](https://www.bengals.com/team/injury-report/), [Stokastic Week 5 salary reference](https://www.stokastic.com/articles/nfl-dfs/nfl-week-5-dfs-picks-draftkings-strategy).

**Reprojected player means**, using the same transparent DraftKings scoring equation from `src/projections.py`: Michael Wilson **16.688**, McBride **19.1923**, Swift **18.2832**, Emanuel Wilson **14.693**. Each is an analyst scenario; neither uncertainty nor target competition is fitted to a historical distribution.

## Fresh salary-constrained lineup screen

An independent exhaustive roster enumeration using the repository's scoring equation and equivalent roster restrictions produced these provisional constructions. The new `run_week5_saturday.py` reproduces the scenario using the repository's SciPy MILP optimizer and writes timestamped CSV and manifest files when executed. **The repository Python runner has not been executed as part of this commit**, so no generated CSV or passing test is claimed yet.

| Slot | 1,000–3,000 (Maye) | 4,000–6,000 (Brissett) | 15,000–25,000 (Bagent) | Gibbs alternative |
|---|---|---|---|---|
| QB | Drake Maye $6,300 | Jacoby Brissett $5,500 | Tyson Bagent $4,700 | Jacoby Brissett $5,500 |
| RB | Emanuel Wilson $5,300 | Emanuel Wilson $5,300 | Chase Brown $6,900 | Emanuel Wilson $5,300 |
| RB | D'Andre Swift $6,200 | D'Andre Swift $6,200 | D'Andre Swift $6,200 | D'Andre Swift $6,200 |
| WR | Amon-Ra St. Brown $7,900 | Amon-Ra St. Brown $7,900 | Michael Wilson $6,200 | Michael Wilson $6,200 |
| WR | Michael Wilson $6,200 | Michael Wilson $6,200 | Rome Odunze $4,700 | Rome Odunze $4,700 |
| WR | DK Metcalf $5,400 | DK Metcalf $5,400 | Christian Watson $6,400 | DK Metcalf $5,400 |
| TE | Hunter Henry $3,700 | Dalton Schultz $4,000 | Colston Loveland $4,600 | Dalton Schultz $4,000 |
| FLEX | Trey McBride $6,700 | Trey McBride $6,700 | Trey McBride $6,700 | Jahmyr Gibbs $9,800 |
| DST | Chargers $2,300 | Browns $2,800 | Texans $3,400 | Browns $2,800 |
| **Salary** | **$50,000** | **$50,000** | **$49,800** | **$49,900** |
| **Manual mean sum** | **138.88** | **138.81** | **134.75** | **136.78** |

These are *construction scenarios*, not proven best lineups for their field sizes. In particular, the Bears double pass stack plus Swift in the Bagent build can suffer if Chicago scores mostly via the run; an optimistic Swift workload can also compete with Bagent's passing TD upside. Likewise, the Detroit/Arizona concentration in the Brissett build brings correlated upside **and** downside. No full-slate ownership, player-ID, field simulation, probability of first place or payout model was run. The pool is 44 hand-researched players, not the full available slate.

**Saturday pool holds:** Tinsley, Meyers, Stefon Diggs, Jaylen Warren, Braelon Allen. Emanuel Wilson is released from hold, **but only conditionally**, with Holani/Mixon involvement unresolved. The Gibbs option is a meaningful alternative even though it trails the listed Brissett mean by approximately 2.04 points; the model does not evaluate whether its upper-tail outcome justifies that salary tradeoff.

## Pre-lock decision gate

1. **Sunday before noon Central:** verify all 1 p.m. player inactives, especially Chase/Higgins, Minnesota receivers, Dowdle, and Swift; reassess Chase Brown, Hockenson and any Pittsburgh alternatives.
2. Confirm Emanuel Wilson's committee role (Holani and Mixon) and Arizona's receiving hierarchy; both Seattle and Arizona play late, so do not rely on late-news flexibility after locking early players.
3. Check exact contest salary and IDs, weather, final market totals and ownership. These lineups are not DraftKings import-ready CSVs.
4. Rerun `python run_week5_saturday.py`, save the input and output hashes, lock a pregame decision, then collect actual contest rank, ownership and payout after the games.

No statistical evidence currently demonstrates that moving from a 1,000-player field to a 25,000-player field makes any one of these candidate lineups higher-EV.
