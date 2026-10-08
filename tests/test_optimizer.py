"""Small exhaustive oracle and failure tests for lineup selection."""

import itertools
import unittest

import numpy as np
import pandas as pd

from src.optimizer import assign_slots, optimize_lineup


class OptimizerTests(unittest.TestCase):
    def setUp(self):
        rows = []
        for i, pos in enumerate(["QB", "RB", "RB", "RB", "WR", "WR", "WR", "WR", "TE", "TE", "DST", "DST"]):
            team = ["A", "C", "D", "E", "A", "C", "D", "B", "B", "E", "F", "G"][i]
            rows.append(dict(player=str(i), position=pos, team=team, opponent={"A":"B","B":"A","C":"D","D":"C","E":"F","F":"E","G":"H"}[team], salary=4000 + 100*i, role_risk=0, model_projection=10+i, stress=10+i, kickoff_utc="2026-10-11T17:00:00Z"))
        self.pool = pd.DataFrame(rows)
        self.pool.loc[7,"stress"] = 2
        self.pool.loc[9,"role_risk"] = 1
        self.pool.loc[7,"role_risk"] = 1

    def test_matches_exhaustive_legal_rosters(self):
        legal = []
        for idx in itertools.combinations(range(len(self.pool)), 9):
            p = self.pool.iloc[list(idx)]
            c = p.position.value_counts()
            if c.get("QB",0)!=1 or c.get("DST",0)!=1 or not (2<=c.get("RB",0)<=3 and 3<=c.get("WR",0)<=4 and 1<=c.get("TE",0)<=2):
                continue
            if p.salary.sum()>50000 or p.role_risk.sum()>1 or p.team.value_counts().max()>4:
                continue
            if "4" not in set(p.player):  # Only A-team pass catcher.
                continue
            dst=p[p.position.eq("DST")].iloc[0]
            if p[p.position.ne("DST")].team.eq(dst.opponent).any():
                continue
            legal.append(min(p.model_projection.sum(),p.stress.sum()))
        got=optimize_lineup(self.pool,["model_projection","stress"])
        self.assertAlmostEqual(got.attrs["objective"],max(legal))
        self.assertEqual(len(got),9)

    def test_bringback_and_exclusion(self):
        result=optimize_lineup(self.pool,["model_projection"],bring_back=True,exclude=("7",))
        self.assertIn("8",set(result.player))
        self.assertNotIn("7",set(result.player))

    def test_invalid_inputs_and_infeasible_budget(self):
        for bad in [pd.concat([self.pool,self.pool.iloc[[0]]]),self.pool.assign(model_projection=np.nan)]:
            with self.assertRaises(ValueError):
                optimize_lineup(bad,["model_projection"])
        with self.assertRaises(ValueError):
            optimize_lineup(self.pool,["model_projection"],salary_cap=100)

    def test_flex_is_latest_eligible_player(self):
        result=optimize_lineup(self.pool,["model_projection","stress"])
        extra_pos=next(pos for pos,n in [("RB",2),("WR",3),("TE",1)] if sum(result.position.eq(pos))>n)
        idx=result.index[result.position.eq(extra_pos)][0]
        result.loc[idx,"kickoff_utc"]="2026-10-11T20:25:00Z"
        slots=assign_slots(result)
        self.assertEqual(slots.loc[idx,"slot"],"FLEX")


if __name__ == "__main__":
    unittest.main()
