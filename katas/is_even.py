def is_even(number):
    if (number % 2 == 0):
        return True
    else:
        return False


result_1 = is_even(4)
print(result_1)  # True expected

result_2 = is_even(7)
print(result_2)  # False expected

result_3 = is_even(0)
print(result_3)  # True expected

result_4 = is_even(-2)
print(result_4)  # True expected


"""
To complete this exercise:
--------------------------
Implement the 'is_even' function to check if the given number is even.
The function should return `True` if the number is even, and `False` otherwise.


Exercise Breakdown:
-------------------
In Python, the boolean type is used to represent truth values.
There are only two boolean values: `True` and `False`. 

Boolean values are often used in conditional statements and functions to control the flow of a program. 
In this exercise, you will use a boolean value to indicate whether a number is even or not.
"""
