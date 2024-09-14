def create_greeting():
    greeting = 'Hello'
    name = 'World'
    return greeting + "," + name + "!"


result = create_greeting()
print(result)  # "Hello, world!" expected

"""
To complete this exercise:
--------------------------
Complete the 'create_greeting' function by concatenating the `greeting` and `name` variables 
with a comma and space in between, and add an exclamation mark at the end.

Exercise Breakdown:
-------------------
In Python, strings are sequences of characters, wrapper by "..." or '...' (there is not difference).
In order to concatenate two strings, use the `+` operator.
"""
