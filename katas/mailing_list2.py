def replace_email(email_list, old_email, new_email):

    for i in range(len(email_list)):  # Loop through each index in the list
        if email_list[i] == old_email:  # Check if the current email is the old email
            email_list[i] = new_email  # Replace it with the new email
            break  # Stop the loop after replacing

    return email_list


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
