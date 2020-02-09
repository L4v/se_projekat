from set_functions import and_items
from set_functions import or_items
from set_functions import not_items

def unos(trie, graph):
    a = input('Unesite za pretragu: ')

    tokens = a.split()

    for token in tokens:
        print(token)

    kriterijum = [] #reci koje smo uneli na osnovu kojih vrsimo pretragu
    logical = None #logicki operator
    pages = [] #stranice u kojima se nalaze reci
    count_logical = 0 #samo jedan logicki operator moze biti unet
    count_reci = 0

    # proveravamo da li je unet i logicki operator

    for token in tokens:
        if token in ['AND', 'OR', 'NOT']:
            if count_logical == 1:
                print('Pogresan unos (samo jedan logicki operator mozete uneti!)')
                return
            else:
                logical = token
                count_logical = 1
        else:
            kriterijum.append(token)

    def and_pretraga(kriterijum):
        return print(and_items(trie.search(kriterijum[0]), trie.search(kriterijum[1])))

    def or_pretraga(kriterijum):
        return print(or_items(trie.search(kriterijum[0]), trie.search(kriterijum[1])))

    def  not_pretraga(kriterijum):
        return print(not_items(trie.search(kriterijum[0]), trie.search(kriterijum[1])))

    def obicna_pretraga(kriterijum):
        for rec in kriterijum:
            print(trie.search(rec))


    if logical == 'AND':
        and_pretraga(kriterijum)
    elif logical == 'OR':
        or_pretraga(kriterijum)
    elif logical == 'NOT':
        not_pretraga(kriterijum)
    elif logical == None:
        obicna_pretraga(kriterijum)



