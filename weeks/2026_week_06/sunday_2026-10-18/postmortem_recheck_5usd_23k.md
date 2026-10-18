# Week 6 Sunday 10:50 CT — postmortem recheck and lineup revision

**Contest:** DraftKings $5 single entry, ~23,000 contestants, 2026-10-18.  
**Status:** provisional research *only*; not a DK contest export or locked entry.

## Explicit lessons applied from prior weeks

From [Week 5 postmortem](../../2026_week_05/postslate_2026-10-11/README.md) and [Week 5 process review](../../2026_week_05/sunday_2026-10-11/process_review_2026-10-11/README.md): $5 lineup 153.86 DK; $3 lineup 120.14 DK, **without final placement, actual ownership or winnings**. The $5 Love–Watson link produced 63.58 DK points; receiver TD allocation defeated the alternative Goff triple stack. Avoid forced runbacks, value receivers lacking credible 20+ outcomes, confusing good team offense with RB scoring, and fading premium RBs purely for low ownership. From [Week 4 audit](../../2026_week_04/audit_2026-10-08/README.md): snapshot accuracy/incomplete inputs mean no validated simulator edge.

## Refreshed objective screen

A local, single-slot binary integer program screened a **114-player curated salary-confirmed pool** (16 QB, 32 RB, 38 WR, 16 TE, 12 DST; not the complete DK export). Constraints: exactly 1 QB, 2+ RB, 3+ WR, 1+ TE, 1 DST, 9 distinct players, $50k salary cap, QB with >=1 teammate WR/TE, and no DST versus rostered opposing offense. Linear baseline uses 60% October 18 SPAGS point projection, 40% October 18 dfsroto where present; missing secondary forecast uses SPAGS with a 0.5-point uncertainty penalty. **The 60/40 weight and penalty are analyst assumptions, not fitted or validated probabilities.** This is an *expected-score* optimizer, NOT a top-1% payout equity optimizer.

| Construction | Salary | SPAGS additive mean | 60/40 comparison estimate | Note |
|---|---:|---:|---:|---|
| Original Stafford / Kyren / Pierce / Puka / Keenan / Tucker / McBride / Worthy / CAR | $49,700 | 133.8 | ~127.6* | Pierce lacks comparable second-source projection; CAR DST vs PHI Pierce, opposing-outcome conflict |
| Strict best 60/40 projection Stafford / Bijan / Kyren / Cook / Nabers / Keenan / Germie / Higbee / CAR | $50,000 | 141.8 | 134.4 | Highest modeled additive mean, *but* thin Stafford–Higbee catch-share link, Germie punt, no Puka |
| **Selected tournament alternative:** Stafford / Kyren / Cook / Chuba / Puka / Worthy / Keenan / Higbee / CAR | **$49,800** | **142.8** | **134.0** | Stafford–Puka direct correlation; avoids Pierce–CAR conflict; strong 3-RB opportunity, but 4 Rams and Higbee role risk |
| Stafford / Bijan / Cook / Allgeier / Puka / Worthy / Germie / Higbee / CAR, excluding Kyren | $49,900 | unreported | 131.8 | Weaker mean and multiple cheap fragile roles; no automatic reason to fade Kyren |

*The old lineup's cross-source comparison is not wholly comparable: no dfsroto entry for Pierce; his SPAGS 12.5 was retained with small penalty. The one-source 133.8 → 142.8 comparison is apples-to-apples as of the latest SPAGS board. Additive means omit lineup correlations.*

### Provisional revised roster

| DK position | Player | Team | Salary |
|---|---|---|---:|
| QB | Matthew Stafford | LAR | $6,400 |
| RB | Kyren Williams | LAR | $6,800 |
| RB | James Cook III | BUF | $7,400 |
| WR | Puka Nacua | LAR | $8,100 |
| WR | Keenan Allen | IND | $4,300 |
| WR | Xavier Worthy | KC | $4,600 |
| TE | Tyler Higbee | LAR | $3,400 |
| FLEX | Chuba Hubbard | CAR | $6,300 |
| DST | Panthers | CAR | $2,500 |

Salary $49,800. For late swap flexibility, list Chuba in an RB slot, Kyren at FLEX only if the platform permits the resulting slot assignment and it preserves all position rules. Since Kyren starts later than Chuba, this keeps a late FLEX decision available.

## Why Kyren survives a Stafford build

Stafford's passing TD and Kyren's rushing TD outcomes are partially competing, but all Rams offensive pieces can succeed together in an exceptional LA scoring day, especially via Kyren receiving scores. Kyren's projection 21.5 on SPAGS and 19.9 on dfsroto at $6,800 make removing him costly in these constrained lineup comparisons. This does **not** prove the Stafford–Kyren–Puka combination is the optimal tournament correlation; Kyren ownership, LA -12.5 spread, possible late Corum carries and thin Higbee target share remain meaningful risks. No calibrated joint outcome, duplicate-lineup model or opponent-field simulation exists.

## Reliability controls before noon CT

- Official 1 p.m. ET inactives on PHI–CAR, IND–TEN, etc. Check Chuba, Keenan, Panthers.
- Rams/Chiefs/Bills players kick off later: confirm late injury statuses and DK contest eligibility; using Worthy at FLEX gives late swap optionality.
- Forecast disagreement: Walker SPAGS 25.6 vs dfsroto 13.2, Chuba 18.6 vs 11.3; cannot simply trust one site's #1 values.
- Do NOT claim highest probability of winning 23,000 entries. Needed: validated projections of all players, correlations, actual contest opponent lineup distributions and payout structure.

## Sources

- SPAGS, updated 10:56 a.m. ET Sunday: https://splashplaypodcast.com/dfs/nfl/rb-rankings/ ; https://splashplaypodcast.com/dfs/nfl/wr-rankings/ ; https://splashplaypodcast.com/dfs/nfl/qb-rankings/ ; https://splashplaypodcast.com/dfs/nfl/te-rankings/ ; https://splashplaypodcast.com/dfs/nfl/dst-rankings/
- Independent open slate projections: https://dfsroto.win/projections
- Ownership (Friday historical, no current actual ownership): https://covertheslate.com/nfl-week-6-draftkings-ownership-2026/
- DraftKings injury report (Oct 18): https://dknetwork.draftkings.com/2026/10/13/nfl-injury-report-week-6/


## 10:56 AM ET projection follow-up — why no Arizona bring-back

**The zero-run-back result was not intentionally constrained:** the original projection optimizer required a QB/WR-TE teammate but **did not mandate** a player from the opposing team. We should have audited the implication of carrying four Rams (Stafford, Puka, Kyren, Higbee) in a 23K GPP. A bring-back may help when Cardinals scoring keeps Stafford throwing, but the Rams are -12.5 and a Rams-dominant scoring script is plausible without Arizona ceiling production. Making an unproductive bring-back **mandatory** would repeat Weeks 3–5's error.

Using the same publicly posted Sunday 10:56 a.m. ET SPAGS projections from https://splashplaypodcast.com/dfs/nfl/players/:

| Valid construction | DK Salary | Published *additive* projected DK points | LAR / ARI pieces | Notes |
|---|---:|---:|---|---|
| **Current (retain)**: Stafford / Cook / Chuba / Puka / Keenan / Worthy / Higbee / Kyren / CAR DST | **$49,800** | **142.8** | 4 / 0 | Best of these three on additive projection; script is Rams onslaught, not necessarily close game |
| **Cheap run-back**: Replace Keenan Allen ($4,300, 11.0) with Kendrick Bourne ($4,000, 8.0) | $49,500 | 139.8 | 4 / 1 | -3.0 model points; Bourne ~4.7 estimated targets, low ceiling relative to reliable role |
| **Strong run-back**: Replace Kyren ($6,800, 21.5) with Trey McBride FLEX ($7,200, 17.9) AND Keenan ($4,300, 11.0) with Germie Bernard ($4,000, 9.8) | $49,900 | 138.0 | 3 / 1 | Credible McBride volume (~11.3 targets), avoids four Rams, but -4.8 additive points and loses Kyren value; now double TE with Higbee |

**Decision:** retain original $49,800 construction rather than force a low-opportunity Arizona bring-back. This is a conscious game-script *choice made after review*, not proof it optimizes win probability. A large-field payoff/ownership simulator with realistic game correlations could select McBride instead, and this comparison cannot adjudicate that. Label all projection precision as uncalibrated and all ownership estimates as historical Friday estimates. Inactives/contest salary IDs remain a prelock requirement.

Sources: https://splashplaypodcast.com/dfs/nfl/players/ (updated October 18 10:56 AM ET), https://covertheslate.com/nfl-week-6-draftkings-ownership-2026/ (Friday ownership snapshot retained Oct 18).
