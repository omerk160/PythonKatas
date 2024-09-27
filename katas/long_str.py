def long_str(words, length):
    """
    Checks if any string in the given list of words has the specified length.
    """


print(long_str(["hello", "world", "python"], 5))  # Expected output: True
print(long_str(["hello", "world", "python"], 6))  # Expected output: False
print(long_str(["hi", "there", "everyone"], 2))  # Expected output: True
print(long_str(["hi", "there", "everyone"], 3))  # Expected output: False
print(long_str([], 3))  # Expected output: False


"""
To complete this exercise:
--------------------------
You may create a new list in which each element match the word length in the original list. 
Then, use the `any()` function to determine if there are any elements in this new list. 


Exercise Breakdown:
-------------------
The built-in function `any()` checks if any element in an iterable is True. 
If the iterable is empty, `any()` returns False. 
"""
