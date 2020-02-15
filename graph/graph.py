# graph/graph.py
class Graph:
    def __init__(self):
        self._vertices = {}

    """ NOTE(Jovan): Stranica se ocekuje kao uredjeni par (reci, linkovi)
        te se preradjuje u cvor i veze
    """
    def add_vertex(self, vertex):
        if vertex not in self._vertices:
            self._vertices[vertex.get_path()] = vertex

    def vertices(self):
        return list(self._vertices.values())

    def edges(self):
        edges = {}
        for v in self._vertices:
            edges[v] = v.get_links()
        return edges

    def get_vertex(self, path):
        return self._vertices.get(path, None)

    def vertex_count(self):
        return len(self._vertices)

    def __str__(self):
        ret = ''
        for v in self._vertices:
            ret += v
            for l in v.get_links():
                ret += '\t->' + l
        return ret
