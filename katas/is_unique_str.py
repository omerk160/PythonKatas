def is_unique_str(text):
    """
    This function checks if all characters in the provided string are unique.
    If the string contains any repeated characters, it returns False.
    Otherwise, it returns True.
    """


print(is_unique_str("abcdef"))  # Expected output: True
print(is_unique_str("hello"))  # Expected output: False
print(is_unique_str(""))  # Expected output: None


"""
To complete this exercise:
--------------------------
A naive solution to check for unique characters is to compare each character in the string with every other character using nested loops.
This approach works but is less efficient than the suggest below breakdown. 


Exercise Breakdown:
-------------------
In Python, a `set` is a collection that contains unique elements only, meaning it automatically removes any duplicates:

my_set = {1, 2, 3, 3, 4}  # Duplicates are removed, so my_set becomes {1, 2, 3, 4}
my_set.add(5)  # Adds 5 to the set
my_set.add(5)  # No effect since 5 is already exist
my_set.remove(2)  # Removes 2 from the set

A list can be converted to set by: `set(text)`.
"""