class UnionFind:

    def __init__(self, n):
        self.father = {i: i for i in xrange(1, n+1)}

    def set(self, a, f):
        self.father[self.find(a)] = f

    def union(self, a, b):
        self.father[self.find(a)] = self.find(b)

    def find(self, node):
        path = []
        while self.father[node] != node:
            path.append(node)
            node = self.father[node]

        for n in path:
            self.father[n] = node

        return node


if __name__ == '__main__':
    uf = UnionFind(7)

    for i in xrange(1, 4):
        uf.set(i, 4)

    for i in xrange(5, 7):
        uf.set(i, 7)

    print uf.father

    uf.union(1, 5)
    print uf.father

    print uf.find(1)
    print uf.father



