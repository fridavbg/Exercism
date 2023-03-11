def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    count = 0
    for letter_a, letter_b in zip(strand_a, strand_b):
        if letter_a != letter_b:
            count += 1
    return count

print(distance('GAGCCTACTAACGGGATAA', 'CATCGTAATGACGGCCTAC'))
