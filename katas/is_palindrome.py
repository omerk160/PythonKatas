def is_palindrome(number):
    """
    Checks if a given number is a palindrome.
    A number is a palindrome if it reads the same forwards and backwards.
    """


result = is_palindrome(12321)
print(result)  # Expected output: True

result = is_palindrome(12345)
print(result)  # Expected output: False

result = is_palindrome(1001)
print(result)  # Expected output: True

result = is_palindrome(1)
print(result)  # Expected output: True

"""
To complete this exercise:
--------------------------
Implement the 'is_palindrome' function to check if a number is a palindrome.


Exercise Breakdown:
-------------------
To reverse the string the `[::-1]` slice can be used.  
"""