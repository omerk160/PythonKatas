import unittest
from katas.bad_average import bad_average


class TestBadAverage(unittest.TestCase):

    def test_bad_average(self):
        result = bad_average(1, 2, 3)
        self.assertEqual(result, 2.0)

