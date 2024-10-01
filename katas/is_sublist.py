def is_sublist(l1, l2):
    """
    Returns True if the first list (l1) is contained the second list (l2) lexicographically.
    """


# Example usage
result_1 = is_sublist(['apple', 'banana'], ['apple', 'avocado', 'banana'])
print(result_1)  # True expected


result_2 = is_sublist(['banana', 'apple'], ['apple', 'banana', 'cherry'])
print(result_2)  # True expected


result_3 = is_sublist(['apple', 'banana'], ['apple'])
print(result_3)  # False expected


"""
To complete this exercise:
--------------------------
Imagine you are working on an inventory management system for a grocery store. You have two lists: 
- `l1`: a list of items to check
- `l2`: a list representing the inventory

Your task is to write a function `is_sublist` that returns `True` if the first list `l1` is 
contained in the second list `l2`. Otherwise, return `False`.


Exercise Breakdown:
-------------------
When comparing lists in Python, the comparison is done element by element.
This means that the each element in the first list should be checked against the other list. 
Then the second element in the first list should be checked against the other, and so on... 
"""