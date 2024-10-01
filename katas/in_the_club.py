def in_the_club(person):
    """
    Checks if a person is eligible to enter the club.
    A person is eligible if they have either an 'id' or 'passport' key and are above 18 years old.
    """


person_1 = {'name': 'Alice', 'age': 20, 'id': '12345'}
person_2 = {'name': 'Bob', 'age': 17, 'passport': '98765'}
person_3 = {'name': 'Charlie', 'age': 22}
person_4 = {'name': 'David', 'age': 19, 'id': '54321', 'passport': '87654'}

print(in_the_club(person_1))  # True expected
print(in_the_club(person_2))  # False expected
print(in_the_club(person_3))  # False expected
print(in_the_club(person_4))  # True expected


"""
To complete this exercise:
--------------------------
Check if a person is eligible to enter the club.
A person is eligible if they have either an 'id' or 'passport' key and are above 18 years old.


Exercise Breakdown:
-------------
To check if a key exists in a dictionary, use the `in` keyword or the `get` method.
Make sure you understand the behaviors of the get() method. 
"""