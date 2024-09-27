def swap_elements(lst, index1, index2):
    """
    This function swaps the elements at the specified indices in the given list.

    The function returns None (it modifies the list in place).
    """


my_list = [10, 20, 30, 40, 50]
swap_elements(my_list, 1, 3)
print(my_list)  # Expected output: [10, 40, 30, 20, 50]

another_list = ['apple', 'banana', 'cherry']
swap_elements(another_list, 0, 2)
print(another_list)  # Expected output: ['cherry', 'banana', 'apple']

swap_elements(my_list, 1, 10)  # Do nothing since input is invalid


"""
To complete this exercise:
--------------------------
- The function should modify the list in place without creating a new list.
- Handle invalid input by checking if the indices are within the bounds of the list.

Exercise Breakdown:
-------------------
In Python, lists are mutable, meaning you can modify them directly without creating a new instance.
"""
