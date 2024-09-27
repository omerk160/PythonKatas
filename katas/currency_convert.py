def convert_currency(amount, from_currency, to_currency, exchange_rates):
    """
    Converts an amount from one currency to another using the provided exchange rates.
    """


# Example exchange rates (amounts are in terms of 1 base currency unit)
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
    "JPY": 110.0
}

# Convert 100 USD to EUR
amount = 100
from_currency = "USD"
to_currency = "EUR"

converted = convert_currency(amount, from_currency, to_currency, exchange_rates)
print(converted)  # Expected output: 100 USD is equal to 85.00 EUR

"""
To complete this exercise:
--------------------------
No any implementation notes. 


Exercise Breakdown:
-------------------
A dictionary in Python is an unordered collection that stores items in key-value pairs.
Each key is unique and is used to retrieve its corresponding value.

To create a dictionary, you use curly braces {} with keys and values separated by colons.
For example:

exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85
}
 
To retrieve a value from a dictionary, you can use the key inside square brackets. 
For instance:

exchange_rates["USD"]
 
Returns 1.0
"""
