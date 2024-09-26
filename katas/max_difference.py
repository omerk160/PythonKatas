def max_difference(numbers):
    """
    This function takes a list of numbers and returns the maximum difference
    between any two elements in the list.
    """

    max_diff = 0  # Initialize the maximum difference to 0

    # Compare each element with every other element
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])  # Calculate the absolute difference
            if diff > max_diff:  # Update max_diff if the current difference is larger
                max_diff = diff

    return max_diff

number_list = [3, 10, 6, 2, 8]
result = max_difference(number_list)
print("Maximum difference:", result)   # Expected output: 8 (difference between 10 and 2)


"""
To complete this exercise:
--------------------------
Implement the `max_difference` function to find the largest absolute difference between two numbers.


Exercise Breakdown:
-------------------
A nested for loop (a for loop inside another for loop) allows you to compare or operate on pairs of elements in a list:

for i in numbers:
    for j in numbers:
        # Compare num i with num j
"""
