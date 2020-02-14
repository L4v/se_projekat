from sets import Set

def pretraga_upita(trie, kriterijum, logical):
    if logical in ['and', 'AND']:
        return Set(trie.find(kriterijum[0])) * Set(trie.find(kriterijum[1]))
    elif logical in ['or', 'OR']:
        return Set(trie.find(kriterijum[0])) + Set(trie.find(kriterijum[1]))
    elif logical in ['not', 'NOT']:
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
                    rez = a + Set(trie.find(kriterijum[i]))
                return rez
