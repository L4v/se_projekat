def unos():
    a = input('Unesite za pretragu: ')

    tokens = a.split()

    for token in tokens:
        print(token)

    for token in tokens:
        if token == 'AND':
            logical= token
        if token == 'OR':
            logical = token
        if token == 'NOT':
            logical = token

