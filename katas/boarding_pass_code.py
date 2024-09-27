def generate_boarding_pass(passenger):
    """
    Generates a boarding pass code for the given passenger.
    """
    last_name = passenger['name'].split()[-1]  # Extract the last name
    flight_number = passenger['flight_number']
    departing = passenger['departing']
    arrival = passenger['arrival']
    boarding_time = passenger['boarding_time'].replace(':', '')  # Remove colon from boarding time
    seat = passenger['seat'].upper()  # Convert seat to uppercase

    # Create the formatted boarding pass code
    boarding_pass = f"{flight_number}//{last_name}//{departing}-{arrival}//{boarding_time}//{seat}"
    return boarding_pass


passenger_info = {
    'name': 'Jane Smith',
    'flight_number': 'CD456',
    'seat': '5b',
    'boarding_time': '15:45',
    'departing': 'LCA',
    'arrival': 'LAX'
}

result = generate_boarding_pass(passenger_info)
print(result)  # Expected output: CD456//Smith//LCA-LAX//1545//5B

"""
To complete this exercise:
--------------------------
Implement the 'generate_boarding_pass' function to create a formatted boarding pass code for a passenger, as follows:

[flight_number]//[last name only]//[departing]-[arrival]//[boarding_time digits only]//[seat upper case]


Exercise Breakdown:
-------------------
The`f` string formatting is used to embed expressions inside string literals, using curly braces `{}`. 
`f` strings are much more readable than using the '+' operator to concat strings: 

name = 'John'
greeting = f"Hello, {name}"

print(greeting) # Output: Hello, John
"""