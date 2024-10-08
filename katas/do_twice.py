def add(a, b):
    return a + b


def square(x):
    return x * x


def capitalize_full_name(firstname, lastname):
    return firstname[0].upper() + firstname[1:] + lastname[0].upper() + lastname[1:]


def do_twice(func, *args):
    """
    Applies the given function to the provided arguments and returns the result.
    """


# Example usage
print(do_twice(add, 3, 4))  # 7, 7 expected
print(do_twice(square, 5))  # 25, 25 expected
print(do_twice(capitalize_full_name, "john", 'doe'))  # 'John Doe', 'John Doe' expected


"""
To complete this exercise:
--------------------------
Implement the `do_twice` function to call the provided function `func` two times
with the arguments passed as `*args`.
The results of both calls should be returned as a tuple.


Exercise Breakdown:
-------------------
You can pass a function as an argument to another function:

def foo():
    pass
    
def boo(func_prt):
    func_prt()

boo(foo)  # in this example, foo is sent to boo as the func_prt, and boo call the function.


The *args syntax allows you to pass a variable number of arguments to a function.
Inside the function, `args` is treated as a tuple containing all arguments passed.
"""
