def count_even_numbers(numbers):
    """
    Returns the count of even numbers in the list.
    """
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1

        return count


numbers_list = [1, 2, 3, 4, 5, 6]
print(count_even_numbers(numbers_list))  # 3 expected

numbers_list = [7, 8, 9, 10]
print(count_even_numbers(numbers_list))  # 2 expected

numbers_list = [1, 3, 5, 7]
print(count_even_numbers(numbers_list))  # 0 expected


"""
To complete this exercise:
--------------------------
In this function, the goal is to count how many numbers in the list are even, but is has a bug.
Fix the function to work properly.


Exercise Breakdown:
-------------------
The `return` statement stops the function immediately and returning the value. 
"""
