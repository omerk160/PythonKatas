def monotonic_array(lst):
    """
    This function returns True/False if the given list is monotonically increased or decreased
    """
    increasing = True
    decreasing = True

    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            decreasing = False
        if lst[i] < lst[i - 1]:
            increasing = False

    return increasing or decreasing


print(monotonic_array([1, 2, 3, 6, 8, 9, 0]))  # False
print(monotonic_array([1, 2, 2, 2, 8, 9, 10]))  # True
