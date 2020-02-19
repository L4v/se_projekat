from result import Result
from sets import Set

def pretraga_upita(trie, graph, kriterijum, logical, not_word):
    if not_word == True:
        a = Set([Result(i, 0) for i in graph.vertices(as_path=True)])  # skup svih stranica
        b = Set(trie.find(kriterijum[0]))  #  b ce biti skup stranica koje sadrze tu rec
        return a - b

    if logical == 'and':
        return Set(trie.find(kriterijum[0])) * Set(trie.find(kriterijum[1]))
    elif logical == 'or':
        return Set(trie.find(kriterijum[0])) + Set(trie.find(kriterijum[1]))
    elif logical == 'not':
        return Set(trie.find(kriterijum[0])) - Set(trie.find(kriterijum[1]))
    else:  # obicna pretraga
        length = len(kriterijum)
        if length == 1:  # ako smo uneli samo jednu rec
            return Set(trie.find(kriterijum[0]))
        else:  # ako smo uneli 2 ili vise reci
            a = Set(trie.find(kriterijum[0])) + Set(trie.find(kriterijum[1]))
            if length == 2:  # ako smo uneli 2 reci vrati
                return a
            else:
                for i in range(2, length):
                    a = a + Set(trie.find(kriterijum[i]))
                return a
