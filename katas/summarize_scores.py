def summarize_scores(scores, threshold=50, include_average=True):
    """
    Summarizes the scores based on a given threshold (default is 50). Returns a list of scores
    above the threshold, and optionally includes the average score.

    """
    # Filter scores above the threshold
    above_threshold = [score for score in scores if score > threshold]

    # Calculate the average score
    average_score = sum(scores) / len(scores) if scores else 0

    # Return based on the value of include_average
    return (above_threshold, average_score) if include_average else above_threshold


# Test cases
print(summarize_scores([30, 60, 90, 20, 75]))  # Expected output: ([60, 90, 75], 54.0)
print(summarize_scores([10, 40, 55, 80], threshold=45))  # Expected output: ([55, 80], 48.75)
print(summarize_scores([15, 25, 35, 45], include_average=False))  # Expected output: []
print(summarize_scores([100, 95, 85, 70, 60], threshold=80,
                       include_average=True))  # Expected output: ([100, 95, 85], 82.0)
