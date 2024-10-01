def dicts_in_order(input_dict):
    """
    Returns a list of tuples containing the key-value pairs from the input dictionary.
    """


# Example usage
sample_dict = {"a": 1, "b": 2, "c": 3}

tuples_list = dicts_in_order(sample_dict)
print(tuples_list)  # [('a', 1), ('b', 2), ('c', 3)]

"""
To complete this exercise:
--------------------------
Alex likes to iterate over dictionaries, but since the order of elements in a dictionary is not guaranteed, 
he wants to convert the dictionary into a list of tuples to preserve the key-value pairs in a fixed order.


Exercise Breakdown:
-------------------
There are several methods provided by the dictionary object to access its data:

`items()` Method:
    - The `items()` method returns a view object that displays a list of dictionary's key-value tuple pairs.
    - Example: `{'a': 1, 'b': 2}.items()` results in `dict_items([('a', 1), ('b', 2)])`.

`keys()` Method:
    - The `keys()` method returns a view object that displays a list of all the keys in the dictionary.
    - Example: `{'a': 1, 'b': 2}.keys()` results in `dict_keys(['a', 'b'])`.

`values()` Method:
    - The `values()` method returns a view object that displays a list of all the values in the dictionary.
    - Example: `{'a': 1, 'b': 2}.values()` results in `dict_values([1, 2])`.
"""