def best_student(grades):
    """
    This function receives a dict of (student name -> grade) mapping, and returns the student with the highest grade
    """
    best_student_name = None
    highest_grade = 0

    # Iterate through the dictionary to find the highest grade
    for student, grade in grades.items():
        if grade > highest_grade:
            highest_grade = grade
            best_student_name = student

    return best_student_name


print(best_student({
    "Dan": 78,
    "Jessica": 88,
    "John": 99,
    "Daniel": 65,
    "Lindsy": 95
}))   # Expected John
