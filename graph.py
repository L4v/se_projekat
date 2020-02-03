class Graph: 
    def __init__(self, nodes=None):
        if nodes == None:
            nodes = {}
        self._nodes = nodes

    def add_node(self, node):
        if node not int self._nodes:
            self._nodes[node] = []

    def add_link(self, link):
        link = set(link)
        
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
    
