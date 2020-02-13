from sets import Set

def pretraga_upita(trie, kriterijum, logical):
    if logical in ['and', 'AND']:
        return Set(trie.find(kriterijum[0])) * Set(trie.find(kriterijum[1]))
    elif logical in ['or', 'OR']:
        return Set(trie.find(kriterijum[0])) + Set(trie.find(kriterijum[1]))
    elif logical in ['not', 'NOT']:
        return Set(trie.find(kriterijum[0])) - Set(trie.find(kriterijum[1]))
    else:
        length = len(kriterijum)
        if length == 1:
            return Set(trie.find(kriterijum[0]))
        else:
            a = Set(trie.find(kriterijum[0])) + Set(trie.find(kriterijum[1]))
            if length == 2:
                return a
            else:
                for i in range(2, length):
                    rez = Set(a + trie.find(kriterijum[i]))
                return rez
