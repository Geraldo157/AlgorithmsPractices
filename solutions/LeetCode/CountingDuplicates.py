def duplicate_count(text):
    text = list(text.lower())
    pairs = {}
    pair = 0
    for i in text:
        if i not in pairs.keys():
            pairs[i] = 1
        else:
            pairs[i] += 1
    for i in pairs.values():
        if i > 1:
            pair += 1
    return pair
