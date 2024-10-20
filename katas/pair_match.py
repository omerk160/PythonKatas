def pair_match(men, women):
    """
    This function receives two dictionaries in the form:
    {
        "<name>": <age>
    }

    Where <name> is a string name, and <age> is an integer representing the age.
    The function returns a pair of names (tuple) of men and women names,
    where their absolute age differences is the minimal.
    """
    min_diff = float('inf')  # Initialize to a large number
    best_pair = None  # To store the best matching pair

    # Iterate through each man and each woman
    for man, man_age in men.items():
        for woman, woman_age in women.items():
            # Calculate the absolute age difference
            diff = abs(man_age - woman_age)

            # Update the best pair if a smaller difference is found
            if diff < min_diff:
                min_diff = diff
                best_pair = (man, woman)

    return best_pair



print(pair_match(
    {
        "John": 20,
        "Abraham": 45
    },
    {
        "July": 18,
        "Kim": 26
    }
))

# Expected ("John", "July"), since:

# abs(John - Kim) = abs(20 - 26) = abs(-6) = 6
# abs(John - July) = abs(20 - 18) = abs(2) = 2
# abs(Abraham - Kim) = abs(45 - 26) = abs(19) = 19
# abs(Abraham - July) = abs(45 - 18) = abs(27) = 27

