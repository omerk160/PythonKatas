def find_student(student_list, student_name):
    """
    Checks if a student is in the list of enrolled students.
    """


students = ["Alice", "Bob", "Charlie", "Diana"]

result = find_student(students, "Alice")
print(result)  # Expected output: Alice is enrolled.

result = find_student(students, "Eve")
print(result)  # Expected output: Eve is not enrolled.

result = find_student(students, "Bob")
print(result)  # Expected output: Bob is enrolled.

result = find_student(students, "Frank")
print(result)  # Expected output: Frank is not enrolled.


"""
To complete this exercise:
--------------------------
Implement the 'find_student' function to check if a specific student is in the list of enrolled students.


Exercise Breakdown:
-------------
The `in` operator is used to check for membership within a collection, such as a list. It returns `True` if the 
specified item is found in the list, and `False` otherwise.

"""
