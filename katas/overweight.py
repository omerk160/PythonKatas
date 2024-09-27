def check_overweight(people_weights, limit):
    """
    This function checks if any person in the given dictionary is overweight.
    """


people = {
    "Alice": 68,
    "Bob": 85,
    "Charlie": 90,
    "Diana": 70
}

weight_limit = 75
result = check_overweight(people, weight_limit)  # Expected output: ['Bob', 'Charlie']


"""
To complete this exercise:
--------------------------
Go through a dictionary of people's weights and return a list of people whose weight exceeds a specified limit. 


Exercise Breakdown:
-------------------
The built-in `items()` method in Python returns view (you can see it as a "list") of key-value tuple pairs.
It's useful when you want to loop through each key and value consecutively. 
"""
