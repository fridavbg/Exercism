def is_armstrong_number(number):
    length = len(str(number))
    armstrong_number = 0
    for num in str(number):
        armstrong_number += int(num) ** length
    return armstrong_number == number

# print(is_armstrong_number(153))
# print(is_armstrong_number(190))
