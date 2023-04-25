def quadrant(x, y):
    retorno = 0
    if x > 0 and y > 0:
        retorno += 1
    elif x < 0 and y > 0:
        retorno += 2
    elif x > 0 and y < 0:
        retorno += 4
    elif x < 0 and y < 0:
        retorno += 3
    return retorno
