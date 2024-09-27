def check_identity(a, b):
    """
    Checks if two objects are identical (i.e., they refer to the same object in memory).
    """


x = [1, 2, 3]
y = x
z = [1, 2, 3]

result = check_identity(x, y)
print(result)  # Expected output: True

result = check_identity(x, z)
print(result)  # Expected output: False

"""
To complete this exercise:
--------------------------
No any implementation notes.


Exercise Breakdown:
-------------
In Python, every object has a unique identifier, which can be obtained using the built-in `id()` function. 
The `is` operator checks if two objects have the same `id()`, meaning they refer to the same memory location.

x = [1, 2, 3]
y = [1, 2, 3]
 
x and y are lists containing the same content, but they are different independent objects in the program memory.
"""
