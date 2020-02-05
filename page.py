class Page:
    def __init__(self, words=None, links=None):
       self._words = [] if words==None else words
       self._links = [] if links==None else links

    def add_link(self, link):
        if link not in self._links:
            self._links.append(link)
    
    def remove_link(self, link):
        if link in self._links:
            self._links.remove(link)

    def add_word(self, word):
        if word not in self._words:
            self._words.append(word)

    def remove_word(self, word):
        if word in self._words:
            self._words.remove(word)
    
    def get(self):
        return self._words, self._links
