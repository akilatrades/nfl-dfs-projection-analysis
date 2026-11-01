"""Exploratory, TD-constrained score simulation; NOT calibrated contest win odds.

Run from any directory: python path/to/run.py
NumPy/SciPy only. All uncertainty parameters are explicit analyst assumptions.
"""
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

ROOT = Path(__file__).resolve().parent
SEED = 20261101
TRAIN_DRAWS = 20000
TEST_DRAWS = 150000

# Independent public SPAGS board, Nov 1 08:36 ET. Missing entries retain the
# primary forecast and are listed as missing in the final documentation.
SECONDARY = {
 'Josh Allen':22.9,'Dak Prescott':21.6,'Joe Burrow':20.8,'Drake Maye':20.2,
 'Lamar Jackson':20.0,'Trevor Lawrence':19.5,'Jacoby Brissett':18.5,
 'Jahmyr Gibbs':27.7,'Bijan Robinson':24.9,'James Cook III':19.6,
 'Javonte Williams':19.0,'Bucky Irving':18.3,'Rhamondre Stevenson':18.2,
 'Jaylen Warren':17.8,'Chase Brown':17.7,'Bhayshul Tuten':17.6,
 'Derrick Henry':15.8,'Ashton Jeanty':15.6,'Tony Pollard':14.2,
 'Jonah Coleman':11.1,'Jeremiyah Love':10.3,
 'Puka Nacua':21.6,'CeeDee Lamb':19.5,'Zay Flowers':18.3,
 "Ja'Marr Chase":17.8,'Drake London':16.6,'Tee Higgins':15.8,
 'Justin Jefferson':15.3,'Parker Washington':14.9,'Michael Wilson':13.7,
 'Garrett Wilson':13.7,'DK Metcalf':12.7,"Wan'Dale Robinson":11.7,
 'KC Concepcion':10.7,'Demario Douglas':10.6,'Tre Tucker':10.6,
 'Chris Godwin':10.5,'Khalil Shakir':10.4,'Ryan Flournoy':10.2,
 'Germie Bernard':10.0,'Malik Washington':9.9,'Kendrick Bourne':9.5,
 'Omar Cooper Jr.':9.2,"Ja'Kobi Lane":8.2,
 'Trey McBride':18.7,'Brock Bowers':16.4,'Hunter Henry':12.4,
 'Sam LaPorta':11.8,'T.J. Hockenson':11.0,'Brenton Strange':10.3,
 'Cade Otton':9.6,'Kyle Pitts':9.3,'Mark Andrews':8.8,
 'Bengals':7.7,'Jaguars':7.3,'Rams':7.3,'Steelers':7.3,
 'Broncos':6.1,'Browns':6.0,'Buccaneers':5.9,'Lions':5.9,'Raiders':5.7,
}


def load_pool():
    pool = json.loads((ROOT / 'base_pool.json').read_text())
    additions = '''Jacoby Brissett,QB,ARI,DAL,5700,18.89
James Cook III,RB,BUF,BAL,7900,17.63
Derrick Henry,RB,BAL,BUF,7200,17.01
Bhayshul Tuten,RB,JAX,IND,5900,15.81
Jaylen Warren,RB,PIT,CLE,6600,15.78
Ashton Jeanty,RB,LV,NYJ,6700,16.26
Jeremiyah Love,RB,ARI,DAL,5400,11.25
Chris Godwin,WR,TB,ATL,4800,11.60
Germie Bernard,WR,PIT,CLE,4900,10.82
KC Concepcion,WR,CLE,PIT,4700,10.82
DK Metcalf,WR,PIT,CLE,5400,12.19
Drake London,WR,ATL,TB,7000,17.39
Justin Jefferson,WR,MIN,DET,7100,17.03
Kendrick Bourne,WR,ARI,DAL,3900,9.59
Ryan Flournoy,WR,DAL,ARI,4600,9.69
Ja'Kobi Lane,WR,BAL,BUF,3400,6.91
Omar Cooper Jr.,WR,NYJ,LV,4800,10.27
Tre Tucker,WR,LV,NYJ,5500,10.91
Demario Douglas,WR,NE,MIA,4400,10.22
Jake Ferguson,TE,DAL,ARI,4100,7.19
T.J. Hockenson,TE,MIN,DET,4600,10.79
Sam LaPorta,TE,DET,MIN,5100,10.88
Kyle Pitts,TE,ATL,TB,4500,8.97
Brock Bowers,TE,LV,NYJ,7600,17.39
Cade Otton,TE,TB,ATL,3400,8.45
Rams,DST,LAR,LAC,3500,8.11
Jaguars,DST,JAX,IND,3700,8.54
Bengals,DST,CIN,TEN,3800,8.64
Raiders,DST,LV,NYJ,2500,6.10
Falcons,DST,ATL,TB,2500,6.16
Buccaneers,DST,TB,ATL,2900,6.31
Chargers,DST,LAC,LAR,2000,4.48
Jets,DST,NYJ,LV,2800,5.95'''
    for row in additions.splitlines():
        n,p,t,o,s,m = row.split(',')
        pool.append(dict(name=n,pos=p,team=t,opp=o,salary=int(s),forecast=float(m)))
    # Cross-source DST disagreement: use the lower published forecast where
    # FTN's public table has a second observation. Keep the original for audit.
    second_dst={'Broncos':5.3,'Steelers':8.1,'Lions':8.1}
    for p in pool:
        p['original_forecast']=p['forecast']
        if p['name'] in second_dst:
            p['forecast']=min(p['forecast'],second_dst[p['name']])
    assert len({p['name'] for p in pool}) == len(pool)
    return pool


# Team TD means inferred from implied points after an assumed six FG/other points.
# Values: implied points, pass TD fraction, QB share of rushing TDs.
TEAM = {
    'DAL':(30.75,.70,.03), 'ARI':(23.75,.69,.03),
    'BUF':(28.75,.56,.48), 'BAL':(25.75,.64,.36),
    'CIN':(29.5,.72,.04), 'TEN':(17,.48,.10),
    'NE':(25.25,.62,.17), 'MIA':(18.25,.55,.20),
    'TB':(22.5,.56,.03), 'ATL':(21,.62,.08),
    'JAX':(28.25,.63,.12), 'IND':(18.25,.58,.12),
    'MIN':(21.75,.63,.16), 'DET':(24.75,.64,.02),
    'NYJ':(24,.67,.05), 'LV':(22.5,.68,.02),
    'PIT':(21.5,.57,.02), 'CLE':(18,.53,.12),
    'LAR':(26,.67,.02), 'LAC':(19.5,.62,.08),
    'KC':(21,.62,.15), 'DEN':(19.5,.57,.13),
}

# TD allocation shares, not estimated target shares. Unlisted players consume
# all remaining scores; Q/OUT teammates are NOT silently removed from shares.
REC = {
 'DAL':{'CeeDee Lamb':.34,'Javonte Williams':.07,'Jake Ferguson':.14,'Ryan Flournoy':.08},
 'ARI':{'Trey McBride':.33,'Michael Wilson':.27,'Kendrick Bourne':.13,'Jeremiyah Love':.07},
 'BUF':{'Khalil Shakir':.22,'James Cook III':.10},
 'BAL':{'Zay Flowers':.35,'Mark Andrews':.20,"Ja'Kobi Lane":.13,'Derrick Henry':.04},
 'CIN':{"Ja'Marr Chase":.33,'Tee Higgins':.28,'Chase Brown':.10},
 'TEN':{"Wan'Dale Robinson":.23,'Tony Pollard':.08},
 'NE':{'Hunter Henry':.26,'Rhamondre Stevenson':.16,'Demario Douglas':.19},
 'MIA':{'Malik Washington':.30},
 'TB':{'Bucky Irving':.10,'Chris Godwin':.32,'Cade Otton':.22},
 'ATL':{'Bijan Robinson':.16,'Drake London':.40,'Kyle Pitts':.23},
 'JAX':{'Parker Washington':.34,'Brenton Strange':.18,'Bhayshul Tuten':.12},
 'IND':{},'MIN':{'Justin Jefferson':.43,'T.J. Hockenson':.22},
 'DET':{'Jahmyr Gibbs':.20,'Sam LaPorta':.20},
 'NYJ':{'Garrett Wilson':.37,'Omar Cooper Jr.':.24},
 'LV':{'Ashton Jeanty':.13,'Tre Tucker':.29,'Brock Bowers':.38},
 'PIT':{'Jaylen Warren':.12,'DK Metcalf':.38,'Germie Bernard':.28},
 'CLE':{'KC Concepcion':.30},'LAR':{'Puka Nacua':.45},
 'LAC':{},'KC':{},'DEN':{'Jonah Coleman':.18},
}
RUSH = {
 'DAL':{'Javonte Williams':.78},'ARI':{'Jeremiyah Love':.63},
 'BUF':{'James Cook III':.45},'BAL':{'Derrick Henry':.55},
 'CIN':{'Chase Brown':.72},'TEN':{'Tony Pollard':.79},
 'NE':{'Rhamondre Stevenson':.73},'MIA':{},
 'TB':{'Bucky Irving':.69},'ATL':{'Bijan Robinson':.80},
 'JAX':{'Bhayshul Tuten':.62},'IND':{},'MIN':{},
 'DET':{'Jahmyr Gibbs':.88},'NYJ':{},'LV':{'Ashton Jeanty':.78},
 'PIT':{'Jaylen Warren':.64},'CLE':{},'LAR':{},'LAC':{},
 'KC':{'Kenneth Walker III':.78},'DEN':{'Jonah Coleman':.40},
}

FAMILIES = {
 'dak_mcbride': ['Dak Prescott','CeeDee Lamb','Trey McBride'],
 'dak_javonte': ['Dak Prescott','CeeDee Lamb','Javonte Williams'],
 'brissett_mcbride': ['Jacoby Brissett','Trey McBride','CeeDee Lamb'],
 'lamar_single': ['Lamar Jackson','Zay Flowers','Khalil Shakir'],
 'allen_single': ['Josh Allen','Khalil Shakir','Zay Flowers'],
 'lamar_double': ['Lamar Jackson','Zay Flowers','Mark Andrews','Khalil Shakir'],
}
FRAGILE = {'Jonah Coleman',"Wan'Dale Robinson",'Kendrick Bourne',
           'Ryan Flournoy',"Ja'Kobi Lane"}


def validate(pool, ids):
    ps=[pool[i] for i in ids]
    assert len(ids)==len(set(ids))==9
    assert sum(p['salary'] for p in ps)<=50000
    counts={pos:sum(p['pos']==pos for p in ps) for pos in ['QB','RB','WR','TE','DST']}
    assert counts['QB']==counts['TE']==counts['DST']==1
    assert counts['RB'] in [2,3] and counts['WR'] in [3,4]
    qb=next(p for p in ps if p['pos']=='QB')
    assert any(p['team']==qb['team'] and p['pos'] in ['WR','TE'] for p in ps)
    dst=next(p for p in ps if p['pos']=='DST')
    assert not any(p['team']==dst['opp'] and p['pos']!='DST' for p in ps)
    assert sum(p['name'] in FRAGILE for p in ps)<=1


def generate(pool):
    n=len(pool);rng=np.random.default_rng(SEED)
    means=np.array([p['forecast'] for p in pool])
    a=[];low=[];high=[]
    def add(v,l,h):a.append(v);low.append(l);high.append(h)
    add(np.ones(n),9,9)
    add([p['salary'] for p in pool],49200,50000)
    for pos,l,h in [('QB',1,1),('DST',1,1),('RB',2,3),('WR',3,4),('TE',1,1)]:
        add([p['pos']==pos for p in pool],l,h)
    add([p['name'] in FRAGILE for p in pool],0,1)
    # Avoid buying the stars by hiding three cheap receivers in WR/FLEX slots.
    add([p['pos']=='WR' and p['salary']<5000 for p in pool],0,2)
    for t in TEAM:
        add([p['team']==t and p['pos']!='DST' for p in pool],0,3)
    for i,p in enumerate(pool):
        if p['pos']=='DST':
            for j,q in enumerate(pool):
                if q['pos']!='DST' and q['team']==p['opp']:
                    v=np.zeros(n);v[i]=v[j]=1;add(v,0,1)
    byname={p['name']:i for i,p in enumerate(pool)}
    out=[]
    for fam,core in FAMILIES.items():
        aa=list(a);ll=list(low);hh=list(high)
        if fam in ['lamar_single','allen_single']:
            v=np.zeros(n);v[byname['Mark Andrews']]=1
            aa.append(v);ll.append(0);hh.append(0)
        for name in core:
            v=np.zeros(n);v[byname[name]]=1;aa.append(v);ll.append(1);hh.append(1)
        def solve(c):
            return milp(-c,integrality=np.ones(n),bounds=Bounds(0,1),
                        constraints=LinearConstraint(np.array(aa),ll,hh))
        best=solve(means);assert best.success,fam
        floor=-best.fun*.955
        aa.append(means);ll.append(floor);hh.append(np.inf)
        seen=set()
        for k in range(100):
            c=means if k==0 else means+rng.normal(0,2.0,n)
            r=solve(c)
            if not r.success:continue
            ids=tuple(np.flatnonzero(r.x>.5).tolist())
            if ids in seen:continue
            seen.add(ids);validate(pool,ids)
            out.append(dict(family=fam,ids=ids,base_mean=round(means[list(ids)].sum(),4),
                            family_best_mean=round(-best.fun,4)))
    return out


def allocations(rng, totals, shares):
    """Allocate each team TD once; residual shares go to unlisted teammates."""
    remaining=totals.copy();mass=1.;out={}
    assert sum(shares.values())<=1+1e-8,shares
    for name,p in shares.items():
        counts=rng.binomial(remaining,np.clip(p/mass,0,1))
        remaining-=counts;mass-=p;out[name]=counts
    return out


def simulate(pool, draws, seed, variant='base'):
    rng=np.random.default_rng(seed)
    idx={p['name']:i for i,p in enumerate(pool)}
    out=np.zeros((draws,len(pool)),dtype=np.float32)
    games={tuple(sorted((p['team'],p['opp']))) for p in pool}
    strength=.20 if variant!='low_correlation' else .08
    game_factor={g:rng.lognormal(-strength**2/2,strength,draws) for g in sorted(games)}
    all_tds={};all_pass={};team_receiving={};team_rushing={}
    pass_fraction={}
    for team,(imp,pass_mean,qb_run) in TEAM.items():
        members=[p for p in pool if p['team']==team]
        game=next((g for g in sorted(games) if team in g),None)
        if game is None:continue
        factor=game_factor[game]
        local=rng.lognormal(-.22**2/2,.22,draws)
        rate=max((imp-6)/7,.1)*factor*local
        if variant=='high_games_cold' and team in ['DAL','ARI','BAL','BUF']:
            rate=rate*.8
        tds=rng.poisson(rate)
        pass_p=rng.beta(pass_mean*15,(1-pass_mean)*15,draws)
        ptd=rng.binomial(tds,pass_p)
        rtd=tds-ptd
        rec={k:v for k,v in REC[team].items() if k in idx}
        rush={k:v for k,v in RUSH[team].items() if k in idx}
        qb=next((p for p in members if p['pos']=='QB'),None)
        if qb:rush[qb['name']]=qb_run
        rec_td=allocations(rng,ptd,rec);rush_td=allocations(rng,rtd,rush)
        for name,counts in rec_td.items():out[:,idx[name]]+=6*counts
        for name,counts in rush_td.items():out[:,idx[name]]+=6*counts
        if qb:out[:,idx[qb['name']]]+=4*ptd
        all_tds[team]=tds;all_pass[team]=ptd;pass_fraction[team]=pass_p
        # Mean-one production factors: common game + team passing or rushing day.
        sigma=.18 if variant!='low_correlation' else .08
        team_receiving[team]=factor*rng.lognormal(-sigma**2/2,sigma,draws)
        team_rushing[team]=factor*rng.lognormal(-sigma**2/2,sigma,draws)
    for j,p in enumerate(pool):
        name,pos,t=p['name'],p['pos'],p['team']
        mean=SECONDARY.get(name,p['forecast']) if variant=='secondary_projection' else p['forecast']
        if pos=='DST':
            # Budget DST prior; opponent TD shocks reduce points. Not play-by-play.
            opp=p['opp'];td=all_tds[opp]
            expected=(TEAM[opp][0]-6)/7
            vals=mean+rng.normal(0,3.2,draws)-1.0*(td-expected)
            vals+=6*(rng.poisson(.07,draws)-.07)
            out[:,j]=np.maximum(-4,vals)
            continue
        imp,ps,qr=TEAM[t];tdm=(imp-6)/7
        expected_rec=tdm*ps*REC[t].get(name,0)
        expected_rush=tdm*(1-ps)*RUSH[t].get(name,0)
        expected_pass=0
        if pos=='QB':
            expected_pass=tdm*ps
            expected_rush=tdm*(1-ps)*qr
        non_td=mean-6*(expected_rec+expected_rush)-4*expected_pass
        assert non_td>0,(name,non_td)
        cv={'QB':.32,'RB':.44,'WR':.60,'TE':.65}[pos]
        # A bounded extra role shock preserves means while widening weak-role tails.
        idio=rng.gamma(1/cv**2,cv**2,draws)
        factor=team_rushing[t] if pos=='RB' else team_receiving[t]
        if pos=='RB':factor=.70*factor+.30*team_receiving[t]
        if variant=='high_games_cold' and t in ['DAL','ARI','BAL','BUF']:
            factor=factor*.90
        out[:,j]+=non_td*idio*factor
        if variant=='role_downside':
            mult={'Jonah Coleman':.65,"Wan'Dale Robinson":.8,
                  'Mark Andrews':.75,'Brenton Strange':.85,
                  'Hunter Henry':.85,'Malik Washington':.85,
                  'Rhamondre Stevenson':.90,'Khalil Shakir':.85,
                  'Kendrick Bourne':.75,'Ryan Flournoy':.75,
                  "Ja'Kobi Lane":.75,'Demario Douglas':.85}.get(name,1)
            out[:,j]*=mult
    return out


def metrics(scores):
    return dict(mean=round(float(np.mean(scores)),2),
                median=round(float(np.median(scores)),2),
                p10=round(float(np.quantile(scores,.1)),2),
                p90=round(float(np.quantile(scores,.9)),2),
                p95=round(float(np.quantile(scores,.95)),2),
                p180=round(float(np.mean(scores>=180)),5),
                p200=round(float(np.mean(scores>=200)),5))


def main():
    pool=load_pool();candidates=generate(pool)
    scores=simulate(pool,TRAIN_DRAWS,SEED+1)
    for c in candidates:
        c['train']=metrics(scores[:,c['ids']].sum(axis=1))
    # Separate holdout protects against selecting random favorable draws.
    chosen=[]
    for fam in FAMILIES:
        opts=[c for c in candidates if c['family']==fam]
        # Maximize a high-score exceedance, retaining a near-best-mean constraint.
        best=max(opts,key=lambda c:(c['train']['p200'],c['train']['p95']))
        chosen.append(best.copy())
    variants={}
    for v,k in [('base',2),('low_correlation',3),('role_downside',4),('high_games_cold',5),('secondary_projection',6)]:
        s=simulate(pool,TEST_DRAWS,SEED+k,v)
        variants[v]=s
        for c in chosen:c[v]=metrics(s[:,c['ids']].sum(axis=1))
    all_scores=np.stack([variants['base'][:,c['ids']].sum(axis=1) for c in chosen],axis=1)
    # Split ties rather than rewarding whichever identical roster was listed first.
    maxima=all_scores.max(axis=1,keepdims=True)
    tied=all_scores==maxima
    wins=tied/tied.sum(axis=1,keepdims=True)
    for k,c in enumerate(chosen):
        c['best_of_six']=round(float(np.mean(wins[:,k])),5)
        c['salary']=sum(pool[i]['salary'] for i in c['ids'])
        c['players']=[pool[i]['name'] for i in c['ids']]
    # Model checks verify mean centering and positive QB/receiver correlation.
    empirical=variants['base'].mean(axis=0)
    errors={p['name']:round(float(empirical[i]-p['forecast']),3) for i,p in enumerate(pool)}
    assert max(abs(v) for p,v in errors.items() if p not in ['Broncos','Browns','Lions','Steelers','Chargers','Raiders','Falcons','Buccaneers','Jaguars','Bengals','Jets','Rams']) < .25
    ix={p['name']:i for i,p in enumerate(pool)}
    corr=float(np.corrcoef(variants['base'][:,ix['Dak Prescott']],variants['base'][:,ix['CeeDee Lamb']])[0,1])
    assert corr>.1,corr
    (ROOT/'inputs.json').write_text(json.dumps(dict(pool=pool,team=TEAM,receiving_td_shares=REC,rushing_td_shares=RUSH,secondary=SECONDARY),indent=2)+'\n')
    (ROOT/'candidates.json').write_text(json.dumps(candidates,indent=2)+'\n')
    (ROOT/'results.json').write_text(json.dumps(chosen,indent=2)+'\n')
    manifest=dict(seed=SEED,training_draws=TRAIN_DRAWS,holdout_draws_per_scenario=TEST_DRAWS,
                  total_slate_draws=TRAIN_DRAWS+5*TEST_DRAWS,players=len(pool),candidates=len(candidates),
                  variants=list(variants),dak_lamb_correlation=round(corr,3),mean_errors=errors,
                  checks='salary, roster, uniqueness, opponent DST conflict, TD-share conservation, mean centering, QB-WR correlation passed',
                  note='No actual opponent field, payout EV, duplication or calibrated win probability.',
                  code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  base_pool_sha256=hashlib.sha256((ROOT/'base_pool.json').read_bytes()).hexdigest(),
                  numpy_version=np.__version__)
    (ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(dict(manifest=manifest,results=chosen),indent=2))


if __name__=='__main__':main()
