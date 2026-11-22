"""Audit saved recommendations, salary arithmetic, source labels and roster overlap."""
import json
from collections import Counter
from run import ROOT, GAMES, dump, validate

pool=json.loads((ROOT/'inputs.json').read_text())
candidates=json.loads((ROOT/'candidates.json').read_text())
recommendations=json.loads((ROOT/'recommendations.json').read_text())
assert len({p['name'] for p in pool})==len(pool)
assert all(p['game'] in GAMES and p['team'] in GAMES[p['game']][1] for p in pool)
assert all(p['own_source']!='analyst assumption, not a published forecast' for p in pool if 'published_ownership' in p)
assert len({tuple(c['ids']) for c in candidates})==len(candidates)
assert all(validate(c['ids'],pool) for c in candidates)
for c in recommendations['lineups']:
    assert validate(c['ids'],pool)
    assert c['salary']==sum(pool[i]['salary'] for i in c['ids'])
    assert abs(c['projection']-sum(pool[i]['mean'] for i in c['ids']))<.001
    assert Counter(p['pos'] for p in c['slots'])==Counter(pool[i]['pos'] for i in c['ids'])
    assert len({p['name'] for p in c['slots']})==9
    assert next(p for p in c['slots'] if p['slot']=='FLEX')['name']=='Jonah Coleman'
shared=set(recommendations['lineups'][0]['ids']) & set(recommendations['lineups'][1]['ids'])
assert {pool[i]['name'] for i in shared}=={'Emmett Johnson','Jonah Coleman','Sam LaPorta'}
dump('final_verification.json',{'all_634_candidates_legal':True,'recommended_salaries':[x['salary'] for x in recommendations['lineups']],'shared_players':[pool[i]['name'] for i in sorted(shared)],'pool_players':len(pool),'two_or_more_projection_sources':sum('fsc' in p or 'ftn' in p for p in pool),'official_dk_export_verified':False,'official_inactives_verified':False,'contest_sizes_assumed':[5882,12254],'week_10_results_supplied':False,'not_entered_by_assistant':True})
print((ROOT/'final_verification.json').read_text())
