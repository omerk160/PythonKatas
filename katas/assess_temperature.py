def assess_temperature(temp):

    if temp >=30:
        return 'Hot'
    elif temp < 15:
        return 'Cold'
    #else if temp > 15 and temp < 30:
    else:
        return 'Moderate'

print(assess_temperature(35))  # 'Hot' expected
print(assess_temperature(10))  # 'Cold' expected
print(assess_temperature(20))  # 'Moderate' expected

"""
To complete this exercise:
--------------------------
Implement the 'assess_temperature' function to return 'Hot', 'Cold', or 'Moderate' 
based on the value of the input temperature using if, elif, and else statements.


Exercise Breakdown:
-------------------
In Python, the `if` statement is used to make decisions in your code. It allows you to execute certain 
code blocks only when specific conditions are met. 

Here's a quick overview:
- `if` checks a condition and executes the code block if the condition is true.
- `elif` (short for else if) checks another condition if the previous `if` or `elif` conditions were false.
- `else` executes a code block if none of the previous conditions were true.
"""
