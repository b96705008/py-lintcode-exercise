class GraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Graph:
    def __init__(self, vertices, edges, udirect=True):
        self.vertices = vertices
        self.edges = edges
        self.udirect = udirect
        self.create_graph()


    def create_graph(self):
        if self.vertices is None or len(self.vertices) == 0 or \
            self.edges is None or len(self.edges) == 0:
            return None

        nodes = {n: GraphNode(n) for n in self.vertices}

        ad_list = {n: set() for n in self.vertices}
        for e in self.edges:
            u = e[0]
            v = e[1]
            ad_list[u].add(v)
            if self.udirect:
                ad_list[v].add(u)

        for v in self.vertices:
            node = nodes[v]
            neighbors = ad_list[v]
            for neighbor in neighbors:
                neighbor_node = nodes[neighbor]
                node.neighbors.append(neighbor_node)

        self.nodes = [n for l, n in nodes.items()]
        self.start_node = nodes[self.vertices[0]]


    def traverse(self, start_label=None):
        start = self.start_node

        if start_label is not None:
            nodes = filter(lambda n: n.label==start_label, self.nodes)
            if len(nodes) > 0:
                start = nodes[0]
            else:
                start = None

        if start is None:
            print 'graph is empty.'
            return 

        queue = [start]
        visited = set([start])

        while len(queue) > 0:
            u = queue.pop(0)
            print u.label,
            for v in u.neighbors:
                if v in visited:
                    continue
                queue.append(v)
                visited.add(v) 
        print ''


if __name__ == '__main__':
    vertices = range(5)
    edges = [[0,1], [0,2], [1,2], [2, 3], [1,4]]
    g = Graph(vertices, edges)
    g.traverse_graph()
