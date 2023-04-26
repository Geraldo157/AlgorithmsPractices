def descending_order(num):
    num2 = list(str(num))
    num2.sort()
    num2.reverse()
    retorno = ''
    for i in num2:
        retorno += i
    return int(retorno)
