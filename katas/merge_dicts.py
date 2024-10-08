def merge_dicts(dict1, dict2):
    """
    This functions merges the content of dict2 into dict1, and returns dict1
    """


conf1 = {'a': 1, 'b': 99}
conf2 = {'b': 2, 'c': 6}

merge_dicts(conf1, conf2)
print(conf1)  # Expected {'a': 1, 'b': 2, 'c': 6}


"""
To complete this exercise:
--------------------------
Ensure that when there are keys present in both dictionaries, the values from `dict2` override the values from `dict1`.


Exercise Breakdown:
-------------------
Merging dictionaries is a common task, and there are several methods available to do this

- The `update()` method to merge `dict2` into `dict1`.
- The unpacking operator `**` to merge dictionaries into a new dictionary.
"""

