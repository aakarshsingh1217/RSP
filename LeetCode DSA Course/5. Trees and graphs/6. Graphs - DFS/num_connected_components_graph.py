class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

        # Use rank arr. to record height of each vertex i.e. "rank",
        # init. rank of each vert. is 1 because they're initially
        # standalone vertices.
        self.rank = [1] * size

    # find func. is same as DSU with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        
        # Some ranks may becomes obsolete so they're not updated.
        self.root[x] = self.find(self.root[x])

        return self.root[x]
    
    # Union func. with union by rank.
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return 0
        else:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

            return 1
        
def countComponents(n: int, edges: list[list[int]]) -> int:
    uf = UnionFind(n)
    num_components = n

    for x, y in edges:
        num_components -= uf.union(x, y)

    return num_components