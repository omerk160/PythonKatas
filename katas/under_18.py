def count_under_18(ages):
    """
    Returns the count of elements in the list that are less than 18.
    """


ages1 = [25, 34, 17, 16, 40, 15, 28]
result = count_under_18(ages1)
print(result)  # Expected output: 3 (17, 16, 15)

ages2 = [18, 19, 20]
result = count_under_18(ages2)
print(result)  # Expected output: 0 (no elements under 18)

ages3 = [10, 12, 17, 18]
result = count_under_18(ages3)
print(result)  # Expected output: 3 (10, 12, 17)


"""
To complete this exercise:
--------------------------
No any implementation notes. 


Exercise Breakdown:
-------------------
This can be done using a `for` loop to iterate through the list and an `if` condition to check if the number is less than 18.

"""
