def DNA_strand(dna):
    newDna = ''
    for i in dna:
        if i == 'A':
            newDna += 'T'
        elif i == 'T':
            newDna += 'A'
        elif i == 'C':
            newDna += 'G'
        elif i == 'G':
            newDna += 'C'

    return newDna
