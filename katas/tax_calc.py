def tax_calc(income1, income2, income3):
    tax1 = income1 * 0.1
    tax2 = income2 * 0.15
    tax3 = income3 * 0.2
    total_tax = tax1 + tax2 + tax3
    return total_tax


total_tax = tax_calc(50000, 80000, 120000)
print(total_tax)  # 41000.0 expected based on the provided tax rates below

total_tax = tax_calc(30000, 60000, 90000)
print(total_tax)  # 30000.0 expected based on the provided tax rates below

"""
To complete this exercise:
--------------------------
Implement the 'tax_calc' function to calculate the total tax for three income values.
Use the following tax rates for each income value:
- Income1: 10%  (0.1)
- Income2: 15%  (0.15)
- Income3: 20%  (0.2)


Exercise Breakdown:
-------------------
In Python, you can define functions that accept multiple arguments. 
This allows you to pass multiple values to the function when you call it. 
These arguments can then be used within the function to perform calculations or other operations.

An argument can be used only from within the function where it is defined. 
This is because arguments have a local scope, meaning they are accessible only within the function. 
Outside the function, these arguments are not available.

Example:
--------
def example_function(x):
    y = x + 1  # 'y' is defined inside the function and is only accessible within this function
    return y


print(y)  # This will raise a NameError because 'y' is not defined outside the function
"""

