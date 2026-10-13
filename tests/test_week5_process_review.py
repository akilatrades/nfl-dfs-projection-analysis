"""Prevent Sunday's conservative process review from silently reverting."""

import unittest

from run_week5_process_review import (
    CONSERVATIVE_CHANGES,
    PRIMARY_EXCLUSIONS,
    SPECS,
    revised_inputs,
)
from run_week5_sunday import sunday_inputs
from src.projections import add_model_projections


class ProcessReviewTests(unittest.TestCase):
    def test_regression_choices_are_versioned_without_mutating_sunday(self):
        before = sunday_inputs().set_index("player")
        after = revised_inputs().set_index("player")
        self.assertEqual(float(before.loc["Romeo Doubs", "targets"]), 7.5)
        self.assertEqual(float(after.loc["Romeo Doubs", "targets"]), 5.5)
        self.assertEqual(float(before.loc["Braelon Allen", "rush_attempts"]), 18.5)
        self.assertEqual(float(after.loc["Braelon Allen", "rush_attempts"]), 16.0)
        self.assertEqual(len(before), len(after))
        self.assertEqual(len(after), 48)

    def test_point_changes_are_explainable_from_inputs(self):
        before = add_model_projections(sunday_inputs()).set_index("player")
        after = add_model_projections(revised_inputs()).set_index("player")
        self.assertAlmostEqual(
            float(before.loc["Romeo Doubs", "model_projection"]), 12.485, places=3
        )
        self.assertAlmostEqual(
            float(after.loc["Romeo Doubs", "model_projection"]), 9.321, places=3
        )
        # DraftKings points by hand: 16 x 3.9 rush yds x 0.1 = 6.24; 0.38 rush TD x 6
        # = 2.28; 3.2 x 0.72 = 2.304 catches; 2.304 x 6.0 rec yds x 0.1 = 1.3824;
        # 0.065 rec TD x 6 = 0.39; 100-yd bonuses 0.10 x 3 + 0.01 x 3 = 0.33;
        # fumbles lost -0.04. Total 12.8864.
        self.assertAlmostEqual(
            float(after.loc["Braelon Allen", "model_projection"]), 12.8864, places=3
        )
        self.assertLess(
            float(after.loc["Braelon Allen", "model_projection"]),
            float(before.loc["Braelon Allen", "model_projection"]),
        )

    def test_explicit_doubs_control_is_separate(self):
        self.assertIn("Romeo Doubs", PRIMARY_EXCLUSIONS)
        self.assertIn("Braelon Allen", PRIMARY_EXCLUSIONS)
        self.assertEqual(sum(s.get("allow_doubs", False) for s in SPECS), 1)
        for spec in SPECS:
            self.assertLessEqual(spec["azmin"], spec["azmax"])
            self.assertLessEqual(spec["azmax"], 3)
            self.assertTrue(spec["locks"])


if __name__ == "__main__":
    unittest.main()
