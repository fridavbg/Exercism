def sum_of_multiples(limit, multiples):
    multiples_set = set()
    for number in multiples:
        if number == 0:
            continue
        num = number
        while (num < limit):
            multiples_set.add(num)
            num += number
    return sum(multiples_set)
    
print(sum_of_multiples(10, [3, 5]))