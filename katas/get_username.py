def get_username(email):


    return email.split('@')[0]


email_1 = "alice.smith@example.com"
print(get_username(email_1))  # "alice.smith" expected

email_2 = "bob.jones@example.com"
print(get_username(email_2))  # "bob.jones" expected

email_3 = "carol@example.com"
print(get_username(email_3))  # "carol" expected


"""
To complete this exercise:
--------------------------
Implement the 'get_username' function. The email address (email) has a fixed format where the domain is always `example.com`

You need to extract the username part by slicing the string.

Exercise Breakdown:
-------------------
Strings can be sliced the same way lists can. 
"""
