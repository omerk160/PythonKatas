def all_elements_meet_condition(numbers):
    """
    Checks if all elements in the given list of numbers are positive.
    """


print(all_elements_meet_condition([1, 2, 3, 4, 5]))   # Expected output: True
print(all_elements_meet_condition([1, -2, 3, 4, 5]))  # Expected output: False
print(all_elements_meet_condition([0, 1, 2]))  # Expected output: False
print(all_elements_meet_condition([]))  # Expected output: True (since there are no elements to violate the condition)


"""
To complete this exercise:
--------------------------
No any implementation notes. 

Exercise Breakdown:
-------------------
The built-in function `all()` checks if all elements in an iterable are True. 
If the iterable is empty, `all()` returns True.

This is useful for conditions that need to be checked against every item in a collection.
"""
