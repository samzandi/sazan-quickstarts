import unittest

from agent import run_analysis
from engine import analyze
from models import BusinessInput


class BusinessAgentTests(unittest.TestCase):
    def test_demo_shop_calculations(self):
        result = run_analysis("demo-shop")
        self.assertTrue(result.supported)
        self.assertEqual(result.revenue, 6000.0)
        self.assertEqual(result.variable_cost, 2400.0)
        self.assertEqual(result.contribution_margin, 3600.0)
        self.assertEqual(result.operating_result, 1200.0)
        self.assertEqual(result.break_even_units, 80)
        self.assertGreaterEqual(len(result.assumptions), 3)

    def test_unknown_business_refuses(self):
        result = run_analysis("missing")
        self.assertFalse(result.supported)
        self.assertEqual(result.reason, "unknown_business_id")

    def test_no_positive_contribution_refuses_break_even(self):
        result = run_analysis("loss-case")
        self.assertFalse(result.supported)
        self.assertEqual(result.reason, "no_positive_unit_contribution")
        self.assertIsNone(result.break_even_units)

    def test_negative_input_is_rejected(self):
        result = analyze(BusinessInput("bad", -1, 10.0, 2.0, 100.0))
        self.assertFalse(result.supported)
        self.assertEqual(result.reason, "invalid_negative_input")


if __name__ == "__main__":
    unittest.main()
