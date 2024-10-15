import unittest
from io import StringIO
from unittest.mock import patch
from katas.dog import Dog


class TestDog(unittest.TestCase):
    def setUp(self):
        self.my_dog = Dog("Buddy", "Golden Retriever")

    def test_dog_attributes(self):
        self.assertEqual(self.my_dog.name, "Buddy")
        self.assertEqual(self.my_dog.breed, "Golden Retriever")

    def test_dog_positions(self):
        self.assertEqual(self.my_dog.position, "sitting")

        self.my_dog.stand()
        self.assertEqual(self.my_dog.position, "standing")

        self.my_dog.jump()
        self.assertEqual(self.my_dog.position, "jumping")

        self.my_dog.sit()
        self.assertEqual(self.my_dog.position, "sitting")

    def test_bark(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.my_dog.bark(n=3)
            output = mock_stdout.getvalue()

        self.assertEqual(output.strip(), "Woof! Woof!\nWoof! Woof!\nWoof! Woof!")

    def test_describe(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.my_dog.describe()
            output = mock_stdout.getvalue()

        expected_description = f"I'm {self.my_dog.name}, a {self.my_dog.breed}. I'm {self.my_dog.position}\n"
        self.assertEqual(output.strip(), expected_description)
