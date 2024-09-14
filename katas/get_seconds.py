def get_seconds(days):
    return (days * 24 * 60 * 60)



seconds_1 = get_seconds(1)
print(seconds_1)  # 86400 expected

seconds_2 = get_seconds(0)
print(seconds_2)  # 0 expected

seconds_3 = get_seconds(2)
print(seconds_3)  # 172800 expected


"""
To complete this exercise:
--------------------------
Implement the 'get_seconds' function to convert the given number of days into seconds.



Exercise Breakdown:
-------------
Python provides several basic mathematical operators that you can use to perform calculations:

| Op  | Description                                                     | Example      | Result |
|-----|-----------------------------------------------------------------|--------------|--------|
| +   | Adds two numbers                                                | 5 + 3        | 8      |
| -   | Subtracts one number from another                               | 10 - 4       | 6      |
| *   | Multiplies two numbers                                          | 7 * 6        | 42     |
| /   | Divides one number by another and returns a float               | 8 / 2        | 4.0    |
| //  | Divides one number by another and returns the integer part only | 8 // 3       | 2      |
| %   | Returns the remainder of a division                             | 8 % 3        | 2      |
| **  | Raises a number to the power of another                         | 2 ** 3       | 8      |
"""
