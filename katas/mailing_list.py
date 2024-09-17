def mailing_list(emails):
    """
    Splits a comma-separated string of email addresses into a list of individual emails.
    """
    return emails.split(',')

def add_to_list(emails_str, new_email):
    """
    Adds the new_email to an existing comma-separated emails_str and returns the updated string.
    """
    if emails_str:  # If the existing string is not empty
        return emails_str + ',' + new_email
    else:
        return new_email

# Test cases
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
