def disemvowel(string_):
    string = ''
    vowels = 'aeiouAEIOU'
    for i in string_:
        if i in vowels:
            pass
        else:
            string += i
    return string
