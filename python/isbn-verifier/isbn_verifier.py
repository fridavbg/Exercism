def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    total = 0
    for multiplier, digit in enumerate(isbn[::-1], start=1):
        if digit == "X" and multiplier == 1:
            digit = 10
        elif not digit.isnumeric():
            return False
        total += int(digit) * multiplier
    return total % 11 == 0
