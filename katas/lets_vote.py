def lets_vote(votes, candidate):
    """
    Updates the vote counts in the votes dictionary based on the candidate who received a single vote.
    """


candidate_state = {'Alice': 0, 'Bob': 0}

lets_vote(candidate_state, 'Alice')
print(candidate_state)  # {'Alice': 1, 'Bob': 0} expected

lets_vote(candidate_state, 'Alice')
print(candidate_state)  # {'Alice': 2, 'Bob': 0} expected

lets_vote(candidate_state, 'Charlie')
print(candidate_state)  # {'Alice': 2, 'Bob': 0, 'Charlie': 1} expected


"""
To complete this exercise:
--------------------------
Update the vote counts in the `votes` dictionary based on the incoming candidate.
You should add a new key to the dictionary if it's the first time the candidate receives a vote.  


Exercise Breakdown:
-------------
To check if a key exists in a dictionary, you can use the `in` keyword. 

Using a dictionary as a counter is an efficient way to keep track of occurrences of items.
"""
