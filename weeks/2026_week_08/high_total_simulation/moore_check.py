"""Explicit Moore versus Shakir comparison after both confirmed active."""
import json
from pathlib import Path
exec(Path(__file__).with_name('final_check.py').read_text().split('out={}')[0])
p.append(dict(name='DJ Moore',pos='WR',team='BUF',opp='BAL',salary=5700,forecast=11.7))
m.REC['BUF']['DJ Moore']=.30
idx={v['name']:i for i,v in enumerate(p)}
old=cores+rest['balanced_london']
new=[('DJ Moore' if n=='Khalil Shakir' else 'Broncos' if n=='Browns' else n) for n in old]
out={}
for label,names in [('shakir_browns',old),('moore_broncos',new)]:
 ids=[idx[n] for n in names];m.validate(p,ids)
 out[label]={'players':names,'salary':sum(p[i]['salary'] for i in ids),'projection':round(sum(p[i]['forecast'] for i in ids),2)}
for v,seed in [('base',192),('low_correlation',193),('role_downside',194)]:
 s=m.simulate(p,100000,2026110100+seed,v)
 if v=='role_downside':
  s[:,idx['Braelon Allen']]*=.9
  s[:,idx['DJ Moore']]*=.85
 for label,names in [('shakir_browns',old),('moore_broncos',new)]:out[label][v]=m.metrics(s[:,[idx[n] for n in names]].sum(axis=1))
report={'draws':300000,'assumptions':'Moore 30% of BUF receiving TDs, analyst assumption, others retain prior shares. Moore 15% role stress explicitly added, matching Shakir stress but not an empirical injury probability. Latest projection board 12:03 ET. This is exploratory score-proxy comparison, not calibrated winning odds. Prior comparisons held Shakir fixed and did not evaluate Moore.','results':out}
Path(__file__).with_name('moore_check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
