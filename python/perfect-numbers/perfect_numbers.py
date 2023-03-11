def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number > 0:
        sum = 0
        for num in range(1, number):
            if (number % num) == 0:
                sum += num
        if sum == number:
            return 'perfect'
        if sum > number:
            return 'abundant'
        else: 
            return 'deficient'
    else: 
        raise ValueError("Classification is only possible for positive integers.")
