"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    letters = ["A", "B", "C", "D"]
    seats_letters = []

    for row in range(1, number + 1):
        seats_letters.append(letters[(row - 1) % 4])
        yield seats_letters[-1]
        
def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    row_number = 1

    for seat_index in range(number):
        seat_letter = chr(ord('A') + seat_index % 4)
        seat_with_row = f"{row_number}{seat_letter}"
        yield seat_with_row

        if (seat_index + 1) % 4 == 0 and seat_letter == 'D':
            row_number += 1
            if row_number == 13:
                row_number += 1


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seats = list(generate_seats(len(passengers)))
    assigned_seats = dict(zip(passengers, seats))
    return assigned_seats


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers: 
        seat_flight = f"{seat}{flight_id}"
        ticket_number = seat_flight.ljust(12, '0')

        yield ticket_number

