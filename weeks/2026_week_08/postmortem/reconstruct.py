"""Reconstruct the saved selected roster, not a verified DraftKings entry export."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
rows=[
 ('Lamar Jackson',20.,dict(pass_yd=0,pass_td=0)),
 ('Bijan Robinson',25.,dict(rush_yd=76)),
 ('Braelon Allen',19.4,dict(rush_yd=147,rush_td=1,rec=2,rec_yd=6)),
 ('Zay Flowers',18.8,dict(rec=0,rec_yd=0)),
 ("Wan'Dale Robinson",11.8,dict(rec=6,rec_yd=57,rec_td=1,lost_fumbles=1)),
 ('DJ Moore',11.7,dict(rec=4,rec_yd=82,rec_td=1,rush_yd=4,lost_fumbles=1)),
 ('Mark Andrews',8.8,dict(rec=3,rec_yd=14)),
 ('Rhamondre Stevenson',18.9,dict(rush_yd=82,rec=3,rec_yd=8)),
 ('Broncos',6.,dict(sacks=2,interceptions=0,recoveries=0,points_allowed=24,def_td=0,blocks=0,safeties=0))]
def points(s):
 if 'points_allowed' in s:
  pa=s['points_allowed'];allowed=10 if pa==0 else 7 if pa<=6 else 4 if pa<=13 else 1 if pa<=20 else 0 if pa<=27 else -1 if pa<=34 else -4
  return s['sacks']+2*(s['interceptions']+s['recoveries']+s['blocks']+s['safeties'])+6*s['def_td']+allowed
 return round(.04*s.get('pass_yd',0)+4*s.get('pass_td',0)-s.get('pass_int',0)+.1*(s.get('rush_yd',0)+s.get('rec_yd',0))+6*(s.get('rush_td',0)+s.get('rec_td',0))+s.get('rec',0)-s.get('lost_fumbles',0)+2*s.get('two_pt',0)+3*sum(s.get(k,0)>=v for k,v in [('pass_yd',300),('rush_yd',100),('rec_yd',100)]),2)
out=[dict(player=n,projection=p,stats=s,reconstructed_dk=points(s),error=round(points(s)-p,2)) for n,p,s in rows]
actual=round(sum(x['reconstructed_dk'] for x in out),2);expected=round(sum(x['projection'] for x in out),2)
bal=[v for v in out if v['player'] in ['Lamar Jackson','Zay Flowers','Mark Andrews']]
report=dict(slate_date='2026-11-01',review_date='2026-11-02',status='provisional_box_score_reconstruction',entry_verified=False,assumption='Saved Lamar/Bijan roster retained DJ Moore; no final export or screenshot supplied and no replacement reported.',projection=expected,reconstructed_dk=actual,error=round(actual-expected,2),baltimore_projection=sum(v['projection'] for v in bal),baltimore_actual=sum(v['reconstructed_dk'] for v in bal),baltimore_deficit=round(sum(v['projection']-v['reconstructed_dk'] for v in bal),2),rank=None,payout=None,net_profit=None,players=out)
assert expected==140.4 and actual==86.6
assert points(dict(rush_yd=147,rush_td=1,rec=2,rec_yd=6))==26.3
(ROOT/'reconstructed_results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
