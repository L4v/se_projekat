def unos():
    a = input('Unesite za pretragu: ')

    tokens = a.split()

    for token in tokens:
        print(token)

    kriterijum = []

    for token in tokens:
        if token in ['AND', 'OR', 'NOT']:
            logical = token
        else:
            kriterijum.append(token)

