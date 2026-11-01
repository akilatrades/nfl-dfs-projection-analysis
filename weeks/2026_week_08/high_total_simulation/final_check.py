"""Final prelock comparison: SPAGS Nov 1 12:03 ET means; frozen score-proxy assumptions."""
import json
from pathlib import Path
import run as m
p=m.load_pool()
p.append(dict(name='Braelon Allen',pos='RB',team='NYJ',opp='LV',salary=6100,forecast=19.4))
latest={'Josh Allen':23.,'Braelon Allen':19.4,'Rhamondre Stevenson':18.9,'Zay Flowers':18.8,'Khalil Shakir':10.8,'Puka Nacua':22.,'Jonah Coleman':11.9,'Malik Washington':9.9,'Hunter Henry':12.2,'Browns':6.1,'Broncos':6.,'Drake London':16.8,'Brenton Strange':11.5,"Wan'Dale Robinson":11.8,'Demario Douglas':10.4,'Parker Washington':14.8,'Chase Brown':18.1,'Bucky Irving':18.3,'Chris Godwin':10.4}
for v in p:
 if v['name'] in latest:v['forecast']=latest[v['name']]
m.REC['NYJ']['Braelon Allen']=.12
m.RUSH['NYJ']['Braelon Allen']=.80
idx={v['name']:i for i,v in enumerate(p)}
cores=['Josh Allen','Zay Flowers','Khalil Shakir','Rhamondre Stevenson']
rest={
'original_puka':['Jonah Coleman','Puka Nacua','Hunter Henry','Malik Washington','Broncos'],
'balanced_london':['Braelon Allen','Drake London','Brenton Strange',"Wan'Dale Robinson",'Browns'],
'balanced_parker':['Braelon Allen','Parker Washington','Hunter Henry',"Wan'Dale Robinson",'Browns'],
'balanced_douglas':['Braelon Allen','Drake London','Brenton Strange','Demario Douglas','Broncos'],
'bucky_three_rb':['Braelon Allen','Bucky Irving','Chris Godwin','Brenton Strange','Browns'],
'chase_three_rb':['Braelon Allen','Chase Brown','Chris Godwin','Brenton Strange','Browns']}
out={}
for name,extra in rest.items():
 names=cores+extra; ids=[idx[n] for n in names];m.validate(p,ids)
 out[name]=dict(players=names,salary=sum(p[i]['salary'] for i in ids),projection=round(sum(p[i]['forecast'] for i in ids),2))
for scenario,seed in [('base',91),('low_correlation',92),('role_downside',93),('high_games_cold',94)]:
 s=m.simulate(p,100000,2026110100+seed,scenario)
 if scenario=='role_downside':s[:,idx['Braelon Allen']]*=.90
 for name,extra in rest.items():out[name][scenario]=m.metrics(s[:,[idx[n] for n in cores+extra]].sum(axis=1))
report={'projection_source':'https://splashplaypodcast.com/dfs/nfl/players/ (Nov 1 12:03 PM ET)','draws_per_scenario':100000,'scenarios':4,'total_slate_draws':400000,'new_analyst_assumptions':{'Braelon Allen receiving TD share':.12,'Braelon Allen rushing TD share':.80,'Braelon role downside multiplier':.90},'limitations':'Score proxy only; frozen earlier team totals and other variance/TD shares. Not actual opponent field, duplication or contest win probability. Salary uses public boards, not official contest export. Candidate comparison is exploratory.','latest_means':latest,'results':out}
Path(__file__).with_name('final_check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(out,indent=2))
