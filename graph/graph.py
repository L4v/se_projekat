# graph/graph.py
from sets import Set


class Graph:
    def __init__(self):
        self._vertices = {}

    """ NOTE(Jovan): Stranica se ocekuje kao uredjeni par (reci, linkovi)
        te se preradjuje u cvor i veze
    """
    def add_vertex(self, vertex):
        # TODO(Jovan): Nepotrebno?
        if vertex not in self._vertices:
            self._vertices[vertex.path] = vertex

    # NOTE(Jovan): as_path -> ako je true vraca samo putanja, inace
    # vraca objekat vertex
    def vertices(self, as_path=False):
        if as_path:
            return list(self._vertices.keys())
        return list(self._vertices.values())

    def edges(self):
        edges = {}
        for v in self._vertices:
            edges[v] = v.links
        return edges

    def get_backlink(self, vertex):
        ret = Set()
        if vertex not in self._vertices:
            return ret
        for v in self._vertices:
            if vertex in self._vertices[v]:
                ret.add(v)

    def get_vertex(self, path):
        return self._vertices.get(path, None)

    def vertex_count(self):
        return len(self._vertices)

    def __str__(self):
        ret = ''
        for v in self._vertices:
            ret += v
            for l in v.links:
                ret += '\t->' + l
        return ret
