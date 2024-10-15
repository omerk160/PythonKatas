import unittest
from katas.hello_world2 import create_greeting


class TestCreateGreeting(unittest.TestCase):
    def test_create_greeting(self):
        self.assertEqual(create_greeting(), "Hello, world!")

