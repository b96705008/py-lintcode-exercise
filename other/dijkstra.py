
from collections import defaultdict
import heapq
import sys


def shortest_path(edges, start, end):
    # create adjacent list
    graph = defaultdict(list)
    for u, v, cost in edges:
        graph[u].append((v, cost))

    min_path = {start: 0}
    visited = set()
    q = [(0, start, [])]

    while q:
        prev_cost, node, path = heapq.heappop(q)
        visited.add(node)
        path = path + [node]
        if node == end:
            return prev_cost, path

        for neighbor, edge_cost in graph[node]:
            if neighbor in visited:
                continue

            new_cost = prev_cost + edge_cost
            if neighbor not in min_path or new_cost < min_path[neighbor]:
                min_path[neighbor] = new_cost
                decrease_key_or_insert(q, neighbor, new_cost, path)

    return None


def decrease_key_or_insert(heap, node, cost, path):
    for i, n in enumerate(heap):
        _, v, _ = n
        if v == node:
            heap[i] = (cost, v, path)
            heapq._siftdown(heap, 0, i)
            return

    heapq.heappush(heap, (cost, node, path))


if __name__ == '__main__':
    edges = [
        ("A", "B", 2),
        ("A", "C", 5),
        ("B", "C", 6),
        ("B", "D", 1),
        ("B", "E", 3),
        ("D", "E", 4),
        ("C", "F", 8),
        ("E", "G", 9),
        ("F", "G", 7)
    ]

    print "=== Dijkstra ==="
    print edges
    print "A -> G:"
    print shortest_path(edges, "A", "G")




                


