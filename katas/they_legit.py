def they_legit(people, is_legit):
    """
    Returns a list of all legit people based on the 'is_legit' lambda function.
    """


# Example usage
people_list = [
    {"name": "Alice", "age": 30, "verified": True},
    {"name": "Bob", "age": 25, "verified": False},
    {"name": "Charlie", "age": 35, "verified": True}
]

legit_checker = lambda person: person["verified"]

legit_people = they_legit(people_list, legit_checker)
print(legit_people)  # ['Alice', 'Charlie']

"""
To complete this exercise:
--------------------------
The lambda function, based on a `person` argument as an input, will check the 'verified' status of each person in the list.


Exercise Breakdown:
-------------------
When you pass a lambda function to another function, such as `they_legit`, you're not CALLING the lambda function.
Instead, you're passing a REFERENCE to the function itself.
This means that the lambda acts as a pointer to the function rather than executing it immediately.
"""