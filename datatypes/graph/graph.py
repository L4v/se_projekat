# graph/graph.py


class Graph:
    def __init__(self):
        self._vertices = {}

    """ NOTE(Jovan): Stranica se ocekuje kao uredjeni par (reci, linkovi)
        te se preradjuje u cvor i veze
    """
    def add_vertex(self, vertex):
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

    def gen_backlinks(self):
        for v1 in self._vertices:
            tmp = []
            for v2 in self._vertices:
                if v2 == v1:
                    continue
                if v1 in self._vertices[v2].links:
                    tmp.append(v2)
            tmp = list(dict.fromkeys(tmp))
            self._vertices[v1].backlinks = tmp

    def get_backlink(self, vertex):
        if vertex in self._vertices:
            return self._vertices[vertex].backlinks
        else:
            return []

    def get_vertex(self, path, as_path=False):
        if as_path:
            return self._vertices[path].path or None
        else:
            return self._vertices[path] or None

    def vertex_count(self):
        return len(self._vertices)

    def __str__(self):
        ret = ''
        for v in self._vertices:
            ret += v
            for l in v.links:
                ret += '\t->' + l
        return ret
