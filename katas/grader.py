def grade_check(score):
    """
    Determines the grade based on the score.
    """

    # fixme
    if score >= 60:
        return 'D'
    elif score >= 70:
        return 'C'
    elif score >= 80:
        return 'B'
    elif score >= 90:
        return 'A'

    return 'F'


result = grade_check(85)
print(result)  # Expected output: B

result = grade_check(92)
print(result)  # Expected output: A

result = grade_check(67)
print(result)  # Expected output: D

result = grade_check(55)
print(result)  # Expected output: F

"""
To complete this exercise:
--------------------------
Fix the logical issue in the 'grade_check' function. The current implementation does not correctly assign grades 
based on the score.


Exercise Breakdown:
-------------
In Python, a function can have multiple return statements. When a return statement is executed, the function exits 
immediately, and the value specified in the return statement is sent back to the caller. 

Using multiple return statements allows a function to handle different conditions and provide appropriate results 
based on the input.

def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"

    return "Zero"

The return at the end of the function is a "catch-all" for any cases that do not match the previous conditions. 
"""
