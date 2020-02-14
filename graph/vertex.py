# NOTE(Jovan): Predstava web stranice
class Vertex(object):

    __slots__ = ('_path', '_words', '_links', '_rank')

    # TODO(Jovan): Make fields private?
    def __init__(self, path, words=None, links=None, links_to=None):
        self._path = path
        self._words = [] if words is None else words
        self._links = [] if links is None else links
        self._rank = 0

    def get_path(self):
        return self._path

    def get_words(self):
        return self._words

    def get_links(self):
        return self._links

    def set_rank(self, rank):
        self._rank = 0 if rank <= 0 else rank

    def __str__(self):
        return self._path

    def __eq__(self, other):
        return isinstance(other, Vertex) and other._path == self._path

    def __hash__(self):
        return hash(str(self))
