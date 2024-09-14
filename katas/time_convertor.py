def time_convertor(value, unit):
    if unit == 'minutes':
        return value * 60
    elif unit == 'hours':
        return int(value * 60 * 60)
    elif unit == 'days':
        return value * 60 * 60 * 24
    elif unit == 'seconds':
        return value


converted_time_1 = time_convertor(2, 'minutes')
print(converted_time_1)  # 120 expected

converted_time_2 = time_convertor(3, 'hours')
print(converted_time_2)  # 10800 expected

converted_time_3 = time_convertor(1, 'days')
print(converted_time_3)  # 86400 expected

converted_time_4 = time_convertor(45, 'seconds')
print(converted_time_4)  # 45 expected

converted_time_5 = time_convertor(0.5, 'hours')
print(converted_time_5)  # 1800 expected

"""
To complete this exercise:
--------------------------
Implement the 'time_convertor' function to convert the given time value to seconds.
The function should handle the following units: 'seconds', 'minutes', 'hours', and 'days'.


Exercise Breakdown:
-------------
The `==` operator in Python is used to compare two values to check if they are equal. 
It returns `True` if the values are equal and `False` otherwise.

Example:

a = 'hi'
b = 'hi'
c = 'Hi'

print(a == b)  # This will output: True
print(a == c)  # This will output: False
"""

