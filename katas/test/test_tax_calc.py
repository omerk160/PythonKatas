import unittest
from katas.tax_calc import tax_calc


class TestTaxCalc(unittest.TestCase):

    def test_tax_calc(self):
        self.assertEqual(tax_calc(50000, 80000, 120000), 41000.0)
        self.assertEqual(tax_calc(30000, 60000, 90000), 30000.0)
        self.assertEqual(tax_calc(0, 0, 0), 0)
