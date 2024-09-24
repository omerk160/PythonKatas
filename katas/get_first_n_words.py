def get_first_n_words(text, n=5):
    """
    Splits the text into words and returns the first 'n' words as a single string.
    """


text_content = "The quick brown fox jumps over the lazy dog."

result = get_first_n_words(text_content, 3)
print(result)  # Expected output: 'The quick brown'

result = get_first_n_words(text_content)
print(result)  # Expected output: 'The quick brown fox jumps'

result = get_first_n_words(text_content, 0)
print(result)  # Expected output: '' (empty string)

result = get_first_n_words(text_content, 8)
print(result)  # Expected output: 'The quick brown fox jumps over the lazy'

"""
To complete this exercise:
--------------------------
Implement the 'get_first_n_words' function to:

- Split the input text into list of words using `split()`,
- Use slicing to retrieve the first 'n' words,
- Join the words back into a single string with spaces in between.

Exercise Breakdown:
-------------------
The `split()` method divides a string into a list of words based on a specified separator (a space by default).
The `join()` method takes a list of words and combines them into a single string with a specified separator.
"""
