import unittest
from katas.numbers_division import numbers_division


class TestNumbersDivision(unittest.TestCase):
    def test_numbers_division(self):
        self.assertAlmostEqual(numbers_division(10, 3), 3.3333, places=4)
        self.assertAlmostEqual(numbers_division(8, 2), 4.0, places=4)
        self.assertAlmostEqual(numbers_division(5, 2), 2.5, places=4)
