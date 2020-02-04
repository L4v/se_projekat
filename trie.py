class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

    def set_end(self):
        self.end = True

    def is_end(self):
        return self.end

class Trie:

    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def get_index(self, ch):
        return ord(ch) - ord('a')

    def add(self, word):
        current = self.root
        length = len(word)

        for i in range(length):
            index = self.get_index(word[i])

            if not current.children[index]:
                current.children[index] = self.get_node()
            current = current.children[index]

        current.end = True

    def find(self, word):
        current = self.root
        length = len(word)
        for i in range(length):
            index = self.get_index(word[i])
            if not current.children[index]:
                return False
            current = current.children[index]

        return current != None and current.end
