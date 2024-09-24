def split_full_name(full_name):
    """
    Splits a full name into first and last name and returns them as a tuple.
    """


full_name = "Alice Johnson"
first_name, last_name = split_full_name(full_name)
print(f"First name: {first_name}, Last name: {last_name}")  # Expected output: First name: Alice, Last name: Johnson

full_name = "Bob Smith"
first_name, last_name = split_full_name(full_name)
print(f"First name: {first_name}, Last name: {last_name}")  # Expected output: First name: Bob, Last name: Smith

full_name = "Charlie Brown"
first_name, last_name = split_full_name(full_name)
print(f"First name: {first_name}, Last name: Brown")   # Expected output: First name: Charlie, Last name: Brown


"""
To complete this exercise:
--------------------------
Implement the 'split_full_name' function to return the first and last elements as a tuple (first name, last name).


Exercise Breakdown:
-------------------
In python, a `tuple` is a collection of ordered elements. 
It is similar to a list but is immutable (cannot be changed after creation).

When you return multiple values from a function using commas, Python automatically groups them into a tuple. 

For example:

def get_coordinates():
    return 10, 20  # This returns a tuple (10, 20)

"""
