"""Independent seeds and explicit adverse assumptions; none has an assigned probability."""
import copy
import json
import numpy as np
from run import ROOT, SEED, dump, evaluate_candidates, simulate, validate

pool=json.loads((ROOT/'inputs.json').read_text())
candidates=json.loads((ROOT/'candidates.json').read_text())
results={}
for label in ['lower_forecasts','role_uncertainty','chicago_weather','less_variance']:
    changed=copy.deepcopy(pool)
    for p in changed:
        if label=='lower_forecasts':
            p['mean']=min(p[k] for k in ['mean','spags','fsc','ftn'] if k in p)
        elif label=='role_uncertainty':
            p['mean']*= {'Emmett Johnson':.75,'Jonah Coleman':.85,'Carnell Tate':.75,'Elic Ayomanor':.8,'Dawson Knox':.8,'Brevyn Spann-Ford':.8}.get(p['name'],1.)
        elif label=='chicago_weather' and p['team'] in ['CHI','NO'] and p['pos'] in ['QB','WR','TE']:
            p['mean']*=.9
    scores,_=simulate(changed,50000,SEED+100,.8 if label=='less_variance' else 1.)
    metrics=evaluate_candidates(changed,candidates,scores)
    results[label]=[{k:c[k] for k in ['candidate_id','projection','p95','p99','p_gt_200']} for c in metrics]
scores,_=simulate(pool,100000,SEED+200)
ids={p['name']:i for i,p in enumerate(pool)}
pairs=[('Dak Prescott','CeeDee Lamb'),('Dak Prescott','George Pickens'),('Caleb Williams','Colston Loveland'),('Cam Ward','Carnell Tate'),('Jared Goff','Amon-Ra St. Brown')]
sanity={'max_mean_error':max(abs(float(scores[:,i].mean())-p['mean']) for i,p in enumerate(pool)), 'all_rosters_legal':all(validate(c['ids'],pool) for c in candidates),'all_scores_finite':bool(np.isfinite(scores).all()),'pair_correlations':{a+' / '+b:float(np.corrcoef(scores[:,ids[a]],scores[:,ids[b]])[0,1]) for a,b in pairs},'draws_per_stress':50000,'sanity_draws':100000,'note':'No measured probability for adverse roles/weather/QB exit. Non-TD gamma approximates PPR/yardage/bonuses; offense turnover negatives absent.'}
assert sanity['max_mean_error']<.65 and sanity['all_rosters_legal'] and sanity['all_scores_finite']
dump('sensitivity_results.json',results)
dump('simulation_sanity.json',sanity)
print(json.dumps(sanity,indent=2))
