import unittest
from katas.simple_queue import SimpleQueue


class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        q = SimpleQueue()
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        q.enqueue(2)
        self.assertEqual(q.size(), 2)

    def test_dequeue(self):
        q = SimpleQueue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)

    def test_peek(self):
        q = SimpleQueue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.peek(), 1)
        self.assertEqual(q.size(), 2)

    def test_size(self):
        q = SimpleQueue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.size(), 3)

    def test_is_empty(self):
        q = SimpleQueue()
        self.assertTrue(q.is_empty())
        q.enqueue(1)
        self.assertFalse(q.is_empty())

    def test_dequeue_empty_queue(self):
        q = SimpleQueue()
        with self.assertRaises(RuntimeError):
            q.dequeue()

    def test_peek_empty_queue(self):
        q = SimpleQueue()
        with self.assertRaises(RuntimeError):
            q.peek()

