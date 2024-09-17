def is_shopping_list_complete(shopping_list):
    """
    Returns True if the shopping list has at least 3 items, otherwise False.
    """


list_1 = ["milk", "eggs"]
print(is_shopping_list_complete(list_1))  # False expected

list_2 = ["bread", "butter", "jam"]
print(is_shopping_list_complete(list_2))  # True expected

list_3 = ["apple"]
print(is_shopping_list_complete(list_3))  # False expected

"""
To complete this exercise:
--------------------------
Implement the 'is_shopping_list_complete' function. It should return True if the shopping list has at least 3 items.
Otherwise, return False.

Exercise Breakdown:
-------------------
A list in Python is a collection of items stored in a specific order. 
You can create list by: 

You can create a list by placing items inside square brackets, separated by commas: 

items = ["pen", "book", "notebook"]

You can count how many items are in the list using the 'len()' function.

print(len(items))   # "3" is expected
"""
