def find_min(numbers):
    """
    Finds the minimum number in a list without using the built-in min() function.
    """
    min_value = numbers[0]  # assume the 1st element is the minimum
    # for loop comes here ....
        # update min_value in the loop body

    return min_value


def find_max(numbers):
    """
    Finds the maximum number in a list without using the built-in max() function.
    """



numbers = [4, 2, 9, 11, 6, 3]
result_min = find_min(numbers)
print(result_min)  # Expected output: 2

result_max = find_max(numbers)
print(result_max)  # Expected output: 11

numbers = [-1, -7, -3, -4, -5]
result_min = find_min(numbers)
print(result_min)  # Expected output: -7

result_max = find_max(numbers)
print(result_max)  # Expected output: -1

"""
To complete this exercise:
--------------------------
Implement the 'find_min' and 'find_max' functions to find the minimum and maximum values in a list of numbers without 
using the built-in min() and max() functions.

Exercise Breakdown:
-------------
To find the minimum or maximum value in a list, you need to use a variable to keep track of the current minimum or 
maximum value. This variable is initialized outside the loop and then updated inside the loop as each element of the 
list is processed.

In the 'find_min' function, 'min_value' is initialized to the first element of the list. Inside the loop, each element 
is compared to 'min_value', and if it is smaller, 'min_value' is updated.

While Python provides the built-in `min()` and `max()` functions to find the minimum and maximum values in a list, 
the purpose of this exercise is to implement this functionality manually without using these built-in functions.
"""
