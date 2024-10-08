def prime_number(num):
    """
    Check if the given number is prime or not.
    """
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 is the only even prime number
    if num % 2 == 0:
        return False  # Exclude all other even numbers

    # Check for factors from 3 to num - 1, skipping even numbers
    for i in range(3, num, 2):
        if num % i == 0:
            return False
    return True




print(prime_number(5))  # True
print(prime_number(22))  # False

"""
To complete this exercise:
--------------------------
A prime number is an integer greater than 1 that cannot be divided by any other numbers except 1 and itself. 

Examples of prime numbers are 2, 3, 5, 7, 11, 13, etc.
 
A number is **not prime** if it can be divided evenly by another number (other than 1 and itself).
"""
