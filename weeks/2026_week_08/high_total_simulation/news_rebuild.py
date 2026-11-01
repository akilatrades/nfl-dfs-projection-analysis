"""Rebuild with confirmed active Moore, Kincaid, Pickens and Hall-out Braelon."""
import json
import inspect
from pathlib import Path
import numpy as np
import run as m
ROOT=Path(__file__).resolve().parent
p=m.load_pool()
for name,pos,team,opp,salary,mean in [('Braelon Allen','RB','NYJ','LV',6100,19.4),('DJ Moore','WR','BUF','BAL',5700,11.7),('Dalton Kincaid','TE','BUF','BAL',5300,12.),('George Pickens','WR','DAL','ARI',6600,15.4)]:
 p.append(dict(name=name,pos=pos,team=team,opp=opp,salary=salary,forecast=mean))
latest={'Josh Allen':23,'Dak Prescott':21.6,'Joe Burrow':21.2,'Lamar Jackson':20,'Drake Maye':19.8,'Trevor Lawrence':19.3,'Jacoby Brissett':18.5,'Jared Goff':18,'Baker Mayfield':16.7,'Jahmyr Gibbs':27.9,'Bijan Robinson':25,'James Cook III':19.6,'Braelon Allen':19.4,'Javonte Williams':19,'Rhamondre Stevenson':18.9,'Bucky Irving':18.3,'Chase Brown':18.1,'Kyren Williams':17.9,'Jaylen Warren':17.8,'Bhayshul Tuten':17.5,'Derrick Henry':16.1,'Ashton Jeanty':15.8,'Tony Pollard':14.2,'Jonathan Taylor':14,'Jonah Coleman':11.9,'Jeremiyah Love':10.6,'Puka Nacua':22,'CeeDee Lamb':19.7,"Ja'Marr Chase":18.9,'Zay Flowers':18.8,'Tee Higgins':16.9,'Drake London':16.8,'Justin Jefferson':15.8,'George Pickens':15.4,'Parker Washington':14.8,'Michael Wilson':14.3,'Garrett Wilson':14,'DK Metcalf':12.5,"Wan'Dale Robinson":11.8,'DJ Moore':11.7,'Jameson Williams':11.6,'Tre Tucker':11,'Khalil Shakir':10.8,'KC Concepcion':10.7,'Demario Douglas':10.4,'Chris Godwin':10.4,'Ryan Flournoy':10.2,'Germie Bernard':9.9,'Malik Washington':9.9,'Kendrick Bourne':9.6,'Omar Cooper Jr.':9.4,"Ja'Kobi Lane":8.1,'Trey McBride':18.7,'Brock Bowers':16.5,'Hunter Henry':12.2,'Dalton Kincaid':12,'Sam LaPorta':11.6,'Brenton Strange':11.5,'T.J. Hockenson':11,'Cade Otton':9.6,'Kyle Pitts':9.2,'Mark Andrews':8.8,'Bengals':7.7,'Jaguars':7.5,'Steelers':7.4,'Rams':7.3,'Browns':6.1,'Broncos':6,'Lions':5.9,'Buccaneers':5.8,'Raiders':5.7,'Falcons':5.6,'Chargers':4.48}
# Require an explicit current observation for every candidate except disclosed
# Chargers defense (retains earlier mean, unavailable on the public second board).
p=[v for v in p if v['name'] in latest and v['name'] not in ["Ja'Kobi Lane", 'Kendrick Bourne']]
# Final quality control: at most one WR below $5,000. Prior lessons flag
# buying expensive cores with multiple uncertain cheap receiving roles.
source=inspect.getsource(m.generate).replace("p['salary']<5000 for p in pool],0,2)","p['salary']<5000 for p in pool],0,1)")
exec(source,m.__dict__)
for v in p:v['forecast']=latest[v['name']]
m.SECONDARY.update(latest)
m.REC['BUF'].update({'DJ Moore':.30,'Dalton Kincaid':.22})
m.REC['DAL']['George Pickens']=.25
m.REC['NYJ']['Braelon Allen']=.12
m.RUSH['NYJ']['Braelon Allen']=.80
m.TEAM['BUF']=(28.5,.56,.48);m.TEAM['BAL']=(25,.64,.36)
for t in m.REC:assert sum(m.REC[t].values())<=1
m.FAMILIES={'allen_moore':['Josh Allen','DJ Moore','Zay Flowers'],'allen_kincaid':['Josh Allen','Dalton Kincaid','Zay Flowers'],'allen_shakir':['Josh Allen','Khalil Shakir','Zay Flowers'],'dak_mcbride':['Dak Prescott','CeeDee Lamb','Trey McBride'],'brissett_mcbride':['Jacoby Brissett','Trey McBride','CeeDee Lamb'],'lamar_moore':['Lamar Jackson','Zay Flowers','DJ Moore']}
m.SEED=202611019
c=m.generate(p)
train=m.simulate(p,20000,202611020)
for v in c:v['train']=m.metrics(train[:,v['ids']].sum(axis=1))
chosen=[]
for f in m.FAMILIES:
 opts=[v for v in c if v['family']==f]
 best=max(opts,key=lambda v:(v['train']['p200'],v['train']['p95']))
 chosen.append(dict(best))
# Retain the immediately preceding recommendation as a benchmark.
byname={v['name']:i for i,v in enumerate(p)}
benchmark=['Josh Allen','Braelon Allen','Rhamondre Stevenson','Zay Flowers','Drake London','DJ Moore','Brenton Strange',"Wan'Dale Robinson",'Broncos']
chosen.append({'family':'prior_moore_benchmark','ids':[byname[n] for n in benchmark]})
for scenario,seed in [('base',202611021),('low_correlation',202611022),('role_downside',202611023),('high_games_cold',202611024)]:
 s=m.simulate(p,150000,seed,scenario)
 if scenario=='role_downside':
  for name,mult in [('Braelon Allen',.9),('DJ Moore',.85),('Dalton Kincaid',.85),('George Pickens',.85)]:s[:,byname[name]]*=mult
 for v in chosen:v[scenario]=m.metrics(s[:,v['ids']].sum(axis=1))
for v in chosen:
 ids=v['ids'];m.validate(p,ids);v['players']=[p[i] for i in ids];v['salary']=sum(p[i]['salary'] for i in ids);v['projection']=round(sum(p[i]['forecast'] for i in ids),2)
report={'projection_board':'SPAGS November 1 12:03 PM ET; Chargers previous mean 4.48','players':len(p),'candidate_count':len(c),'draws':620000,'training_draws':20000,'holdout_per_scenario':150000,'new_assumptions':{'BUF_implied':28.5,'BAL_implied':25,'Moore_receiving_TD_share':.30,'Kincaid_receiving_TD_share':.22,'Pickens_receiving_TD_share':.25,'Braelon_receiving_TD_share':.12,'Braelon_rushing_TD_share':.8,'new_role_stress':{'Moore':.85,'Kincaid':.85,'Pickens':.85,'Braelon':.9}},'quality_controls':'Exclude Lane/Bourne thin-role discounts; at most one WR under 5000; remaining original constraints retained. These are judgment choices, not statistical discoveries.','limits':'Exploratory score proxy, not field simulation. Analyst shares/variance not calibrated. Other game totals frozen; ownership and duplication not modeled. Public salaries, not official contest export. Every family fixes a declared core, not every player. Six families plus preceding recommendation benchmark.','results':chosen}
(ROOT/'news_rebuild_inputs.json').write_text(json.dumps({'pool':p,'TEAM':m.TEAM,'REC':m.REC,'RUSH':m.RUSH},indent=2)+'\n')
(ROOT/'news_rebuild_results.json').write_text(json.dumps(report,indent=2)+'\n')
(ROOT/'news_rebuild_candidates.json').write_text(json.dumps(c,separators=(',',':'))+'\n')
print(json.dumps([dict(family=v['family'],salary=v['salary'],projection=v['projection'],players=[p['name'] for p in v['players']],base=v['base'],stress=v['role_downside']['mean']) for v in chosen],indent=2))
