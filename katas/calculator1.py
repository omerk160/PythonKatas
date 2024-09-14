def calculator1(num1, num2):
    """ No need to touch this implementation"""
    if type(num1) != int or type(num2) != int:
        return None
    else:
        return num1 + num2


result = calculator1(1, 1)  # 2 expected
print(result)

# TODO fill in the correct arguments
print(calculator1(0, 0))  # 0 expected
print(calculator1(-10, 2))  # -8 expected
print(calculator1(0.33, 0.88))  # None expected

"""
To complete this exercise:
--------------------------
Call the 'calculator1' function with appropriate arguments to produce the expected output for each case.


Exercise Breakdown:
-------------------
Functions can be called with specific arguments to produce a result.
You can either assign the result of a function call to a variable, e.g.

result = calculator1(1, 1)
print(result)
 
Or use the result immediately in other expressions or function calls, e.g.:

print(calculator1(1, 1))

In this exercise, you have a `calculator1` function that takes two integer arguments and returns their sum if both arguments are integers.
If either argument is not an integer, it returns `None`.
"""

