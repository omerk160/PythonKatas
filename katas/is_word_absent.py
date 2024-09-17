def is_word_absent(text, word):
    """
    Checks if a given word is not present in the provided text.
    """


text_content = "The quick brown fox jumps over the lazy dog."

result = is_word_absent(text_content, "fox")
print(result)  # Expected output: The word 'fox' is found in the text.

result = is_word_absent(text_content, "cat")
print(result)  # Expected output: The word 'cat' is not found in the text.

result = is_word_absent(text_content, "dog")
print(result)  # Expected output: The word 'dog' is found in the text.

result = is_word_absent(text_content, "elephant")
print(result)  # Expected output: The word 'elephant' is not found in the text.

"""
To complete this exercise:
--------------------------
Implement the 'is_word_absent' function to check if a specific word is not present in a given text. 


Exercise Breakdown:
-------------------
The `not in` operator can also be used with strings to check if a substring is not present within another string. 
"""
