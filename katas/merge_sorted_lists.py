def merge_sorted_lists(l1, l2):
    """
    This function gets two sorted lists (each one of them is sorted)
    and returns a single sorted list combining both of them.
    """
    merged_list = []
    i, j = 0, 0  # Pointers for both lists

    # Traverse both lists
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged_list.append(l1[i])
            i += 1
        else:
            merged_list.append(l2[j])
            j += 1

    # If there are remaining elements in l1
    while i < len(l1):
        merged_list.append(l1[i])
        i += 1

    # If there are remaining elements in l2
    while j < len(l2):
        merged_list.append(l2[j])
        j += 1

    return merged_list




print(merge_sorted_lists([1, 4, 9, 77, 13343], [-7, 0, 7, 23]))  # Expected # [-7, 0, 1, 4, 7, 9, 23, 77, 13343]


"""
To complete this exercise:
--------------------------
Try to be as efficient as you can - don't use Python's built in sort() or sorted() functions!


Exercise Breakdown:
-------------------
`sort()` - Sorts a list in-place, meaning it sorts the original list and does not return a new one.
`sorted()` - Sorts the list but returns a new list with the elements sorted, leaving the original iterable unchanged.
"""

