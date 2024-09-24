def is_valid_password(password):
    if len(password) < 8:
        return False
    #Compare lower and upper strings to the original string
    if password.upper() == password:
        #.upper() turns all string to CAPS
        #When checking if the capped version matches the original, this checks if the original string was capped, thus not answering requirements.
        return False
    if password.lower() == password:
        #.upper() turns all string to CAPS
        #When checking if the capped version matches the original, this checks if the original string was capped, thus not answering requirements.
        return False
    return True


# Test cases
print(is_valid_password("Passw0rd"))  # Expected output: True
print(is_valid_password("password"))  # Expected output: False
print(is_valid_password("PASSWORD"))  # Expected output: False
print(is_valid_password("P@ssw0rd"))  # Expected output: True

"""
To complete this exercise:
--------------------------
Implement the 'is_valid_password' function to check if the provided password meets the required criteria. 
The criteria include having a minimum length of 8 characters, containing at least one uppercase letter, 
and at least one lowercase letter.

Exercise Breakdown:
-------------
The .lower() and .upper() methods can convert a given string to lower or upper case, respectively. 

name = "John"
print(name.upper())   # JOHN is printed
 
"""
