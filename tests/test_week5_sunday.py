"""Sunday snapshot guards: frozen source assumptions and coupled game risks."""
import unittest

from run_week5_sunday import sunday_inputs, football_scenarios
from src.projections import add_model_projections


class SundayTests(unittest.TestCase):
    def test_injury_adjustments_and_new_player_ids(self):
        players = sunday_inputs()
        self.assertEqual(len(players), 48)
        self.assertFalse(players.player.duplicated().any())
        self.assertEqual(
            int(players.loc[players.player.eq("Braelon Allen"), "salary"].iloc[0]),
            5400,
        )
        self.assertEqual(
            float(players.loc[players.player.eq("Michael Wilson"), "targets"].iloc[0]),
            9.0,
        )
        self.assertIn("D'Andre Swift", set(players.player))
        self.assertIn("George Kittle", set(players.player))
        self.assertIn("Jordan Love", set(players.player))

    def test_game_downside_moves_both_arizona_receivers(self):
        players = sunday_inputs()
        scenario = football_scenarios(players, "Drake Maye")
        for name in ("Trey McBride", "Michael Wilson", "Jahmyr Gibbs"):
            self.assertLess(
                scenario["det_ari_offense_down20"].loc[name],
                scenario["mean"].loc[name],
            )

    def test_reconciles_projection_engine(self):
        players = sunday_inputs()
        direct = add_model_projections(players).set_index("player")
        scen = football_scenarios(players, "Brock Purdy")
        for name in ("Brock Purdy", "Jordan Love", "George Kittle"):
            self.assertAlmostEqual(
                float(direct.loc[name, "model_projection"]),
                float(scen["mean"].loc[name]),
                places=6,
            )


if __name__ == "__main__":
    unittest.main()
