# graph/vertex.py
class Vertex(object):

    __slots__ = ('_path', '_words', '_links', '_rank', '_backlinks')

    def __init__(self, path, words=None, links=None, links_to=None):
        self._path = path
        self._words = [] if words is None else words
        self._links = [] if links is None else links
        self._backlinks = []

    @property
    def path(self):
        return self._path

    @property
    def words(self):
        return self._words

    @property
    def links(self):
        return self._links

    @property
    def backlinks(self):
        return self._backlinks

    @backlinks.setter
    def backlinks(self, b):
        self._backlinks = b

    def __str__(self):
        return self._path

    def __eq__(self, other):
        return isinstance(other, Vertex) and other._path == self._path

    def __hash__(self):
        return hash(str(self))
