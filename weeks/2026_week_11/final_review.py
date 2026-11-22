"""Held-out final comparison, including explicit portfolio and inactive alternatives."""
import copy
import json
import numpy as np
from run import ROOT, SEED, dump, evaluate_candidates, field_evaluate, fit_field_weights, generate_field, simulate, validate

pool=json.loads((ROOT/'inputs.json').read_text())
candidates=json.loads((ROOT/'candidates.json').read_text())
chosen_ids=[47,71,79,253,632,633]
chosen=[candidates[i] for i in chosen_ids]
scores,_=simulate(pool,200000,SEED+700)
metrics=evaluate_candidates(pool,chosen,scores)
stress={}
for label in ['lower_forecasts','role_uncertainty','chicago_weather']:
    altered=copy.deepcopy(pool)
    for p in altered:
        if label=='lower_forecasts':p['mean']=min(p[k] for k in ['mean','spags','fsc','ftn'] if k in p)
        elif label=='role_uncertainty':p['mean']*={'Emmett Johnson':.75,'Jonah Coleman':.85,'Carnell Tate':.75,'Elic Ayomanor':.8}.get(p['name'],1.)
        elif p['team'] in ['CHI','NO'] and p['pos'] in ['QB','WR','TE']:p['mean']*=.9
    sc,_=simulate(altered,75000,SEED+701)
    stress[label]=evaluate_candidates(altered,chosen,sc)
field_results={}
for label in ['base','flatter']:
    field=np.load(ROOT/f'field_{label}.npy')
    field_results[label]=field_evaluate(pool,chosen,field,10000,SEED+702)
# A more projection-conscious field checks the effect of weak synthetic opposition.
weights,targets,history=fit_field_weights(pool,1.)
field,audit=generate_field(pool,12253,np.random.default_rng(SEED+703),fitted_weights=weights,min_projection=135.)
audit.update(targets=targets.tolist(),fit_history=history)
audit['minimum_projection']=135.
dump('field_stronger_audit.json',audit)
field_results['stronger']=field_evaluate(pool,chosen,field,10000,SEED+702)
result={'draws':200000,'seed':SEED+700,'metrics':metrics,'stress':stress,'fields':field_results,'note':'Hypothetical restricted fields and analyst distributions; no validated real contest win/ROI or uniqueness probability.'}
dump('final_comparison.json',result)
for x in metrics:print(x['candidate_id'],x['projection'],x['p50'],x['p95'],x['p_gt_200'])
assert all(validate(c['ids'],pool) for c in chosen)
