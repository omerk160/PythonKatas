import unittest
from katas.get_seconds import get_seconds


class TestGetSeconds(unittest.TestCase):
    def test_get_seconds(self):
        self.assertEqual(get_seconds(1), 86400)
        self.assertEqual(get_seconds(0), 0)
        self.assertEqual(get_seconds(2), 172800)


