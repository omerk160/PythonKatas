def verbing(word):
    """
    Given a string `word`, if its length is at least 3, append 'ing' in the end,
    unless it already ends with 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged.

    e.g.
    teach -> teaching
    do -> do
    swimming -> swimmingly
    """


print(verbing('walk'))      # Expected output: teaching
print(verbing('swimming'))  # Expected output: swimmingly
print(verbing('do'))        # Expected output: do


"""
To complete this exercise:
--------------------------
No any implementation notes. 


Exercise Breakdown:
-------------------
The `endswith()` method to determine if the word ends with 'ing'.
"""