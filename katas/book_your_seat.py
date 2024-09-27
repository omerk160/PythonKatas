def add_passenger(seats, seat_class, passenger_name):
    """
    Adds a passenger to the first available seat in the correct section.
    First 10 seats are for 'Business' Class.
    Next 10 seats are for 'First' Class.
    The remaining seats are for 'Economy' Class.
    """
    if seat_class == "Business":
        start_index = 0
        end_index = 10
    elif seat_class == "First":
        start_index = 10
        end_index = 20
    elif seat_class == "Economy":
        start_index = 20
        end_index = 100
    else:
        return  # Invalid seat class, do nothing

    # Find the first available seat in the specified section
    for i in range(start_index, end_index):
        if seats[i] is None:
            seats[i] = passenger_name  # Assign passenger name to the seat
            return  # Exit once the passenger is added

# Example usage
aircraft_seats = [None] * 100  # Creates a list of None of length 100

add_passenger(aircraft_seats, "Business", "Alice")
add_passenger(aircraft_seats, "Business", "Eve")
add_passenger(aircraft_seats, "First", "Bob")

print(aircraft_seats[:15])  # Expected output: ['Alice', 'Eve', None, None, None, None, None, None, None, None, 'Bob', None, None, None, None]
