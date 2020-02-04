
class Graph: 
    def __init__(self, nodes=None):
        if nodes == None:
            nodes = {}
        self._nodes = nodes

    def add_node(self, node):
        if node not in self._nodes:
            self._nodes[node] = []

    def add_link(self, link):
        # NOTE(Jovan): Linkovi se dodaju u vidu skupa
        link = set(link)
        """ NOTE(Jovan):
            Formira se uredjeni par i dodaje se u graf,
            ako vec postoji, na postojeci cvor dodaje se link na drugi,
            inace pravi se cvor sa novim linkom
        """
        (node1, node2) = tuple(link)
        if node1 in self._nodes:
            self._nodes[node1].append(node2)
        else:
            self._nodes[node1] = [node2]
        
    def nodes(self):
        return list(self._nodes.keys())

    def links(self):
        return self._generate_edges()

    def _generate_links(self):
        links = []
        for node in self._nodes:
            for neighbour in self._nodes:
                if {neighbour, node} not in links:
                    links.append({node, neighbour})
        return links

    def __str__(self):
        ret = "nodes: "
        for n in self._nodes:
            ret += str(n) + " "
        res += "\nlinks: "
        for link in self._generate_links():
            ret += str(link)
        return ret
        
