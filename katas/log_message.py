def log_message(message, log_type):
    """
    Logs a message to the console with a specific log type (e.g., 'INFO', 'WARNING', 'ERROR').
    """
    if log_type == "INFO":
        print(f"[INFO]: {message}")

    # TODO complete the rest...


log_message("System started", "INFO")   # Expected output: [INFO]: System started

log_message("Low disk space", "WARNING")   # Expected output: [WARNING]: Low disk space

log_message("Unable to connect to server", "ERROR")   # Expected output: [ERROR]: Unable to connect to server

result = log_message("", "UNKNOWN LOG TYPE")
print(result)  # Expected output: None


"""
To complete this exercise:
--------------------------
Implement the 'log_message' function to PRINT the message with the appropriate log type prefix as described above.


Exercise Breakdown:
-------------------
Functions might print messages, without returning a value.

Make sure you understand the above sentence. 

The `print` function outputs information to the console but does not return a value.

When a function uses `print`, it only prints the information,
the `return` statement, on the other hand, sends a value back to the caller of the function.

If a function does not explicitly return a value using `return`, it implicitly returns the `None` object.

Example:

def greet(name):
    print(f"Hello, {name}")   # This will print: Hello, Alice

x = greet("Alice")
print(x)   # None expected

You should carefully be aware if your function should PRINT a value re RETURN a value. 
"""
