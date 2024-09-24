def replace_email(email_list, old_email, new_email):
    """
    This function replaces an old email with a new email in the provided list of emails.
    """


email_list = ["email1@example.com", "email2@example.com", "email3@example.com"]
updated_list = replace_email(email_list, "email2@example.com", "new_email@example.com")
print("Updated email list:", updated_list)  # Expected output: Updated email list: ['email1@example.com', 'new_email@example.com', 'email3@example.com']


"""
To complete this exercise:
--------------------------
You can use a loop to iterate through the list and check for the old email.
When found, replace it with the new email.


Exercise Breakdown:
-------------------
To override an element in a list, use its index to assign a new value.

my_list = [10, 20, 30]
my_list[1] = 25  # This changes the second element from 20 to 25
"""
