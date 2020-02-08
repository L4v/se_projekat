# TODO(Jovan): Dodati listu stranica koje pokazuju na stranicu
class Page(object):

    __slots__ = ('path', 'words', 'links', 'links_to')

    def __init__(self, path, words=None, links=None, links_to=None):
        self.path = path
        self.words = [] if words is None else words
        self.links = [] if links is None else links
        self.links_to = [] if links_to is None else links_to

    def __str__(self):
        return self.path

