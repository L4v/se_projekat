from page import Page
from parser import Parser

class Graph: 
    def __init__(self):
        self._vertices = {}
        self._parser = Parser()

    """ NOTE(Jovan): Stranica se ocekuje kao uredjeni par (reci, linkovi)
        te se preradjuje u cvor i veze
    """
    def add_vertex(self, page):
        words, links = self._parser.parse(page)
        vertex = Page(words, links)
        if vertex is not in self._vertices:
            self._vertices[vertex] = {}
        for l in links:
            _add_edge(vertex, l)    


        
    """ NOTE(Jovan):
        Dodaje se veza izmedju dva cvora.
    """
    def _add_edge(self, vertex, link):
        if vertex in self._vertices:
            self._vertices[vertex].append(link)
        else:
            self._vertices[vertex] = [link]
        
    def vertices(self):
        return list(self._vertices.keys())

    def edges(self):
        return self._generate_edges()

    def _generate_edges(self):
        edges = []
        for vertex in self._vertices:
            for neighbour in self._vertices:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        ret = "vertices: "
        for n in self._vertices:
            ret += str(n) + " "
        ret += "\nedges: "
        for link in self._generate_edges():
            ret += str(link)
        return ret
        
