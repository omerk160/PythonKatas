import unittest
from katas.personalized_hello_world import greeting


class TestGreeting(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(greeting('David'), 'hello David')
        self.assertEqual(greeting('Alice'), 'hello Alice')

