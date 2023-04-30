def solution(arr):
    # Não terminada
    letras = {}
    retorno = True
    for i, v in enumerate(arr):
        if i[0] not in letras.values():
            letras[i[0]] = 1
        else:
            letras[i[0]] += 1
        if i[-1] not in letras.values():
            letras[i[-1]] = 1
        else:
            letras[i[-1]] += 1
    for i in letras.values():
        if i % 2 == 1:
            retorno = False
    return retorno
