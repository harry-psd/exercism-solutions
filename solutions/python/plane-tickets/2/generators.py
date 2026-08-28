"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    seat_letters = ['A','B','C','D']
    for seat in range(number):
        yield seat_letters[seat % 4]
    
    

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """
    seat_letters = ['A','B','C','D']
    for current_seat in range(number):
        seat_row = (current_seat // 4) + 1
        if seat_row >= 13:
            seat_row += 1
        yield str(seat_row) + seat_letters[current_seat % 4]


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """
    passengers_seats = {}
    all_seat_numbers = generate_seats(len(passengers))
    for passenger in passengers:
        passengers_seats[passenger] = next(all_seat_numbers)
    return passengers_seats


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """
    for seat_number in seat_numbers:
        trailing_zeros = '0' * (12 - len(seat_number) - len(flight_id))
        yield seat_number + flight_id + trailing_zeros