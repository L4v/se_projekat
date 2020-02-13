class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.pages = {}

    def add_page(self, page):  # dodaj za svaki cvor stranice
        if page not in self.pages:
            self.pages[page] = 1
        else:
            self.pages[page] += 1

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

    def add(self, word, page):
        current = self.root

        for ch in word:
            if not current.contains_key(ch):
                current.put(ch)

            current = current.get(ch)

        current.add_page(page)
        current.set_end()  # kraj reci

    def find(self, word):
        current = self.root

        for ch in word:
            if not current.contains_key(ch):
                return {}
            current = current.get(ch)

        return {} if not current.is_end() else current.pages


