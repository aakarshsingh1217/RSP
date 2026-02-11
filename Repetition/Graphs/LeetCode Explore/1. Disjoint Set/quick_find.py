"""
O(n) space compl. to store root arr. size n.
"""
class UnionFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]

    """
    O(1) time compl., as lookup arr. directly.
    """
    def find(self, x: int) -> int:
        return self.root[x]
    
    """
    O(n) due to for loop that goes through arr.
    """
    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    """
    O(1)
    """
    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
uf = UnionFind(10)
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
uf.union(9, 4)
print(uf.connected(4, 9))  # true