def square_of_sum(number):
    sum = 0
    for num in range(1, number + 1):
        sum += num
    return sum ** 2


def sum_of_squares(number):
    sum = 0
    for num in range(1, number + 1):
        sum += num ** 2
    return sum

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
