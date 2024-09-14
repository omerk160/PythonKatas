def bad_average(a, b, c):
    """
    Calculates the average of three numbers.
    """
    return int((a + b + c) / 3)


result = bad_average(3, 6, 9)
print(result)  # Expected output: 6.0

result = bad_average(10, 20, 30)
print(result)  # Expected output: 20.0

result = bad_average(5, 15, 25)
print(result)  # Expected output: 15.0

"""
To complete this exercise:
--------------------------
Fix the 'bad_average' function by adding parentheses to correctly calculate the average of three numbers.


Exercise Breakdown:
-------------------
Parentheses play a crucial role in determining the order of operations in mathematical expressions in Python.
Without the correct use of parentheses, you might not get the expected result due to the default precedence
of operators.
"""
