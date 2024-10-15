def hello_world():
    return "hello world"


if __name__ == '__main__':
    result_str = hello_world()
    print(result_str)   # hello world should be printed


"""
To complete this exercise:
--------------------------
Modify the 'hello_world' function to return the string "hello world".


Exercise Breakdown:
-------------------
A function is a reusable block of code that performs a specific task.
Functions allow us to organize our code and make it more readable and manageable.

In Python, a function is defined using the 'def' keyword, followed by the function name and parentheses ().
Inside the parentheses, we can specify parameters that the function can accept.
The code block within every function starts with a colon (:) and is indented.

Here is an example of how to define and call a function:

Example:
--------
def example_function():
    return "This is an example"

result = example_function()
print(result)  # This will output: This is an example
"""