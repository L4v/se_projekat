from set_functions import and_items, or_items, not_items

def pretraga_upita(trie, kriterijum, logical):
    if logical in ['and', 'AND']:
        return and_items(trie.find(kriterijum[0]), trie.find(kriterijum[1]))
    elif logical in ['or', 'OR']:
        return or_items(trie.find(kriterijum[0]), trie.find(kriterijum[1]))
    elif logical in ['not', 'NOT']:
        return not_items(trie.find(kriterijum[0]), trie.find(kriterijum[1]))
    else:
        length = len(kriterijum)
        if length == 1:
            return trie.find(kriterijum[0])
        else:
            a = or_items(trie.find(kriterijum[0]), trie.find(kriterijum[1]))
            if length == 2:
                return a
            else:
                for i in range(2, length):
                    rez = or_items(a, trie.find(kriterijum[i]))
                return rez