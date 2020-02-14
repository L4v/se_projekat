from pretraga import pretraga_upita

def unos_upita(trie):

    while True:
        a = input('Unesite reci za pretragu: ')

        if a == '':
            print('*** NEMA UNOSA! ***')
            continue

        tokens = a.split()

        kriterijum = []  # reci za pretragu
        logical = None  # logicki operator
        count_logical = 0  # samo jedan logicki operator moze biti unet

        # proveravamo da li je unet i logicki operator
        for token in tokens:
            if token in ['and', 'or', 'not', 'AND', 'OR', 'NOT']:
                if count_logical == 1:
                    print('* Samo jedan logicki operator mozete uneti! *')
                    continue
                else:
                    logical = token
                    count_logical = 1
            else:
                kriterijum.append(token)

        if logical is tokens[0] and logical in ['not', 'NOT'] and len(kriterijum) == 1:
            print("Not unos") # zavrsiti

        # provera unosa
        if count_logical == 1:
            if len(kriterijum) != 2 or logical is not tokens[1]:
                print('*** POGRESAN UNOS! ***')
                continue



        return pretraga_upita(trie, kriterijum, logical)