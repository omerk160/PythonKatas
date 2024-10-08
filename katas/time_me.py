import time


def time_me(func):
    """
    Return the number of milliseconds it took to execute the func function.
    Since execution time may vary from time to time, execute func 10 times and return the average running time.
    """


time_took = time_me(lambda: time.sleep(2 + random()))
print(time_took)  # Prints the average time in milliseconds


"""
To complete this exercise:
--------------------------
Implement the 'time_me' function to measure the average execution time of a given function over 10 runs.


Exercise Breakdown:
-------------------
The `time` module provides various time-related functions.
`time.time()` returns the current time in seconds since the Epoch. 
By calculating the difference between the start and end times, you can measure how long a function takes to execute.
"""
