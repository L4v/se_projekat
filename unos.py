from pretraga import pretraga_upita
from result import Result
from sets import Set


def unos_upita(trie, graph):

    while True:
        a = input('Unesite reci za pretragu: ')

        if a == '':
            print('*** NEMA UNOSA! ***')
            continue

        a = a.lower()
        tokens = a.split()

        kriterijum = []  # reci za pretragu
        logical = None  # logicki operator
        count_logical = 0  # samo jedan logicki operator moze biti unet
        not_word = 0  # ako je unos tipa 'not word'

        # proveravamo da li je unet i logicki operator
        for token in tokens:
            if token in ['and', 'or', 'not']:
                if count_logical == 1:
                    print('* Samo jedan logicki operator mozete uneti! *')
                    continue
                else:
                    logical = token
                    count_logical = 1  # povecavamo
            else:
                kriterijum.append(token)

        if logical is tokens[0] and logical in ['not', 'NOT'] and len(kriterijum) == 1:
            print("Not unos")

            a = Set([Result(i, 0) for i in graph.vertices(as_path=True)])
            #  trie.find vraca Result tip moramo pretvoriti u path
            #  b ce biti skup stranica koje sadrze tu rec
            b = Set([x.get_path() for x in trie.find(kriterijum[0])])

            return a - b
        # ukoliko imamo unos tipa 'not word'
        if logical == tokens[0] and logical == 'not' and len(kriterijum) == 1:
            not_word = 1
            return pretraga_upita(trie, graph, kriterijum, logical, not_word)

        # provera unosa
        if count_logical == 1:
            if len(kriterijum) != 2 or logical != tokens[1]:
                print('*** POGRESAN UNOS! ***')
                continue

        return pretraga_upita(trie, graph, kriterijum, logical, not_word)
