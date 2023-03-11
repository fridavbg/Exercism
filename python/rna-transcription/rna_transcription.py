def to_rna(dna_strand):
    dna_list = list(dna_strand)

    for letter in range(len(dna_strand)):

        if(dna_list[letter] == 'G'):
            dna_list[letter] = 'C'

        elif(dna_list[letter] == 'C'):
            dna_list[letter] = 'G'

        elif (dna_list[letter] == 'T'):
            dna_list[letter] = 'A'

        elif (dna_list[letter] == 'A'):
            dna_list[letter] = 'U'
    return ''.join(dna_list)
