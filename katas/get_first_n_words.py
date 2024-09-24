def get_first_n_words(text, n=5):
    # Split the text into a list of words
    words = text.split()

    # Get the first 'n' words by slicing
    first_n_words = words[:n]

    # Join the words back into a single string with spaces
    return ' '.join(first_n_words)


# Testing the function
text_content = "The quick brown fox jumps over the lazy dog."

result = get_first_n_words(text_content, 3)
print(result)  # Expected output: 'The quick brown'

result = get_first_n_words(text_content)
print(result)  # Expected output: 'The quick brown fox jumps'

result = get_first_n_words(text_content, 0)
print(result)  # Expected output: '' (empty string)

result = get_first_n_words(text_content, 8)
print(result)  # Expected output: 'The quick brown fox jumps over the lazy'
