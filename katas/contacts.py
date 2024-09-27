def add_contact(contact_book, name, phone_number):
    """
    Adds a contact with the given name and phone number to the contact_book.
    If the contact already exists, it updates the phone number.
    """


contacts = {}

add_contact(contacts, "Alice", "123-456-7890")
add_contact(contacts, "Bob", "987-654-3210")
print(contacts)

add_contact(contacts, "Alice", "111-222-3333")
print(contacts)


"""
To complete this exercise:
--------------------------
No any implementation notes. 


Exercise Breakdown:
-------------------
To add a key-value pair, simply use the syntax:

dict[key] = value


In addition, dictionaries are mutable data structures.
Meaning, you can change their content without creating a new dictionary.
 
If you modify a dictionary inside a function, those changes will reflect outside the function as well.
This behavior is essential to understand when working with functions that handle dictionaries, as it can lead to unintended side effects if you are not careful.
"""

