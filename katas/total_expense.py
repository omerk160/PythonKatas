def calculate_total_expenses(expenses):
    """
    Calculates the total of a list of expenses.
    """
    total = 0
    # for loop here ....
        # total += ....

    return total

expenses = [120.50, 85.25, 40.00, 22.75]
result = calculate_total_expenses(expenses)
print(result)  # Expected output: 268.50

expenses = [300.00, 150.50, 45.75]
result = calculate_total_expenses(expenses)
print(result)  # Expected output: 496.25

expenses = []
result = calculate_total_expenses(expenses)
print(result)  # Expected output: 0.00

"""
To complete this exercise:
--------------------------
Complete the 'calculate_total_expenses' function to sum a list of expenses using an aggregator variable.


Exercise Breakdown:
-------------------
When summing values from a list, an aggregator variable is used to keep track of the running total. 
This variable is initialized outside the loop and then updated inside the loop as each element of the list is processed.

Additionally, Python provides the built-in `sum()` function that can be used to achieve the 
same result more concisely. But don't use it in this exercise. 
"""
