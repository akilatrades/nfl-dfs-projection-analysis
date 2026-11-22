"""Check whether Gibbs constructions depend on an under-owned synthetic Gibbs."""
import copy
import json
import numpy as np
from run import ROOT, SEED, dump, field_evaluate, fit_field_weights, generate_field

pool=json.loads((ROOT/'inputs.json').read_text())
altered=copy.deepcopy(pool)
for p in altered:
    if p['name']=='Jahmyr Gibbs':
        p['own']=p['published_ownership']=20.
        p['own_source']='deliberate hypothetical ownership stress, not a published forecast'
weights,targets,history=fit_field_weights(altered,1.)
field,audit=generate_field(altered,12253,np.random.default_rng(SEED+800),fitted_weights=weights)
audit.update(targets=targets.tolist(),fit_history=history,note='Gibbs target 20% is a hypothetical ownership stress, not observed ownership.')
dump('field_gibbs_chalk_audit.json',audit)
candidates=json.loads((ROOT/'candidates.json').read_text())
chosen=[candidates[i] for i in [47,71,79,253,632,633]]
result=field_evaluate(pool,chosen,field,10000,SEED+702)
dump('field_gibbs_chalk_results.json',result)
print(next(x for x in audit['marginals'] if x['name']=='Jahmyr Gibbs'))
