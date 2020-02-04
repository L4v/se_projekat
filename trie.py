class Trie:

    def __init__(self):
        self.root = {}

    def add(self, word):
        current = self.root

        for ch in word:
            if ch not in current:
                current[ch] = {}
            current = current[ch]
        current['*'] = True

    def find(self, word):
        current = self.root

        for ch in word:
            if ch not in current:
                return False
            current = current[ch]

        if '*' in current:
            return True
        else:
            return False

