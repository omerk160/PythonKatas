def is_prime(number):
    """
    Returns True if the given number is prime, False otherwise.
    A prime number is an integer greater than 1 that has no divisors
    other than 1 and itself.
    """
    for i in range(number):
        ...  # TODO complete the loop body


number = 11
result = is_prime(number)
print(result)  # Expected output: True

number = 8
result = is_prime(number)
print(result)  # Expected output: False

number = 2
result = is_prime(number)
print(result)  # Expected output: True

number = 1
result = is_prime(number)
print(result)  # Expected output: False


"""
To complete this exercise:
--------------------------
You can check if number is prime by looping through i from 2 to the given number,
and check if your number is dividable by i. 


Exercise Breakdown:
-------------------
The `range()` function in Python generates a sequence of numbers.
It can take up to three arguments:

1. `range(stop)` - generates numbers from 0 to stop-1.
2. `range(start, stop)` - generates numbers from start to stop-1.
3. `range(start, stop, step)` - generates numbers from start to stop-1, stepping by step.
"""
