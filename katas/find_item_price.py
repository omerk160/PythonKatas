def find_item_price(items_dict, category, item):
    """
    This function takes a dictionary of categories, where each category is a dict of items, and returns the price of
    the specified item within the specified category, or None if the item or category doesn't exist.
    """


items = {
    "Fruits": {"apple": 2, "banana": 1.5, "orange": 3},
    "Vegetables": {"carrot": 1, "broccoli": 2.5, "spinach": 3}
}

print(find_item_price(items, "Fruits", "apple"))  # Expected output: 2
print(find_item_price(items, "Vegetables", "broccoli"))  # Expected output: 2.5
print(find_item_price(items, "Vegetables", "potato"))  # Expected output: None
print(find_item_price(items, "Dairy", "milk"))  # Expected output: None

"""
To complete this exercise:
--------------------------
Check whether both the category and the item exist in the nested dictionary.


Exercise Breakdown:
-------------------
A nested dictionary is a dictionary where values can themselves be dictionaries.
You can access these nested dictionaries using two keys, like so: dict[key1][key2].
"""
