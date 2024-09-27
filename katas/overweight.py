def check_overweight(people_weights, limit):
    """
    This function checks if any person in the given dictionary is overweight.
    Returns a list of names of people whose weight exceeds the specified limit.
    """
    overweight_people = [name for name, weight in people_weights.items() if weight > limit]
    return overweight_people


people = {
    "Alice": 68,
    "Bob": 85,
    "Charlie": 90,
    "Diana": 70
}

weight_limit = 75
result = check_overweight(people, weight_limit)  # Expected output: ['Bob', 'Charlie']
print(result)  # This should print ['Bob', 'Charlie']
