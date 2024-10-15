import unittest
from katas.age_message_fix import age_message


class TestAgeMessage(unittest.TestCase):
    def test_age_message(self):
        self.assertEqual(age_message(25), "I am 25 years old.")
        self.assertEqual(age_message(30), "I am 30 years old.")
        self.assertEqual(age_message(18), "I am 18 years old.")
