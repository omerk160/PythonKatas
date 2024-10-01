import time


def time_me(func):
    """
    Given func - a pointer to some function which can be executed by func()
    Return the number of milliseconds it took to execute the function. Since execution time may vary from time to time,
    execute func 10 times and return the average running time.

    :param func: Callable function to measure.
    :return: Average execution time in milliseconds.
    """
    total_time = 0
    for _ in range(10):
        start_time = time.time()  # Start time in seconds
        func()                     # Execute the function
        end_time = time.time()     # End time in seconds
        total_time += (end_time - start_time) * 1000  # Convert to milliseconds
    return total_time / 10  # Return average time


if __name__ == '__main__':
    time_took = time_me(lambda: time.sleep(2 + random()))
    print(time_took)  # Prints the average time in milliseconds


"""
To complete this exercise:
--------------------------
Implement the 'time_me' function to measure the average execution time of a given function over 10 runs.


Exercise Breakdown:
-------------------
The `time` module provides various time-related functions. `time.time()` returns the current time in seconds since the Epoch. 
By calculating the difference between the start and end times, you can measure how long a function takes to execute.
"""
