def reformat_phone(phone_str):
    """
    This function takes a string representing a phone number and reformats it into
    a standardized format: (XXX) XXX-XXXX, where X represents a digit.
    The function removes any non-numeric characters from the string and reformats it.

    Return None if the input is invalid (not exactly 10 digits)
    """
    # Remove all non-numeric characters
    digits = ''.join([char for char in phone_str if char.isdigit()])

    if len(digits) != 10:
        return None

    # Reformat to (XXX) XXX-XXXX
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"


print(reformat_phone("123-456-7890"))  # Expected output: (123) 456-7890
print(reformat_phone("(123) 456-7890"))  # Expected output: (123) 456-7890
print(reformat_phone("1234567890"))  # Expected output: (123) 456-7890
print(reformat_phone("123-45"))  # Expected output: None


"""
To complete this exercise:
--------------------------
No any implementation notes. 


Exercise Breakdown:
-------------------
The `isdigit()` can help you to filter out non-numeric characters.
"""
