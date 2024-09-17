def grade_check(score):
    """
    Determines the grade based on the score.
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Test cases
result = grade_check(85)
print(result)  # Expected output: B

result = grade_check(92)
print(result)  # Expected output: A

result = grade_check(67)
print(result)  # Expected output: D

result = grade_check(55)
print(result)  # Expected output: F
