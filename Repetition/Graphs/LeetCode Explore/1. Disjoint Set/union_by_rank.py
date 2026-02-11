"""
- find(x) walks up parent pointers until it reaches root.
- union(x, y) does:
  - Two find calls.
  - One ptr. update.
- connected(x, y) does:
  - Two find calls.
- So everything hinges on how tall tree gets.
- A tree of rank r has at least 2^r nodes:
  - Rank r -> size >= 2^(r - 1)
    2^rank <= N
    rank <= log base 2 N.
  - Max tree height O(log N).
"""

class UnionFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x: int) -> int:
        while x != self.root[x]:
            x = self.root[x]

        return x
    
    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)