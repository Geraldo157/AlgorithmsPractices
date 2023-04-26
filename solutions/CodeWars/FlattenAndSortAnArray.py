def flatten_and_sort(array):
    arrays = []
    for x in array:
        for i in x:
            arrays.append(i)
    arrays.sort()
    return arrays
