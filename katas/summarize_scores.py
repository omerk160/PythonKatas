def summarize_scores(...):
    """
    Summarizes the scores based on a given threshold (default is 50). Returns a list of scores
    above the threshold, and optionally includes the average score.
    """
    above_threshold = [score for score in scores if score > threshold]
    average_score = sum(scores) / len(scores) if scores else 0

    return (above_threshold, average_score) if include_average else above_threshold


print(summarize_scores([30, 60, 90, 20, 75]))  # Expected output: ([60, 90, 75], 54.0)
print(summarize_scores([10, 40, 55, 80], threshold=45))   # Expected output: ([55, 80], 48.75)
print(summarize_scores([15, 25, 35, 45], include_average=False))  # Expected output: []
print(summarize_scores([100, 95, 85, 70, 60], threshold=80, include_average=True))   # Expected output: ([100, 95, 85], 82.0)


"""
To complete this exercise:
--------------------------
According to the above function calls, write the function *declaration*. 


Exercise Breakdown:
-------------------
In Python, you can have multiple types of arguments. E.g:

- Positional arguments
- Arguments with default values
"""
