class UnionFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]

    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        
        self.root[x] = self.find(self.root[x])

        return self.root[x]
    

    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)