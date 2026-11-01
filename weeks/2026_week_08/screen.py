"""Reproduce a curated-pool expected-score screen, not contest payout EV."""
import json
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from pathlib import Path

# Published FantasySportsCentral Week 8 forecasts; no analyst injury boosts.
# name, position, team, opponent, salary, published DK forecast
rows = '''Dak Prescott,QB,DAL,ARI,6300,22.31
Joe Burrow,QB,CIN,TEN,7000,22.53
Lamar Jackson,QB,BAL,BUF,6800,20.38
Drake Maye,QB,NE,MIA,6500,21.15
Josh Allen,QB,BUF,BAL,7700,24.63
Trevor Lawrence,QB,JAX,IND,6200,20.41
Rhamondre Stevenson,RB,NE,MIA,5600,17
Chase Brown,RB,CIN,TEN,6300,17.38
Tony Pollard,RB,TEN,CIN,5800,14.50
Bucky Irving,RB,TB,ATL,6400,16.96
Javonte Williams,RB,DAL,ARI,7300,18.72
Bijan Robinson,RB,ATL,TB,8500,22.23
Jahmyr Gibbs,RB,DET,MIN,9500,24
Jonah Coleman,RB,DEN,KC,4300,11.63
CeeDee Lamb,WR,DAL,ARI,8100,21.38
Ja'Marr Chase,WR,CIN,TEN,7700,20.42
Zay Flowers,WR,BAL,BUF,7200,18.49
Tee Higgins,WR,CIN,TEN,6700,16.67
Puka Nacua,WR,LAR,LAC,8600,22.94
Wan'Dale Robinson,WR,TEN,CIN,4200,10.64
Malik Washington,WR,MIA,NE,4400,10.46
Michael Wilson,WR,ARI,DAL,6200,14.72
Garrett Wilson,WR,NYJ,LV,6300,15.35
Parker Washington,WR,JAX,IND,6500,16.10
Hunter Henry,TE,NE,MIA,4300,11.84
Brenton Strange,TE,JAX,IND,4000,11.21
Trey McBride,TE,ARI,DAL,7400,19.70
Mark Andrews,TE,BAL,BUF,3400,8.52
Khalil Shakir,WR,BUF,BAL,5600,9.83
Steelers,DST,PIT,CLE,3300,9.08
Browns,DST,CLE,PIT,2600,6.24
Broncos,DST,DEN,KC,2300,6.81
Lions,DST,DET,MIN,2700,7.06'''
pool=[]
for row in rows.splitlines():
    n,p,t,o,s,f=row.split(',');pool.append(dict(name=n,pos=p,team=t,opp=o,salary=int(s),forecast=float(f)))

def solve(qb, stress=False, premium=False, one_te=False):
    n=len(pool); a=[];lo=[];hi=[]
    def add(v,l,h):a.append(v);lo.append(l);hi.append(h)
    add([1]*n,9,9);add([p['salary'] for p in pool],0,50000)
    for pos,l,h in [('QB',1,1),('DST',1,1),('RB',2,3),('WR',3,4),('TE',1,1 if one_te else 2)]:
        add([int(p['pos']==pos) for p in pool],l,h)
    add([int(p['name']==qb) for p in pool],1,1)
    team=next(p['team'] for p in pool if p['name']==qb)
    add([int(p['team']==team and p['pos'] in ['WR','TE']) for p in pool],1,2)
    for team in set(p['team'] for p in pool):
        add([int(p['team']==team and p['pos']!='DST') for p in pool],0,3)
    for i,p in enumerate(pool):
        if p['pos']=='DST':
            for j,q in enumerate(pool):
                if q['team']==p['opp'] and q['pos']!='DST':
                    v=[0]*n;v[i]=v[j]=1;add(v,0,1)
    # Explicit analyst sensitivity: uncertain roles regress; no fitted probabilities.
    factors={'Rhamondre Stevenson':.85,'Tony Pollard':.85,"Wan'Dale Robinson":.75,'Jonah Coleman':.65,'Malik Washington':.85}
    values=[p['forecast']*(factors.get(p['name'],1) if stress else 1) for p in pool]
    if premium:add([int(p['name']=='Jahmyr Gibbs') for p in pool],1,1)
    out=milp(-np.array(values),integrality=np.ones(n),bounds=Bounds(0,1),constraints=LinearConstraint(np.array(a),lo,hi))
    assert out.success,out.message
    selected=[p for p,x in zip(pool,out.x) if x>.5]
    assert len(selected)==9 and sum(p['salary'] for p in selected)<=50000
    return dict(qb=qb,stress=stress,gibbs=premium,one_te=one_te,salary=sum(p['salary'] for p in selected),forecast=round(sum(p['forecast'] for p in selected),2),objective=round(-out.fun,2),players=[p['name'] for p in selected])

if __name__=='__main__':
    results=[solve(q,stress) for q in ['Dak Prescott','Joe Burrow','Lamar Jackson','Drake Maye','Josh Allen','Trevor Lawrence'] for stress in [False,True]]
    results.append(solve('Dak Prescott',False,True))
    results.extend(solve(q, s, one_te=True) for q in ['Dak Prescott','Joe Burrow','Drake Maye'] for s in [False,True])
    path=Path(__file__).parent
    (path/'pool.json').write_text(json.dumps(pool,indent=2)+'\n')
    (path/'comparison.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2))
