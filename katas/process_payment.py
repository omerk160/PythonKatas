def process_payment(payment):
    """
    Returns a formatted string of the provided amount, or None if the input is invalid.

    The `payment` argument can be either a single float, a string, or a list of floats.
    """
    if isinstance(payment, float):
        # Format a single float as currency
        return f"${payment:.2f}"

    elif isinstance(payment, str):
        try:
            # Try converting string to float
            amount = float(payment)
            return f"Payment Ref: ${amount:.2f}"
        except ValueError:
            return None  # Return None if conversion fails

    elif isinstance(payment, list):
        # Ensure all elements in the list are floats
        if all(isinstance(x, float) for x in payment):
            total = sum(payment)
            return f"${total:.2f}"
        else:
            return None  # Return None if any element is not a float

    return None  # Return None for unsupported types


# Example test cases
print(process_payment(123.456))  # Expected output: $123.46
print(process_payment("12345"))  # Expected output: Payment Ref: $12345.00
print(process_payment([50.75112, 25.25665, 10.987]))  # Expected output: $86.00
print(process_payment(["not", "a", "number"]))  # Expected output: None
