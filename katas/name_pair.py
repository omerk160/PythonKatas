def generate_name_pairs(names):
    """
    This function takes a list of names and returns a list of tuples,
    where each tuple contains all possible pairs of names.
    """



name_list = ["Alice", "Bob", "Charlie"]
all_pairs = generate_name_pairs(name_list)
print("All name pairs:", all_pairs)  # Expected output: [('Alice', 'Bob'), ('Alice', 'Charlie'), ('Bob', 'Charlie')]


"""
To complete this exercise:
--------------------------
Implement the `generate_name_pairs` function to find all possible pairs from the list of names.
Use a nested `for` loop to iterate through the names and create pairs without repeating the same pair twice.


Exercise Breakdown:
-------------------
A loop can be placed inside another loop to iterate over multiple levels.
In this exercise, the outer loop picks a name, and the inner loop pairs it with every following name.
"""
