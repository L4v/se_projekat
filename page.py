class Page:
    def __init__(self, path, words=None, links=None):
       self.path = path
       self.words = [] if words==None else words
       self.links = [] if links==None else links

