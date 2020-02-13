# TODO(Jovan): Dodati listu stranica koje pokazuju na stranicu
class Page(object):

    __slots__ = ('path', 'words', 'links', '_rank')

    # TODO(Jovan): Make fields private?
    def __init__(self, path, words=None, links=None, links_to=None):
        self.path = path
        self.words = [] if words is None else words
        self.links = [] if links is None else links
        self._rank = 0

    def set_rank(self, rank):
        self._rank = 0 if rank <= 0 else rank

    def __str__(self):
        return self.path

    def __eq__(self, other):
        return isinstance(other, Page) and other.path == self.path

    def __hash__(self):
        return hash(str(self))
