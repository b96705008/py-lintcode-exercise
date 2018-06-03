"""
Find the number connected component in the undirected graph. 
Each node in the graph contains a label and a list of its neighbors. 
(a connected component (or just component) of an undirected graph is 
a subgraph in which any two vertices are connected to each other by paths, 
and which is connected to no additional vertices in the supergraph.)

Notice
Each connected component should sort by label.

Example
Given graph:

A------B  C
 \     |  | 
  \    |  |
   \   |  |
    \  |  |
      D   E
Return {A,B,D}, {C,E}. Since there are two connected component which is {A,B,D}, {C,E}
"""


from graph import Graph


def find_nodes_in_cc(node, visited):
    queue = [node]
    visited.add(node)
    cc = [node.label]

    while len(queue) > 0:
        cur_node = queue.pop(0)
        for neighbor in cur_node.neighbors:
            if neighbor in visited:
                continue
            queue.append(neighbor)
            visited.add(neighbor)
            cc.append(neighbor.label)

    return sorted(cc)


def connedtedSet(nodes):
    ccs = []
    if nodes is None or len(nodes) == 0:
        return ccs

    visited = set()
    for node in nodes:
        if node in visited:
            continue
        cc = find_nodes_in_cc(node, visited)
        ccs.append(cc)

    return ccs


if __name__ == '__main__':
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [['A','B'], ['A','D'], ['B','D'], ['C','E']]
    g = Graph(vertices, edges, True)
    ccs = connedtedSet(g.nodes)
    print 'ex1:'
    for cc in ccs:
        print cc

    print 'ex2:'
    vertices = ['A', 'B', 'C']
    edges = [['A','B'], ['A','C']]
    g = Graph(vertices, edges, True)
    ccs = connedtedSet(g.nodes)
    for cc in ccs:
        print cc

    print 'ex3:'
    vertices = ['A', 'B', 'C', 'D']
    edges = [['A','B'], ['D','C']]
    g = Graph(vertices, edges, True)
    ccs = connedtedSet(g.nodes)
    for cc in ccs:
        print cc

