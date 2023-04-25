def quarter_of(month):
    quarters = {
        1: [1, 2, 3],
        2: [4, 5, 6],
        3: [7, 8, 9],
        4: [10, 11, 12]
    }
    for i in quarters:
        if month in quarters.get(i):
            return i
