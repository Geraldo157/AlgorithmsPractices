def array_diff(a, b):
    array = []
    for i, v in enumerate(a):
        if v not in b:
            array.append(v)
    return array
