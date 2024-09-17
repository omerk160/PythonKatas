def add_to_list(emails_str, new_email):
    """
    Adds the new_email to an existing emails_str.
    """


def mailing_list(emails):
    """
    Splits a comma-separated string of email addresses into a list of individual emails.
    """


email_string = "alice@example.com,bob@example.com,charlie@example.com"
result = mailing_list(email_string)
print(result)  # Expected output: ['alice@example.com', 'bob@example.com', 'charlie@example.com']

email_string = "john.doe@example.com"
result = mailing_list(email_string)
print(result)  # Expected output: ['john.doe@example.com']

email_string = "jane@example.com,,doe@example.com"
result = mailing_list(email_string)
print(result)  # Expected output: ['jane@example.com', '', 'doe@example.com']

emails = add_to_list("alice@example.com,bob@example.com", "dave@example.com")
print(emails)  # Expected output: 'alice@example.com,bob@example.com,dave@example.com'


"""
To complete this exercise:
--------------------------
1. Implement the 'mailing_list' function to correctly split a comma-separated string of email addresses into a list 
   of individual email addresses.
2. Implement the 'add_to_list' function to add the new_email to an existing emails_str.


Exercise Breakdown:
-------------------
String concatenation can be performed using the `+` operator, combining multiple strings into a single string. 
This is useful for building dynamic strings from smaller components.

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2    # "Hello World"

The `str.split()` method in Python is used to split a string into a list based on a specified delimiter.

x = "a b c d e"
result = x.split()   # In this case, no delimiter is specified in the split() function call, so it uses the space as a default value
print(result)  # Output: ['a', 'b', 'c', 'd', 'e']
"""
