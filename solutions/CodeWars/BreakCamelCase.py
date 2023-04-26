def solution(s):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = list(s)
    palavra = ''
    for i, v in enumerate(s):
        if v in upper:
            palavra += ' '
        palavra += v
    return palavra
