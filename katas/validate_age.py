def validate_age(age):
    """
    This function checks if the provided age is a valid integer
    between 0 and 120. If the input is invalid, it returns None.
    """


print(validate_age(25))   # Expected output: 25
print(validate_age(-5))   # Expected output: None
print(validate_age(130))  # Expected output: None
print(validate_age("30")) # Expected output: None
print(validate_age(3.0))  # Expected output: None


"""
To complete this exercise:
--------------------------
Implement input validation to ensure the provided age is a valid integer between 0 and 120.
If the input is invalid, return None.

Exercise Breakdown:
-------------------
Use `isinstance()` to check the type of a given variable. 
"""
