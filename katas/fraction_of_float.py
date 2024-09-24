def fraction_of_float(number):
    """
    Returns the fractional part of a given float number.
    """


result = fraction_of_float(12.345)
print(result)  # Expected output: 0.345

result = fraction_of_float(7.8901)
print(result)  # Expected output: 0.8901

result = fraction_of_float(5.0)
print(result)  # Expected output: 0.0

"""
To complete this exercise:
--------------------------
Implement the 'fraction_of_float' function to extract and return the fractional part of a given float number. 


Exercise Breakdown:
-------------------
Ideas: 

- Converting a float to a string can be done with the `str()` function. 
- Convert float to int using the int() function truncates the decimal portion of the float.
"""
