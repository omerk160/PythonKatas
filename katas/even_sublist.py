from katas.is_prime import number


def even_sublist(numbers):
    """
    Returns a new list containing only the even numbers from the provided list.

    :param numbers: list of integers
    :return: list of even integers
    """
    list = []
    for i in range (len(numbers)):
        if numbers[i] % 2 ==0:
            list.append(numbers[i])

    return list



result = even_sublist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(result)  # Expected output: [2, 4, 6, 8, 10]

result = even_sublist([11, 13, 15])
print(result)  # Expected output: []

result = even_sublist([0, -2, -4, 1, 5, 7])
print(result)  # Expected output: [0, -2, -4]

result = even_sublist([-1, -2, -3, -4])
print(result)  # Expected output: [-2, -4]

"""
To complete this exercise:
--------------------------
No any implementation notes. 


Exercise Breakdown:
-------------------
To check if a number is even use the modulus operator %.
If number % 2 == 0, the number is even.
"""