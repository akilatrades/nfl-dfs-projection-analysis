/* Deterministic illustrative correlated DFS simulator for 2026 Week 5.
 * Run: node monte_carlo_week5_2026.js
 * No external packages. Means are subjective analyst priors vs one
 * uncalibrated public feed (SharkSnip, morning Oct 11); NOT observed
 * player outcomes, tournament EV, or opponent ownership simulation.
 */
const players=[
  {
    "id": "Love",
    "name": "Jordan Love",
    "pos": "QB",
    "team": "GB",
    "opp": "CHI",
    "salary": 5700,
    "ours": 19.494,
    "external": 16.6,
    "game": "CHI-GB"
  },
  {
    "id": "Brown",
    "name": "Chase Brown",
    "pos": "RB",
    "team": "CIN",
    "opp": "MIA",
    "salary": 6900,
    "ours": 18.929,
    "external": 14.6,
    "game": "CIN-MIA"
  },
  {
    "id": "Swift",
    "name": "D'Andre Swift",
    "pos": "RB",
    "team": "CHI",
    "opp": "GB",
    "salary": 6200,
    "ours": 18.283,
    "external": 14.1,
    "game": "CHI-GB"
  },
  {
    "id": "Malik",
    "name": "Malik Washington",
    "pos": "WR",
    "team": "MIA",
    "opp": "CIN",
    "salary": 4600,
    "ours": 10.546,
    "external": 9.9,
    "game": "CIN-MIA"
  },
  {
    "id": "Watson",
    "name": "Christian Watson",
    "pos": "WR",
    "team": "GB",
    "opp": "CHI",
    "salary": 6400,
    "ours": 15.485,
    "external": 14.6,
    "game": "CHI-GB"
  },
  {
    "id": "Metcalf",
    "name": "DK Metcalf",
    "pos": "WR",
    "team": "PIT",
    "opp": "IND",
    "salary": 5400,
    "ours": 13.1,
    "external": 11.3,
    "game": "IND-PIT"
  },
  {
    "id": "Kittle",
    "name": "George Kittle",
    "pos": "TE",
    "team": "SF",
    "opp": "SEA",
    "salary": 5200,
    "ours": 14.618,
    "external": 13.5,
    "game": "SEA-SF"
  },
  {
    "id": "McBride",
    "name": "Trey McBride",
    "pos": "TE",
    "team": "ARI",
    "opp": "DET",
    "salary": 6700,
    "ours": 19.192,
    "external": 13.1,
    "game": "ARI-DET"
  },
  {
    "id": "Browns",
    "name": "Browns DST",
    "pos": "DST",
    "team": "CLE",
    "opp": "NYJ",
    "salary": 2800,
    "ours": 7.12,
    "external": 6.1,
    "game": "CLE-NYJ"
  },
  {
    "id": "Odunze",
    "name": "Rome Odunze",
    "pos": "WR",
    "team": "CHI",
    "opp": "GB",
    "salary": 4700,
    "ours": 12.061,
    "external": 10.7,
    "game": "CHI-GB"
  },
  {
    "id": "Wilson",
    "name": "Michael Wilson",
    "pos": "WR",
    "team": "ARI",
    "opp": "DET",
    "salary": 6200,
    "ours": 16.688,
    "external": 14.7,
    "game": "ARI-DET"
  },
  {
    "id": "Jameson",
    "name": "Jameson Williams",
    "pos": "WR",
    "team": "DET",
    "opp": "ARI",
    "salary": 5900,
    "ours": 12.37,
    "external": 11.9,
    "game": "ARI-DET"
  },
  {
    "id": "Juwan",
    "name": "Juwan Johnson",
    "pos": "TE",
    "team": "NO",
    "opp": "MIN",
    "salary": 4500,
    "ours": 13.4,
    "external": 13.4,
    "game": "MIN-NO"
  },
  {
    "id": "Goff",
    "name": "Jared Goff",
    "pos": "QB",
    "team": "DET",
    "opp": "ARI",
    "salary": 6600,
    "ours": 20.549,
    "external": 18.5,
    "game": "ARI-DET"
  },
  {
    "id": "AmonRa",
    "name": "Amon-Ra St. Brown",
    "pos": "WR",
    "team": "DET",
    "opp": "ARI",
    "salary": 7900,
    "ours": 20.54,
    "external": 15.8,
    "game": "ARI-DET"
  },
  {
    "id": "LaPorta",
    "name": "Sam LaPorta",
    "pos": "TE",
    "team": "DET",
    "opp": "ARI",
    "salary": 4900,
    "ours": 11.24,
    "external": 13.3,
    "game": "ARI-DET"
  },
  {
    "id": "Henry",
    "name": "Hunter Henry",
    "pos": "TE",
    "team": "NE",
    "opp": "LV",
    "salary": 3700,
    "ours": 8.91,
    "external": 8.6,
    "game": "LV-NE"
  },
  {
    "id": "Gibbs",
    "name": "Jahmyr Gibbs",
    "pos": "RB",
    "team": "DET",
    "opp": "ARI",
    "salary": 9800,
    "ours": 25.633,
    "external": 20.1,
    "game": "ARI-DET"
  },
  {
    "id": "Maye",
    "name": "Drake Maye",
    "pos": "QB",
    "team": "NE",
    "opp": "LV",
    "salary": 6300,
    "ours": 20.451,
    "external": 18.5,
    "game": "LV-NE"
  },
  {
    "id": "Brissett",
    "name": "Jacoby Brissett",
    "pos": "QB",
    "team": "ARI",
    "opp": "DET",
    "salary": 5500,
    "ours": 18.335,
    "external": 15.8,
    "game": "ARI-DET"
  },
  {
    "id": "Doubs",
    "name": "Romeo Doubs",
    "pos": "WR",
    "team": "NE",
    "opp": "LV",
    "salary": 5000,
    "ours": 9.321,
    "external": 12.6,
    "game": "LV-NE"
  },
  {
    "id": "Allen",
    "name": "Braelon Allen",
    "pos": "RB",
    "team": "NYJ",
    "opp": "CLE",
    "salary": 5400,
    "ours": 12.957,
    "external": 13,
    "game": "CLE-NYJ"
  },
  {
    "id": "Chargers",
    "name": "Chargers DST",
    "pos": "DST",
    "team": "LAC",
    "opp": "DEN",
    "salary": 2300,
    "ours": 5.28,
    "external": 5.6,
    "game": "DEN-LAC"
  },
  {
    "id": "Purdy",
    "name": "Brock Purdy",
    "pos": "QB",
    "team": "SF",
    "opp": "SEA",
    "salary": 6500,
    "ours": 21.233,
    "external": 18.8,
    "game": "SEA-SF"
  },
  {
    "id": "Boston",
    "name": "Denzel Boston",
    "pos": "WR",
    "team": "CLE",
    "opp": "NYJ",
    "salary": 5200,
    "ours": 13.8,
    "external": 13.8,
    "game": "CLE-NYJ"
  },
  {
    "id": "Tucker",
    "name": "Tre Tucker",
    "pos": "WR",
    "team": "LV",
    "opp": "NE",
    "salary": 4800,
    "ours": 11.1,
    "external": 11.1,
    "game": "LV-NE"
  }
];
const lineups=[
  {
    "name": "Current revised (Love/Malik/Metcalf/McBride)",
    "ids": [
      "Love",
      "Brown",
      "Swift",
      "Malik",
      "Watson",
      "Metcalf",
      "Kittle",
      "McBride",
      "Browns"
    ]
  },
  {
    "name": "Original (Love/Odunze/McBride)",
    "ids": [
      "Love",
      "Brown",
      "Swift",
      "Odunze",
      "Watson",
      "Metcalf",
      "Kittle",
      "McBride",
      "Browns"
    ]
  },
  {
    "name": "Pivot 1 (Love/Wilson/Juwan/Metcalf)",
    "ids": [
      "Love",
      "Brown",
      "Swift",
      "Wilson",
      "Watson",
      "Metcalf",
      "Kittle",
      "Juwan",
      "Browns"
    ]
  },
  {
    "name": "Pivot 2 (Love/Wilson/Jameson/Juwan)",
    "ids": [
      "Love",
      "Brown",
      "Swift",
      "Wilson",
      "Watson",
      "Jameson",
      "Kittle",
      "Juwan",
      "Browns"
    ]
  },
  {
    "name": "Brissett/Wilson/McBride",
    "ids": [
      "Brissett",
      "Brown",
      "Swift",
      "Wilson",
      "Odunze",
      "Metcalf",
      "Kittle",
      "McBride",
      "Browns"
    ]
  },
  {
    "name": "Goff/Amon-Ra/LaPorta",
    "ids": [
      "Goff",
      "Brown",
      "Swift",
      "AmonRa",
      "Odunze",
      "Malik",
      "LaPorta",
      "Kittle",
      "Browns"
    ]
  },
  {
    "name": "Maye/Gibbs/Henry",
    "ids": [
      "Maye",
      "Gibbs",
      "Swift",
      "Wilson",
      "Odunze",
      "Metcalf",
      "Henry",
      "Kittle",
      "Chargers"
    ]
  },
  {
    "name": "Purdy/Kittle/Wilson/McBride",
    "ids": [
      "Purdy",
      "Brown",
      "Swift",
      "Wilson",
      "Odunze",
      "Malik",
      "Kittle",
      "McBride",
      "Browns"
    ]
  },
  {
    "name": "Love/Gibbs/Watson",
    "ids": [
      "Love",
      "Gibbs",
      "Swift",
      "Watson",
      "Odunze",
      "Metcalf",
      "Henry",
      "Kittle",
      "Browns"
    ]
  },
  {
    "name": "Love/Wilson/Tucker/Juwan",
    "ids": [
      "Love",
      "Brown",
      "Swift",
      "Wilson",
      "Watson",
      "Tucker",
      "Kittle",
      "Juwan",
      "Browns"
    ]
  },
  {
    "name": "Love/Watson/Wilson/Jameson/McBride/Henry",
    "ids": [
      "Love",
      "Brown",
      "Swift",
      "Wilson",
      "Watson",
      "Jameson",
      "McBride",
      "Henry",
      "Chargers"
    ]
  },
  {
    "name": "Brissett/Wilson/McBride/Jameson/Tucker",
    "ids": [
      "Brissett",
      "Brown",
      "Swift",
      "Wilson",
      "Jameson",
      "Tucker",
      "McBride",
      "Kittle",
      "Chargers"
    ]
  },
  {
    "name": "Purdy/Wilson/Metcalf/McBride",
    "ids": [
      "Purdy",
      "Brown",
      "Swift",
      "Wilson",
      "Metcalf",
      "Malik",
      "Kittle",
      "McBride",
      "Chargers"
    ]
  }
];
function validate(players,lineups){let P=new Map(players.map(p=>[p.id,p]));const outcomes=[];for(let l of lineups){let ps=l.ids.map(id=>P.get(id));if(ps.includes(undefined))throw Error("Unknown player in "+l.name);let salary=ps.reduce((s,p)=>s+p.salary,0),counts={};for(let p of ps)counts[p.pos]=(counts[p.pos]||0)+1;
if(salary>50000||l.ids.length!==9||new Set(l.ids).size!==9||counts.QB!==1||counts.RB<2||counts.RB>3||counts.WR<3||counts.WR>4||counts.TE<1||counts.TE>2||counts.DST!==1)throw Error("Illegal roster "+l.name+" "+salary+JSON.stringify(counts));
let dst=ps.find(p=>p.pos==="DST");if(ps.some(p=>p.pos!=="DST"&&p.team===dst.opp))throw Error("DST clash "+l.name);
if(!ps.some(p=>p.team===ps.find(p=>p.pos==="QB").team&&["WR","TE"].includes(p.pos)))throw Error("no QB receiver "+l.name);
outcomes.push({name:l.name,salary,players:l.ids})}return outcomes}

function mulberry32(a){return ()=>{a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}

function normalSampler(next){let spare=null;return ()=>{if(spare!==null){let k=spare;spare=null;return k}let u=0,v=0;while(!u)u=next();v=next();let r=Math.sqrt(-2*Math.log(u)),a=2*Math.PI*v;spare=r*Math.sin(a);return r*Math.cos(a)}}

function quant(sorted,p){const x=(sorted.length-1)*p;const a=Math.floor(x),b=Math.ceil(x);return sorted[a]*(1-(x-a))+sorted[b]*(x-a)}

function simulate(players,lineups,settings){const N=settings.n,mode=settings.mode,spread=settings.spread||1,seed=settings.seed;const next=mulberry32(seed),z=normalSampler(next), P=new Map(players.map(p=>[p.id,p]));const games=[...new Set(players.map(p=>p.game))],teams=[...new Set(players.map(p=>p.team))];const passMembers=new Map();for(let p of players)if(["WR","TE"].includes(p.pos)){if(!passMembers.has(p.team))passMembers.set(p.team,[]);passMembers.get(p.team).push(p.id)}
const scores=Object.fromEntries(players.map(p=>[p.id,0])), L=lineups.map(l=>({name:l.name,ids:l.ids,sorted:new Float64Array(N),v170:0,v190:0,v210:0,wins:0,azHighN:0,azHighSum:0,azLowN:0,azLowSum:0,gbHighN:0,gbHighSum:0,gbLowN:0,gbLowSum:0,sum:0}));
const qbSigma=.40*spread,rbSigma=.57*spread,wrSigma=.70*spread,teSigma=.60*spread;
let pairWin=0;
for(let k=0;k<N;k++){const g={},t={},passing={},script={},allocZ={},share={};
for(let name of games)g[name]=z();for(let name of teams){t[name]=z();passing[name]=z();script[name]=z()}
for(let p of players)if(["WR","TE"].includes(p.pos))allocZ[p.id]=z();
for(let [team,members] of passMembers){const m=members.reduce((s,id)=>s+allocZ[id],0)/members.length,denom=members.length>1?Math.sqrt(1-1/members.length):1;for(let id of members)share[id]=members.length>1?(allocZ[id]-m)/denom:0;}
for(let p of players){let sig=p.pos==="QB"?qbSigma:p.pos==="RB"?rbSigma:p.pos==="WR"?wrSigma:p.pos==="TE"?teSigma:0;
let a,b,c,d,e=0;
if(p.pos==="QB"){a=.34;b=.27;c=.34;d=.17}
else if(p.pos==="RB"){a=.26;b=.28;c=-.12;d=-.20}
else if(p.pos==="WR"||p.pos==="TE"){a=.29;b=.20;c=.30;d=.15;e=.26}
else {a=-.14;b=.20;c=0;d=0;}
let residual=Math.sqrt(Math.max(0,1-a*a-b*b-c*c-d*d-e*e));
let latent=a*g[p.game]+b*t[p.team]+c*passing[p.team]+d*script[p.team]+(e?e*share[p.id]:0)+residual*z();
let m=mode==="ours"?p.ours:mode==="external"?p.external:(p.ours+p.external)/2;
let v;
if(p.pos==="DST"){v=Math.min(27,Math.max(-4,m+4.2*latent))}
else {v=m*Math.exp(sig*latent-.5*sig*sig);let risk=p.pos==="QB"?.012:p.pos==="RB"?.024:p.pos==="WR"?.028:.023;
if(next()<risk)v*=.05+next()*.55}
scores[p.id]=v}
let max=-1e9,win=-1;
for(let j=0;j<L.length;j++){const l=L[j];let total=0;for(let id of l.ids)total+=scores[id];l.sorted[k]=total;l.sum+=total;if(total>=170)l.v170++;if(total>=190)l.v190++;if(total>=210)l.v210++;
let az=g["ARI-DET"],gb=g["CHI-GB"];
if(az>0.8){l.azHighN++;l.azHighSum+=total}if(az<-.8){l.azLowN++;l.azLowSum+=total}if(gb>0.8){l.gbHighN++;l.gbHighSum+=total}if(gb<-.8){l.gbLowN++;l.gbLowSum+=total}
if(total>max){max=total;win=j;}}L[win].wins++;
if(L[2].sorted[k]>L[0].sorted[k])pairWin++;
}
return {settings,conditionalRates: {AZ_high:"DET-ARI shared Gaussian game factor > +0.8",AZ_low:"< -0.8",GB_high:"CHI-GB factor > +0.8",GB_low:"< -0.8"},probPivot1OverCurrent:pairWin/N,lineups:L.map(l=>{const sorted=Array.from(l.sorted).sort((a,b)=>a-b),base=lineups.find(x=>x.name===l.name),ps=base.ids.map(id=>P.get(id));return {name:l.name,salary:ps.reduce((s,p)=>s+p.salary,0),inputMean:+ps.reduce((s,p)=>s+(mode==="ours"?p.ours:mode==="external"?p.external:(p.ours+p.external)/2),0).toFixed(2),sampleMean:+(l.sum/N).toFixed(2),p50:+quant(sorted,.5).toFixed(2),p90:+quant(sorted,.9).toFixed(2),p95:+quant(sorted,.95).toFixed(2),p99:+quant(sorted,.99).toFixed(2),p170:+(l.v170/N).toFixed(4),p190:+(l.v190/N).toFixed(4),p210:+(l.v210/N).toFixed(4),headToHead:+(l.wins/N).toFixed(4),ifAZHighMean:+(l.azHighSum/l.azHighN).toFixed(1),ifAZLowMean:+(l.azLowSum/l.azLowN).toFixed(1),ifGBHighMean:+(l.gbHighSum/l.gbHighN).toFixed(1),ifGBLowMean:+(l.gbLowSum/l.gbLowN).toFixed(1)}})}
}
const checks=validate(players,lineups);
const scenarios=[
  {
    "label": "blended",
    "settings": {
      "n": 90000,
      "mode": "blended",
      "seed": 20261011,
      "spread": 1
    },
    "edits": {}
  },
  {
    "label": "external",
    "settings": {
      "n": 90000,
      "mode": "external",
      "seed": 20261011,
      "spread": 1
    },
    "edits": {}
  },
  {
    "label": "ours",
    "settings": {
      "n": 90000,
      "mode": "ours",
      "seed": 20261011,
      "spread": 1
    },
    "edits": {}
  },
  {
    "label": "Spags updated Sunday",
    "settings": {
      "n": 75000,
      "mode": "blended",
      "seed": 20261011,
      "spread": 1
    },
    "edits": {
      "McBride": 20.5,
      "Juwan": 11,
      "Kittle": 13.4,
      "Wilson": 18.4,
      "Watson": 14,
      "Jameson": 12.3,
      "Malik": 11.6,
      "Odunze": 9.5,
      "Metcalf": 12.5,
      "Henry": 10.8
    }
  },
  {
    "label": "conservative Juwan Jameson",
    "settings": {
      "n": 75000,
      "mode": "blended",
      "seed": 20261011,
      "spread": 1
    },
    "edits": {
      "McBride": 20.5,
      "Juwan": 8.5,
      "Jameson": 10.5,
      "Henry": 9.5
    }
  },
  {
    "label": "Detroit rushing control",
    "settings": {
      "n": 75000,
      "mode": "blended",
      "seed": 20261011,
      "spread": 1
    },
    "edits": {
      "McBride": 18,
      "Wilson": 16,
      "Jameson": 9,
      "Gibbs": 29
    }
  }
];
const runs=scenarios.map(sc=>({
  label: sc.label,
  edits: sc.edits,
  run: simulate(
    players.map(p => ({
      ...p,
      ours: sc.edits[p.id] ?? p.ours,
      external: sc.edits[p.id] ?? p.external
    })),
    lineups,
    sc.settings
  )
}));
process.stdout.write(JSON.stringify({ checks, runs }, null, 2) + "\n");
