def create_student_dict(name, age, grades):
    """
    Creates a dictionary for a student with their name, age, and grades.
    """
    return {'name': name, 'age': age, 'grades': grades}


def get_average_grade(student_dict):
    """
    Calculates the average grade from the student's grades in the dictionary.

    :param student_dict: dict. A dictionary containing student information.
    :return: float. The average of the student's grades.
    """
    grades = student_dict['grades']
    return sum(grades) / len(grades) if grades else 0


if __name__ == '__main__':
    student = create_student_dict('Alice', 20, [90, 85, 88])
    print(f"Student Info: {student}")  # Expected output: Student Info: {'name': 'Alice', 'age': 20, 'grades': [90, 85, 88]}
    print(f"Average Grade: {get_average_grade(student):.2f}")  # Expected output: Average Grade: 87.67


"""
To complete this exercise:
--------------------------
Implement the `create_student_dict` function to create a dictionary 
for a student and the `get_average_grade` function to calculate 
the average of the student's grades.


Exercise Breakdown:
-------------------
A dictionary in Python is a mutable, unordered collection of 
key-value pairs. It allows you to store and retrieve data using 
unique keys. In this exercise, we create a dictionary to store 
student information, including their name, age, and grades, and 
calculate their average grade using the dictionary's values.
"""
