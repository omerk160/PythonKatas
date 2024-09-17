def get_sandwich_ingredients(sandwich):
    """
    Returns the middle elements of the sandwich list
    """


sandwich_ingredients = ["bread", "lettuce", "tomato", "cheese", "bread"]
print(get_sandwich_ingredients(sandwich_ingredients))  # ["lettuce", "tomato", "cheese"] expected

sandwich_ingredients = ["bread", "butter", "lettuce", "tomato", "cheese", "bread"]
print(get_sandwich_ingredients(sandwich_ingredients))  # ["butter", "lettuce", "tomato", "cheese"] expected

sandwich_ingredients = ["bread", "mustard", "lettuce", "tomato", "onion", "avocado", "bread"]
print(get_sandwich_ingredients(sandwich_ingredients))  # ["mustard", "lettuce", "tomato", "onion", "avocado"] expected

sandwich_ingredients = ["bread", "bread"]
print(get_sandwich_ingredients(sandwich_ingredients))  # [] expected


"""
To complete this exercise:
--------------------------
Implement the 'get_sandwich_ingredients' function to return the middle elements of 'sandwich', excluding the first and last elements.
If the list has less than 3 elements, return an empty list.


Exercise Breakdown:
-------------------
You can extract a portion of a list using slicing. The syntax for slicing is:
list[start:end]

- 'start' is the index where the slice starts (inclusive).
- 'end' is the index where the slice ends (exclusive).

numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])  # [1, 2, 3]
"""
