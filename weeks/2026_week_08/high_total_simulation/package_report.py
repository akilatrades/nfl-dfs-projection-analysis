"""Package five alternatives from the executed simulation results."""
import json
from pathlib import Path

R=Path(__file__).resolve().parent
inputs=json.loads((R/'inputs.json').read_text())
pool=inputs['pool'];byname={p['name']:p for p in pool}
results={r['family']:r for r in json.loads((R/'results.json').read_text())}
choices=[
 ('dak_mcbride','Dak / McBride — first preference',
  'Dak Prescott','Bucky Irving','Bhayshul Tuten','CeeDee Lamb','Kendrick Bourne','Malik Washington','Trey McBride','Rhamondre Stevenson','Chargers'),
 ('brissett_mcbride','Brissett / McBride / Wilson — Arizona passing stack',
  'Jacoby Brissett','Chase Brown','Rhamondre Stevenson','CeeDee Lamb','Michael Wilson',"Wan'Dale Robinson",'Trey McBride','Demario Douglas','Chargers'),
 ('dak_javonte','Dak / Lamb / Javonte — Dallas offense',
  'Dak Prescott','Javonte Williams','Jonah Coleman','CeeDee Lamb',"Ja'Marr Chase",'Malik Washington','Hunter Henry','Rhamondre Stevenson','Chargers'),
 ('allen_single','Allen / Shakir / Flowers — Buffalo lead',
  'Josh Allen','Jonah Coleman','Rhamondre Stevenson','Zay Flowers','Khalil Shakir','Puka Nacua','Hunter Henry','Malik Washington','Broncos'),
 ('lamar_single','Lamar / Flowers / Shakir — Baltimore lead',
  'Lamar Jackson','Chase Brown','Rhamondre Stevenson','Zay Flowers',"Ja'Marr Chase",'Khalil Shakir','Brenton Strange',"Wan'Dale Robinson",'Raiders'),
]
slots=['QB','RB1','RB2','WR1','WR2','WR3','TE','FLEX','DST']
final=[]
for number,(family,label,*names) in enumerate(choices,1):
 r=results[family]
 assert set(names)==set(r['players']) and len(set(names))==9
 line=dict(zip(slots,names))
 for slot,name in line.items():
  pos=byname[name]['pos']
  assert pos==slot[:2] if slot.startswith(('RB','WR')) else (pos in ['RB','WR','TE'] if slot=='FLEX' else pos==slot)
 assert sum(byname[n]['salary'] for n in names)==r['salary']<=50000
 final.append(dict(number=number,label=label,family=family,slots=line,salary=r['salary'],
                   baseline=r['base_mean'],simulation=r['base'],
                   secondary=r['secondary_projection'],role_downside=r['role_downside'],
                   low_correlation=r['low_correlation'],high_games_cold=r['high_games_cold']))
assert len({tuple(sorted(x['slots'].values())) for x in final})==5
(R/'five_lineups.json').write_text(json.dumps(final,indent=2)+'\n')
table=['| Slot | 1: Dak–McBride | 2: Brissett | 3: Dallas offense | 4: Allen | 5: Lamar |',
       '|---|---|---|---|---|---|']
for slot in slots:
 table.append('| '+slot+' | '+' | '.join(x['slots'][slot] for x in final)+' |')
table.append('| Salary | '+' | '.join(f"${x['salary']:,}" for x in final)+' |')
table.append('| Baseline points | '+' | '.join(f"{x['baseline']:.1f}" for x in final)+' |')
table.append('| Simulated P90 | '+' | '.join(f"{x['simulation']['p90']:.0f}" for x in final)+' |')
(R/'lineup_table.md').write_text('\n'.join(table)+'\n')
print('\n'.join(table))
