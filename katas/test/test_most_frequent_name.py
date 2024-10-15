import os
import unittest
from katas.most_frequent_name import most_frequent_name


class TestMostFrequentName(unittest.TestCase):

    def test_most_frequent_name(self):
        file_path = 'test_names.txt'
        with open(file_path, 'w') as file:
            file.write("Alive\nAlice\nBob\nAlice\nCharlie\nBob\nAlice\nDavid\nDavid\nEva")

        result = most_frequent_name(file_path)
        os.remove(file_path)

        self.assertEqual(result, "Alice")
