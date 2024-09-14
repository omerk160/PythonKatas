def fill_a_cab(passengers, seats):
    if passengers > seats:
        return False
    else:
        return True


print(fill_a_cab(3, 4))  # True expected
print(fill_a_cab(5, 4))  # False expected
print(fill_a_cab(4, 4))  # True expected

"""
To complete this exercise:
--------------------------
Implement the 'fill_a_cab' function to return True if the number of passengers can fit in the cab seats, 
and False otherwise, using a simple if statement.


Exercise Breakdown:
-------------------
In Python, the `if` statement is used to make decisions in your code. It allows you to execute certain 
code blocks only when specific conditions are met.

The syntax:
--------
def is_two(number):
    result = False
    if number == 2:    # The == operator used to compare between things
        result = True
    
    return result

print(is_even(2))  # True
print(is_even(7))  # False
"""
