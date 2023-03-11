from tracemalloc import stop


def steps(number):
    steps = 0
    if number > 0 and isinstance(number, int):
        while number > 1:
            if number % 2 == 0:
                number /= 2
            elif number % 2 != 0:
                number = (3 * number) + 1
            steps += 1
        return steps
    else:
        raise ValueError("Only positive integers are allowed")

print(steps(12))