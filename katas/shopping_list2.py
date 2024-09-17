def build_shopping_list(initial_items, new_item):
    """
    Addd new_item to the initial_items list.
    """


current_list = ["milk", "bread"]
new_item = "eggs"
print(build_shopping_list(current_list, new_item))  # ["milk", "bread", "eggs"] expected

current_list = ["apples", "oranges"]
new_item = "bananas"
print(build_shopping_list(current_list, new_item))  # ["apples", "oranges", "bananas"] expected

current_list = []
new_item = "water"
print(build_shopping_list(current_list, new_item))  # ["water"] expected


"""
To complete this exercise:
--------------------------
Implement the 'build_shopping_list' function. 


Exercise Breakdown:
-------------------
The `append()` method is used to add an item to the end of a list. 
"""
