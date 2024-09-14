def add_string_numbers(num1, num2, num3):
    result = int(num1) + int(num2) + int(num3)
    return result



result = add_string_numbers("10", "20", "30")
print(result)  # 60 expected

result = add_string_numbers("5", "15", "25")
print(result)  # 45 expected

result = add_string_numbers("100", "200", "300")
print(result)  # 600 expected


"""
To complete this exercise:
--------------------------
Implement the 'add_string_numbers' function to convert the given string numbers to integers 
and return the sum of those integers.


Exercise Breakdown:
-------------------
Understanding how to convert data types using functions like int() will help you solve this exercise.
"""
