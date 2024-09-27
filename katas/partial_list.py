def partial_list(input_list, fraction):
    """
    Given a list and a fraction (0 < fraction <= 1),
    return a new list containing only the part of the input list
    that corresponds to the specified fraction.

    For example:
    If the input_list is [1, 2, 3, 4, 5] and fraction is 0.4,
    the output should be [1, 2].
    """
    if fraction <= 0 or fraction > 1:
        return None

    x = int(len(input_list) * fraction)

    # Return the slice of the list
    return input_list[:x]



print(partial_list([1, 2, 3, 4, 5], 0.4))  # Expected output: [1, 2]
print(partial_list(['a', 'b', 'c', 'd'], 0.5))  # Expected output: ['a', 'b']
print(partial_list([10, 20, 30, 40], 1))  # Expected output: [10, 20, 30, 40]


"""
To complete this exercise:
--------------------------
No any implementation noted.
"""
