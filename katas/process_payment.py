def process_payment(payment):
    """
    Returns a formatted string of the provided amount, of None if the input is invalid.

    The `payment` argument can be either a single float, a string, or a list of floats.
    """


print(process_payment(123.456))  # Expected output: $123.46
print(process_payment("12345"))  # Expected output: Payment Ref: $12345.00
print(process_payment([50.75112, 25.25665, 10.987]))  # Expected output: $86.00
print(process_payment(["not", "a", "number"]))  # Expected output: None

"""
To complete this exercise:
--------------------------
The 'process_payment' function should handle different types of payment inputs: float, string, and list of floats.

First, determine the type of the input and apply the appropriate processing. For lists, ensure all items 
are floats before summing. Format the output for floats and sums as currency strings.


Exercise Breakdown:
-------------------
The `isinstance()` or the `type()` built-in functions are used to check the type of an argument.

To round a float number to two decimals after the floating numer, use f'' string as follows:

x = 123.456789
print(f"${x:.2f}")  # output 123.45
"""