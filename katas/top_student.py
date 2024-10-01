students = [
    {'name': 'Alice', 'grade': 85, 'birthdate': '2001-05-15'},
    {'name': 'Bob', 'grade': 92, 'birthdate': '2000-03-22'},
    {'name': 'Charlie', 'grade': 87, 'birthdate': '2002-07-30'},
    {'name': 'David', 'grade': 90, 'birthdate': '1999-12-09'},
    {'name': 'Eva', 'grade': 95, 'birthdate': '2003-01-17'},
    {'name': 'Frank', 'grade': 78, 'birthdate': '2001-11-05'}
]


def top_student(data):
    """
    Returns the student dict with the highest grade
    """
    return max(data)


result = top_student(students)
print(top_student)  # {'name': 'Eva', 'grade': 95, 'birthdate': '2003-01-17'} expected


"""
To complete this exercise:
--------------------------
Fix the implementation of the `top_student` function by using the `key` argument of the `max` function with a lambda expression.
The lambda should extract the 'grade' from each student dictionary to determine which student has the highest grade.


Exercise Breakdown:
-------------------
Lambda functions in Python are small anonymous functions defined using the `lambda` keyword.

For example: Find the max absolut value in list of numbers

numbers = [3, -5, 1, -8, 2]
max_abs_number = max(numbers, key=lambda x: abs(x))
print(max_abs_number)  # Output: 8
"""