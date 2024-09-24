def start_end(text, n, m):
    if n < 0 or m < 0 or n > len(text) or m > len(text):
        return 'ERROR'

    start_part = text[:n]
    end_part = text[-m:]

    # Concatenate the two parts
    return start_part + end_part


text = 'Elvis has left the building'
result = start_end(text, 3, 5)
print(result)  # Expected output: 'Elvlding'

result = start_end(text, 7, 2)
print(result)  # Expected output: 'Elvis hng'

result = start_end(text, 5, 4)
print(result)  # Expected output: 'Elvisding'

result = start_end('Pythonista', 4, 3)
print(result)  # Expected output: 'Pythsta'

result = start_end(text, 25, 1)  # Invalid input (too large)
print(result)  # Expected output: ''

"""
To complete this exercise:
--------------------------
No any implementation notes. 
"""
