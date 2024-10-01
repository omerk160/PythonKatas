def find_runner_position(runners, runner_name):
    """
    Returns the index of the given runner in the list, or -1 if the runner is not found.
    """


# Example usage
position_1 = find_runner_position(['Alice', 'Bob', 'Charlie', 'David'], 'Charlie')
print(position_1)  # 3 expected

position_2 = find_runner_position(['Alice', 'Bob', 'Charlie', 'David'], 'Alice')
print(position_2)  # 1 expected

position_3 = find_runner_position(['Alice', 'Bob', 'Charlie', 'David'], 'Eve')
print(position_3)  # -1 expected

"""
To complete this exercise:
--------------------------
You have a list of runners in the order they finished the race. 
Your job is to determine the position of a particular runner based on their name.
If the runner did not finish the race, you should return -1.


Exercise Breakdown:
-------------------
There is a function to do it: list.index(). But try to do it manually using loops.

The `list.index()` method is a built-in Python function that returns the index of the first occurrence of a specified value in a list. 
If the value is not found, it raises a `ValueError` error.
"""