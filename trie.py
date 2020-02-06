class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def put(self, ch):
        self.children[ch] = TrieNode()

    def get(self, ch):
        return self.children[ch]

    def contains_key(self, ch):
        return ch in self.children

    def set_end(self):
        self.end = True

    def is_end(self):
        return self.end

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        current = self.root

        for ch in word:
            if not current.contains_key(ch):
                current.put(ch)
            current = current.get(ch)

        current.set_end() #kraj reci

    def find(self, word):
        current = self.root

        for ch in word:
            if not current.contains_key(ch):
                return False
            current = current.get(ch)

        return current.is_end()


