def last_in_queue(queue):
    """
    Returns the last person in the queue.
    """



queue_1 = ["Alice", "Bob", "Charlie"]
print(last_in_queue(queue_1))  # "Charlie" expected

queue_2 = ["David"]
print(last_in_queue(queue_2))  # "David" expected

queue_3 = []
print(last_in_queue(queue_3))  # None expected


"""
To complete this exercise:
--------------------------
Implement the 'last_in_queue' function to return the last element in the list 'queue'.
If the list is empty, return None.


Exercise Breakdown:
-------------------
In Python, you can access elements of a list using their index. The indices start from 0, meaning:
- The first element is at index 0.
- The second element is at index 1.
- And so on...

To access the last element of a list, you can use the index -1.

fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # "apple"
print(fruits[1])  # "banana"
print(fruits[-1]) # "cherry"
"""
