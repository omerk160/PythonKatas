def strong_pass(password):
    """
    This function returns True if the given password is strong enough
    """



print(strong_pass('##$FgC7^^5a'))   # True expected


"""
To complete this exercise:
--------------------------
A password is considered strong if it satisfies the following criteria:

1) Its length is at least 6.
2) It contains at least one digit.
3) It contains at least one lowercase English character.
4) It contains at least one uppercase English character.
5) It contains at least one special character. The special characters are: !@#$%^&*()-+



Exercise Breakdown:
-------------------
The `re` module in Python provides support for regular expressions, which allow you to search for patterns in strings:

import re

# Check if a string contains a digit
print(bool(re.search(r'\d', 'abc123')))  # True, because 123 contains digits

# Check if a string contains an uppercase letter
print(bool(re.search(r'[A-Z]', 'helloWorld')))  # True, because 'W' is uppercase
"""