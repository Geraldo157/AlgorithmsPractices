def longest(a1, a2):
    single_letters = []
    word = ''

    for i in a1:
        if i not in single_letters:
            single_letters.append(i)
    for j in a2:
        if j not in single_letters:
            single_letters.append(j)

    single_letters.sort()

    for w in single_letters:
        word += w

    return word
