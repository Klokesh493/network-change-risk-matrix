import unittest

from change_risk import classify


class ChangeRiskTest(unittest.TestCase):
    def test_classifies_large_unproven_change_high(self):
        row = {"change_id": "c", "devices": "22", "regions": "4", "rollback_tested": "no", "customer_tier": "enterprise"}
        self.assertEqual(classify(row), "high")


if __name__ == "__main__":
    unittest.main()
