from datatypes.result import Result
from datatypes.sets import Set


def pretraga_upita(trie, graph, kriterijum, logical, not_word):
    if not_word == True:
        a = Set([Result(i, 0) for i in graph.vertices(as_path=True)])  # skup svih stranica
        b = Set(trie.find(kriterijum[0]))  #  b ce biti skup stranica koje sadrze tu rec
        return a - b

    if logical == 'and':
        a = Set(trie.find(kriterijum[0]))
        b = Set(trie.find(kriterijum[1]))

        tmp = a * b
        for i in tmp:  # treba da saberemo br reci
            tmp[tmp.index(i)] += b[b.index(i)]

        return tmp
    elif logical == 'or':
        a = Set(trie.find(kriterijum[0]))
        b = Set(trie.find(kriterijum[1]))

        tmp = a + b
        for i in tmp:  # treba da saberemo br reci
            if i in a and i in b:
                tmp[tmp.index(i)] += b[b.index(i)]

        return tmp
    elif logical == 'not':
        return Set(trie.find(kriterijum[0])) - Set(trie.find(kriterijum[1]))
    else:  # obicna pretraga
        length = len(kriterijum)
        if length == 1:  # ako smo uneli samo jednu rec -> kraj
            return Set(trie.find(kriterijum[0]))
        else:  # ako smo uneli 2 ili vise reci
            a = Set(trie.find(kriterijum[0]))
            b = Set(trie.find(kriterijum[1]))

            tmp = a + b
            for i in tmp:
                if i in a and i in b:
                    tmp[tmp.index(i)] += b[b.index(i)]

            if length == 2:  # ako smo uneli 2 reci -> kraj
                return tmp
            else:  # ako smo uneli 3 ili vise reci
                for i in range(2, length):
                    a = Set(trie.find(kriterijum[i]))
                    tmp = tmp + a
                    for i1 in tmp:
                        if i1 in a:
                            tmp[tmp.index(i1)] += a[a.index(i1)]

                return tmp
