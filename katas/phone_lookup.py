def find_contact(phonebook, name):
    """
    Look up a contact's phone number by their name in the phonebook.

    Returns the phone number if found, otherwise 'Contact not found'.
    """


phonebook = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}

print(find_contact(phonebook, "Alice"))   # Expected output: 123-456-7890
print(find_contact(phonebook, "David"))   # Expected output: Contact not found

"""
To complete this exercise:
--------------------------
No any implementation notes. 


Exercise Breakdown:
-------------------
The `in` operator can be used to check if a specific key exists in the dictionary.
Alternatively, you can use the dict.get() method, which returns the value associated with the key if it exists, or a default value if it doesn't.
"""