def word_count(text):
    """
    This function takes a string and returns the number of words in the string.
    You should handle any periods (.), commas (,), and multiple spaces.
    """


print(word_count("The quick brown fox jumps over the lazy dog."))  # Expected output: 9
print(word_count("Hello, world!"))  # Expected output: 2
print(word_count("This sentence has  double   spaces."))  # Expected output: 5
print(word_count(" "))  # Expected output: 0
print(word_count("One, more, sentence, ,, here."))  # Expected output: 4


"""
To complete this exercise:
--------------------------
Use the `replace()`, `split()` and other string manipulation.
"""
