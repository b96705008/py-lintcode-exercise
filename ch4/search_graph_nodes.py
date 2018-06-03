# -*- coding: utf-8 -*-

"""
Given a undirected graph, a node and a target, 
return the nearest node to given node which value of it is target, 
return NULL if you can’t find.

There is a mapping store the nodes' values in the given parameters.

Note: It’s guaranteed there is only one available solution

Example

        2------3  5
         \     |  | 
          \    |  |
           \   |  |
            \  |  |
              1 --4
Give a node 1, target is 50 
there a hash named values which is [3,4,10,50,50], represent: 
Value of node 1 is 3 
Value of node 2 is 4 
Value of node 3 is 10 
Value of node 4 is 50 
Value of node 5 is 50

Return node 4
"""

from graph import Graph

def search_nodes(start_node, node_values, target):
	if start_node is None:
		return None

	queue = [start_node]
	visited = set([start_node])
	while len(queue) > 0:
		node = queue.pop(0)
		if node_values[node.label] == target:
			return node

		for nb in node.neighbors:
			if nb in visited:
				continue
			queue.append(nb)
			visited.add(nb)

	return None

values = [3,4,10,50,50]
print values
node_values = {i: v for i, v in zip(range(1,6), values)}
edges = [[1,2], [1,4], [1,3], [2,3], [4,5]]
g = Graph(node_values.keys(), edges)

node = search_nodes(g.start_node, node_values, 50)
print 50, node.label
node = search_nodes(g.start_node, node_values, 10)
print 10, node.label



values = [4,4,10,10,50]
print values
node_values = {i: v for i, v in zip(range(1,6), values)}

node = search_nodes(g.start_node, node_values, 10)
print 10, node.label
node = search_nodes(g.start_node, node_values, 4)
print 4, node.label






