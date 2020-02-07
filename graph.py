from page import Page
from parser import Parser


class Graph:
    def __init__(self):
        self._vertices = {}

    """ NOTE(Jovan): Stranica se ocekuje kao uredjeni par (reci, linkovi)
        te se preradjuje u cvor i veze
    """
    # TODO(jovan): Kao uredjeni par ili odmah kao stranica?
    def add_vertex(self, page):
        vertex = page 
        if vertex not in self._vertices:
            self._vertices[vertex] = []

    """ NOTE(Jovan):
        Dodaje se veza izmedju dva cvora.
    """
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self._vertices:
            self._vertices[vertex1].append(vertex2)
        else:
            self._vertices[vertex1] = [vertex2]

    def vertices(self):
        return list(self._vertices.keys())

    def edges(self):
        edges = []
        for edge in self._vertices.values():
            edges.append(edge)
        return edges

    def get_vertex(self, path):
        for v in self._vertices:
            if v.path == path:
                return v
        return None

    def vertex_count(self):
        return len(self._vertices)

    def _generate_edges(self):
        edges = []
        for vertex in self._vertices:
            for neighbour in self._vertices:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        ret = ''
        for vertex in self._vertices:
            ret += '\n' + vertex.path + ':\n'
            for edge in self._vertices[vertex]:
                print(edge)
                ret += '\t' + '->' + edge.path + '\n'
        return ret
