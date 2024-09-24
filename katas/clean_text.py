def clean_text(text):
    """
    Replaces common punctuation marks (',', '.', '!') in the text with spaces.
    """


text_content = "Hello, world! This is a test."

result = clean_text(text_content)
print(result)  # Expected output: 'Hello world this is a test'

text_content = "Python is fun! Let's code."

result = clean_text(text_content)
print(result)  # Expected output: 'Python is fun let s code'

text_content = "Wait... What?! Are you serious?"

result = clean_text(text_content)
print(result)  # Expected output: 'Wait what are you serious'

"""
To complete this exercise:
--------------------------
Implement the 'clean_text' function to:
- Replace commas, periods, and exclamation marks with '' (empty string).
- Make each word lower case, except the first word.

Exercise Breakdown:
-------------------
The `replace()` method allows you to replace specific characters or substrings within a string.
"""
