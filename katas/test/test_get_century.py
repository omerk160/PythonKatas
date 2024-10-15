import unittest
from katas.get_century import get_century


class TestGetCentury(unittest.TestCase):
    def test_get_century(self):
        self.assertEqual(get_century(1786), 18)
        self.assertEqual(get_century(1905), 20)
        self.assertEqual(get_century(2000), 20)
        self.assertEqual(get_century(2023), 21)

