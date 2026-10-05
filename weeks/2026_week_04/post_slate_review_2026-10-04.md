# 2026 Week 4 — Post-Slate Review

**Slate date:** October 4, 2026  
**Contest set:** $50 single entry (4,545 entries), $27 single entry (3,239 entries), $20 Millionaire (161,764 entries)

## Audit note

The Week 4 repository contained extensive pre-lock analysis, but `final_lineup.csv` was left as TBD before kickoff.

That created an avoidable audit problem after the slate because multiple candidate lineups existed in the analysis. This review records the final contest assignments from the chat history. The $20 Millionaire lineup was not committed before lock and is explicitly marked as reconstructed from the final chat.

Starting Week 5, the exact entered lineup for every contest must be committed before kickoff.

## Final scores

| Contest | Entries | Salary | DK points |
|---|---:|---:|---:|
| $50 Single Entry | 4,545 | $49,800 | **153.62** |
| $27 Single Entry | 3,239 | $49,800 | **137.52** |
| $20 Millionaire | 161,764 | $49,800 | **153.62** |

Contest finish, cash line, and actual player ownership are not yet recorded. Those should be imported from DraftKings if available rather than guessed.

## Player results used in the review

| Player | DK points | Review |
|---|---:|---|
| Joe Burrow | 28.72 | Strong QB result despite only one passing TD |
| Kyren Williams | 36.70 | Elite ceiling hit |
| James Cook | 16.30 | Fine outcome, not a tournament separator |
| Braelon Allen | 8.70 | Role thesis did not turn into ceiling |
| Ja'Marr Chase | 5.70 | Concussion; classify primarily as injury variance |
| Tee Higgins | 29.70 | Strong hit |
| Jordan Addison | 9.20 | Modest result |
| T.J. Hockenson | 27.90 | Strong hit |
| Parker Washington | 2.00 | Major process-review target |
| Jakobi Meyers | 6.30 | Ownership pivot did not create enough scoring |
| Rams DST | 5.00 | Acceptable but not a separator |

## What worked

The Week 3 process correction was directionally right.

We started with game environment and correlation instead of cheap isolated value. The Cincinnati stack produced useful scoring through Burrow and Higgins. Kyren Williams and T.J. Hockenson were excellent ceiling plays.

The lineup therefore was not a case where every projection failed.

## Variance versus process

### Injury variance

Ja'Marr Chase left with a concussion and finished at 5.70 DK points.

That should not be treated as evidence that the pre-lock Chase projection was bad. The correct classification is largely injury variance.

### Process issues

Parker Washington produced only 2.00 DK points. Unlike the Chase injury, this deserves a stronger process review because Parker was deliberately used as a bring-back in the highest-priority game environment.

More importantly, the portfolio carried too much of the same Cincinnati/Jacksonville thesis across all three contests.

The $50 single entry and the 161,764-entry Millionaire used the same lineup. That is not ideal portfolio construction because those contests reward different risk profiles.

## Main Week 4 lesson

Week 3 exposed a **lineup-construction problem**.

Week 4 exposed a **portfolio and model-validation problem**.

The next process must optimize not only a single lineup, but the relationship between all entries.

## Week 5 changes

1. **Commit final entries before lock.**
   - One exact record for every entered contest.
   - No TBD placeholders.
   - Candidate lineups remain separate from entered lineups.

2. **Use contest-specific objectives.**
   - $50 SE: strong median plus P90/P95 and modest leverage.
   - $27 SE: similar structure but allow more variance.
   - Large-field Milly: prioritize P99 / first-place path, duplication risk, and scenario leverage rather than reusing the best SE lineup.

3. **Add portfolio exposure controls.**
   - Track how many of the three lineups use the same QB, primary stack, bring-back, and value core.
   - Do not let one game environment control the entire portfolio unless the edge is exceptional and explicitly documented.

4. **Model lineup-level ownership and duplication.**
   - Individual projected ownership is not enough.
   - Estimate how common the full combination of popular pieces is likely to be.

5. **Move defense and matchup adjustments earlier.**
   - Use pressure rate, explosive-play allowance, pace, pass rate, target share by position, RB receiving allowance, and red-zone tendencies before lineup generation.

6. **Make the correlated simulator reproducible.**
   - Read assumptions from CSV.
   - Save player means and volatility.
   - Save team/game factors and correlations.
   - Use a fixed random seed.
   - Save simulation settings and lineup distributions to CSV.

7. **Track forecast error every week.**
   - Projected DK points vs actual.
   - Projected ownership vs actual.
   - Projection error by position and role.
   - Whether the role assumption itself was right or wrong.

8. **Run a pre-lock 'what beats us?' test.**
   - Identify the most plausible alternate game environment.
   - Ensure at least one portfolio entry represents a coherent alternate slate story when appropriate.

## Week 5 workflow

```text
injuries / roles
    ->
game environments
    ->
defense + matchup adjustments
    ->
8-12 coherent lineup families
    ->
correlated simulations
    ->
ownership + duplication adjustment
    ->
contest-specific lineup selection
    ->
portfolio exposure review
    ->
commit exact entered lineups before lock
    ->
post-slate results + forecast-error review
```

The goal is not to chase the players who scored the most in Week 4. The goal is to make the decision process reproducible and improve the parts that failed for repeatable reasons.
