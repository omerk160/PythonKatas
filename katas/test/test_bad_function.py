import unittest
from katas.bad_function import get_sum

class TestGetSum(unittest.TestCase):

    def test_get_sum(self):
        self.assertEqual(get_sum(3, 5), 8)
        self.assertEqual(get_sum(10, 2), 12)
