def sum_even_numbers(lst):
    """
    This function is supposed to return the sum of all even numbers in the list.
    However, there is an error in the loop implementation. Fix it so that the function works correctly.
    """
    total = 0
    for i in range(lst):
        if lst[i] % 2 == 0:
            total += lst[i]
    return total


number_list = [1, 2, 3, 4, 5, 6]
result = sum_even_numbers(number_list)
print("Sum of even numbers:", result)   # Expected output: 12 (2 + 4 + 6)


"""
To complete this exercise:
--------------------------
No any implementation notes. 


Exercise Breakdown:
-------------------
The range() function takes an integer as an argument, not a list.
"""
