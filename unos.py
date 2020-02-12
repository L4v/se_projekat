from pretraga import pretraga_upita
from sets import Set

def unos_upita(trie):
    a = input('Unesite reci za pretragu: ')

    if a == '':
        print('*** NEMA UNOSA! ***')
        return Set()

    tokens = a.split()

    kriterijum = []  # reci za pretragu
    logical = None  # logicki operator
    count_logical = 0  # samo jedan logicki operator moze biti unet

    # proveravamo da li je unet i logicki operator
    for token in tokens:
        if token in ['and', 'or', 'not', 'AND', 'OR', 'NOT']:
            if count_logical == 1:
                print('* Samo jedan logicki operator mozete uneti! *')
                return Set()
            else:
                logical = token
                count_logical = 1
        else:
            kriterijum.append(token)

    # provera unosa
    if count_logical == 1:
        if len(kriterijum) != 2 or logical is not tokens[1]:
            print('*** POGRESAN UNOS! ***')
            return Set()

    return pretraga_upita(trie, kriterijum, logical)