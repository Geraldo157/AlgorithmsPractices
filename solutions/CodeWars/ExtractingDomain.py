def domain_name(url):
    word = ''
    if url[0:7] == 'http://':
        url = url[7:]
    if url[0:8] == 'https://':
        url = url[8:]
    if url[0:4] == 'www.':
        url = url[4:]
    for i in url:
        if i == '.':
            break
        word += i
    return word
