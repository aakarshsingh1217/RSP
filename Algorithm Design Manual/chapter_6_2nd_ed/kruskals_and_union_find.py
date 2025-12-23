SET_SIZE = 1000 # arbitrary choice

class Edge:
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w

class Graph:
    def __init__(self, n):
        self.n_vertices = n
        self.edges = []

    def add_edge(self, x, y, w):
        self.edges.append(Edge(x, y, w))

class SetUnion:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        r1 = self.find(x)
        r2 = self.find(y)

        if r1 == r2:
            return

        if (self.size[r1] >= self.size[r2]):
            self.parent[r2] = r1
            self.size[r1] += self.size[r2]
        else:
            self.parent[r1] = r2
            self.size[r2] += self.size[r1]

    def same_component(self, x, y):
        return (self.find(x) == self.find(y))

def kruskal(graph):
    uf = SetUnion(graph.n_vertices)

    # Sort edges by weight
    edges = sorted(graph.edges, key=lambda e: e.w)

    mst = []

    for e in edges:
        if not uf.same_component(e.x, e.y):
            mst.append(e)
            uf.union(e.x, e.y)

        if len(mst) == graph.n_vertices - 1:
            break

    return mst