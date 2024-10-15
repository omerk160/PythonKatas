import unittest
from katas.calculator2 import add_string_numbers


class TestAddStringNumbers(unittest.TestCase):

    def test_add_string_numbers(self):
        self.assertEqual(add_string_numbers("10", "20", "30"), 60)
        self.assertEqual(add_string_numbers("5", "15", "25"), 45)
        self.assertEqual(add_string_numbers("100", "200", "300"), 600)
