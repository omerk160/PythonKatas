def get_alternate_words(sentence):
    """
    Returns every second word from the given sentence.
    """


sentence_1 = "The quick brown fox jumps over the lazy dog"
print(get_alternate_words(sentence_1))  # ["quick", "fox", "over", "lazy"] expected

sentence_2 = "Every second word in this sentence will be returned"
print(get_alternate_words(sentence_2))  # ["second", "in", "sentence", "be"] expected

sentence_3 = "Learning Python is fun and rewarding"
print(get_alternate_words(sentence_3))  # ["Python", "fun", "rewarding"] expected

"""
To complete this exercise:
--------------------------
Implement the 'get_alternate_words' function to return every second word from the given sentence. 


Exercise Breakdown:
-------------
List slicing allows you to extract a portion of a list by specifying a start, stop, and step (jump) value. 
- Syntax: list[start:stop:step]
- 'start' is the index where the slice starts.
- 'stop' is the index where the slice ends (not included in the slice).
- 'step' is the interval between each index in the slice. If 'step' is omitted, it defaults to 1.
"""
