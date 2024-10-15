class SimpleQueue:
    """
    A basic queue data structure.
    """

    def __init__(self):
        """
        Initialize an empty queue.
        """
        raise NotImplementedError()

    def is_empty(self):
        """
        Check if the queue is empty.

        :return: bool: True if the queue is empty, False otherwise.
        """
        raise NotImplementedError()

    def enqueue(self, item):
        """
        Add an item to the rear of the queue.

        :param item: The item to be added to the queue.
        """
        raise NotImplementedError()

    def dequeue(self):
        """
        Remove and return the item at the front of the queue.

        :return: The item at the front of the queue.
        :raises RuntimeError: If the queue is empty.
        """
        raise NotImplementedError()

    def peek(self):
        """
        Return the item at the front of the queue without removing it.

        :return: The item at the front of the queue.
        :raises RuntimeError: If the queue is empty.
        """
        raise NotImplementedError()

    def size(self):
        """
        Return the number of items in the queue.

        :return: int: The number of items in the queue.
        """
        raise NotImplementedError()


if __name__ == '__main__':
    q = SimpleQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Queue size:", q.size())
    print("Front item:", q.peek())

    while not q.is_empty():
        print("Dequeued item:", q.dequeue())

    try:
        q.dequeue()  # Queue is empty
    except RuntimeError as e:
        print("Error:", e)
