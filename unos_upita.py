def unos(trie, graph):
    a = input('Unesite za pretragu: ')

    tokens = a.split()

    for token in tokens:
        print(token)

    kriterijum = [] #reci koje smo uneli na osnovu kojih vrsimo pretragu
    logical = None #logicki operator
    pages = [] #stranice u kojima se nalaze reci

    for token in tokens:
        if token in ['AND', 'OR', 'NOT']:
            logical = token
        else:
            kriterijum.append(token)

    def and_pretraga(kriterijum):
        for page in graph.vertices():
            for word in page.words:
                if word == kriterijum[0]:
                    i1 = 1
                elif word == kriterijum[1]:
                    i2 = 1
            if i1 == 1 and i2 == 1:
                print(page.path)
            i1 = 0
            i2 = 0

    def or_pretraga(kriterijum):
        for page in graph.vertices():
            for word in page.words:
                if word == kriterijum[0]:
                    i1 = 1
                elif word == kriterijum[1]:
                    i2 = 1
            if i1 == 1 or i2 == 1:
                print(page.path)
            i1 = 0
            i2 = 0

    def  not_pretraga(kriterijum):
        for page in graph.vertices():
            for word in page.words:
                if word == kriterijum[0]:
                    i1 = 1
                elif word != kriterijum[1]:
                    i2 = 1
            if i1 == 1 and i2 == 1:
                print(page.path)
            i1 = 0
            i2 = 0

    def obicna_pretraga(kriterijum):
        for rec in kriterijum:
            if trie.find(rec):
                return print('Postoji!')
            else:
                return print('Ne postoji!', rec)

    if logical == 'AND':
        and_pretraga(kriterijum)
    elif logical == 'OR':
        or_pretraga(kriterijum)
    elif logical == 'NOT':
        not_pretraga(kriterijum)
    elif logical == None:
        obicna_pretraga(kriterijum)



