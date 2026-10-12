"""Week 5 2026 DraftKings Classic: reproducible box-score scoring audit.

Run from repository root:
  python weeks/2026_week_05/postslate_2026-10-11/score_week5.py

Freeze the two original entered rosters. Source stats were transcribed from dated
postgame box scores; verify against DraftKings official contest scoring before
reporting cashes, ranks or prizes. Standard-library only.
"""
from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path

OUT = Path(__file__).resolve().parent
# Frozen analyst/public midpoint used in the October 11 lineup-selection research.
# This is NOT the later event-constrained 180K Monte Carlo's simulated mean.
PLAYERS = {
    "Jordan Love":         dict(pos="QB",pass_yd=367,pass_td=2,rush_yd=6,pass_2pt=1, prior="18.047",source="GB_CHI"),
    "Chase Brown":         dict(pos="RB",rush_yd=39,rec=3,rec_yd=21,prior="16.7645",source="CIN_MIA"),
    "D'Andre Swift":      dict(pos="RB",rush_yd=43,rush_td=1,rec=4,rec_yd=30,prior="16.1915",source="GB_CHI"),
    "Michael Wilson":     dict(pos="WR",pass_yd=7,rec=4,rec_yd=30,prior="15.694",source="DET_ARI"),
    "Christian Watson":   dict(pos="WR",rec=6,rec_yd=143,rec_td=2,prior="15.0425",source="GB_CHI"),
    "Jameson Williams":   dict(pos="WR",rec=2,rec_yd=47,rec_td=2,prior="12.135",source="DET_ARI"),
    "Hunter Henry":       dict(pos="TE",rec=3,rec_yd=44,rec_td=1,prior="8.755",source="LV_NE"),
    "Trey McBride":       dict(pos="TE",rec=9,rec_yd=66,rec_td=1,prior="16.146",source="DET_ARI"),
    "Chargers DST":       dict(pos="DST",pa=23,sacks=1,frecoveries=1,prior="5.44",source="DEN_LAC"),
    "Jared Goff":         dict(pos="QB",pass_yd=271,pass_td=3,rush_yd=1,rush_td=1,prior="19.5245",source="DET_ARI"),
    "Aaron Jones Sr.":    dict(pos="RB",rush_yd=113,rush_td=1,rec=3,rec_yd=4,fumbles_lost=1,prior="15.6",source="MIN_NO"),
    "Amon-Ra St. Brown":  dict(pos="WR",rec=6,rec_yd=69,prior="18.17",source="DET_ARI"),
    "Luther Burden III":  dict(pos="WR",rush_yd=2,rec=4,rec_yd=47,prior="14.7",source="GB_CHI"),
    "Tre Tucker":         dict(pos="WR",rush_yd=-6,rec=4,rec_yd=41,prior="11.1",source="LV_NE"),
    "Sam LaPorta":       dict(pos="TE",rec=5,rec_yd=88,rec_td=1,prior="12.27",source="DET_ARI"),
    "George Kittle":     dict(pos="TE",rec=5,rec_yd=24,prior="14.059",source="SF_SEA"),
}
LINEUPS = {
    "5usd_23k": ["Jordan Love","Chase Brown","D'Andre Swift","Michael Wilson",
                 "Christian Watson","Jameson Williams","Hunter Henry","Trey McBride","Chargers DST"],
    "3usd_7k": ["Jared Goff","Chase Brown","Aaron Jones Sr.","Amon-Ra St. Brown",
                "Luther Burden III","Tre Tucker","Sam LaPorta","George Kittle","Chargers DST"],
}
# Archived final Poisson team-TD game simulation means, rather than a rank model.
FINAL_MODEL_MEANS = {"5usd_23k":Decimal("123.20"),"3usd_7k":Decimal("126.44")}
SOURCES = {
    "GB_CHI":"https://www.footballdb.com/games/boxscore/chicago-bears-vs-green-bay-packers-2026101112",
    "CIN_MIA":"https://www.statmuse.com/nfl/ask/chase-brown-receiving-stats-this-season",
    "DET_ARI":"https://www.statmuse.com/nfl/game/10-11-2026-ari-vs-det-19139",
    "LV_NE":"https://www.statmuse.com/nfl/game/10-11-2026-lv-at-ne-19132",
    "MIN_NO":"https://www.neworleanssaints.com/game-day/2026/reg-week5/vikings-at-saints/box-score",
    "SF_SEA":"https://www.statmuse.com/nfl/game/10-11-2026-sf-at-sea-19140",
    "DEN_LAC":"https://www.statmuse.com/nfl/game/10-11-2026-lac-vs-den-19137",
}
D = lambda x: Decimal(str(x))
def dk(p):
    if p["pos"]=="DST":
        pa=p["pa"]
        allowed = 10 if pa==0 else 7 if pa<=6 else 4 if pa<=13 else 1 if pa<=20 else 0 if pa<=27 else -1 if pa<=34 else -4
        return D(allowed+p.get("sacks",0)+2*p.get("ints",0)+2*p.get("frecoveries",0)+6*p.get("def_tds",0))
    return (
        D(p.get("pass_yd",0))*D(".04")+D(p.get("pass_td",0))*4
        - D(p.get("pass_int",0))+D(p.get("rush_yd",0))*D(".1")
        +D(p.get("rush_td",0))*6+D(p.get("rec",0))
        +D(p.get("rec_yd",0))*D(".1")+D(p.get("rec_td",0))*6
        +D(p.get("pass_2pt",0)+p.get("rush_2pt",0)+p.get("rec_2pt",0))*2
        -D(p.get("fumbles_lost",0))
        +D(3 if p.get("pass_yd",0)>=300 else 0)
        +D(3 if p.get("rush_yd",0)>=100 else 0)
        +D(3 if p.get("rec_yd",0)>=100 else 0)
    )

def main():
    rows=[];lineup_sums={}
    for lineup,names in LINEUPS.items():
        assert len(names)==9 and len(set(names))==9
        total=D(0);prior=D(0)
        for name in names:
            stats=PLAYERS[name]
            actual=dk(stats)
            previous=D(stats["prior"])
            total+=actual;prior+=previous
            rows.append(dict(contest=lineup,position=stats["pos"],player=name,
                prior_mean=f"{previous:.2f}",actual_dk=f"{actual:.2f}",
                forecast_error=f"{actual-previous:.2f}",source=SOURCES[stats["source"]]))
        lineup_sums[lineup]=dict(
            observed=f"{total:.2f}",old_mean=f"{prior:.2f}",
            new_monte_carlo_mean=f"{FINAL_MODEL_MEANS[lineup]:.2f}",
            residual_v_final=f"{total-FINAL_MODEL_MEANS[lineup]:.2f}",
            residual_v_old=f"{total-prior:.2f}")
    assert lineup_sums["5usd_23k"]["observed"]=="153.86"
    assert lineup_sums["3usd_7k"]["observed"]=="120.14"
    with (OUT/"entered_player_results.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    with (OUT/"lineup_summary.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.writer(f);w.writerow(["contest","actual_dk_from_box_score",
             "archived_mean","final_poisson_mc_mean","error_vs_final","error_vs_archived",
             "contest_rank","official_dk_score","payout"])
        for c,v in lineup_sums.items():
            w.writerow([c,v["observed"],v["old_mean"],v["new_monte_carlo_mean"],
                        v["residual_v_final"],v["residual_v_old"],"unknown","unverified","unknown"])
    print(lineup_sums)

if __name__=="__main__":
    main()
