def age_message(age):
    """
    Returns a message that combines a string and an integer representing age.
    """
    message = "I am " + str(age) + " years old."
    return message


result = age_message(25)
print(result)  # "I am 25 years old." expected

"""
To complete this exercise:
--------------------------
Fix the function call - i.e. "result = age_message(25)" - so the program runs properly.
Modify only the function call, without changing the `age_message` function implementation itself.
 
Exercise Breakdown:
-------------------
In Python, you cannot directly concatenate a string with an integer.
  
To fix it, you should call the function with an str argument (or convert the argument to str using the `str()` function).
 
In Python, variables are dynamically typed, which means a variable can hold values of different types 
(such as `str`, `int`, etc.) at different points in the program. This is called *dynamic typing*.
"""
