class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        
        return self.root[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                root_x, root_y = root_y, root_x

            # Modify the root of the smaller group as
            # root of the larger group, also increment
            # the size of the larger group.
            self.rank[root_y] += self.rank[root_x]
            self.root[root_x] = root_y

def validPath(n: int, edges: list[list[int]], source: int, dest: int):
    uf = UnionFind(n)

    for a, b in edges:
        uf.union(a, b)

    return uf.find(source) == uf.find(dest)

"""
DFS sol.

from collections import defaultdict

def validPath(n: int, edges: list[list[int]], source: int, dest: int) -> bool:
    graph = defaultdict(list)

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    seen = [False] * n

    def dfs(curr_node: int):
        if curr_node == dest:
            return True
        
        seen[curr_node] = True

        for next_node in graph[curr_node]:
            # Only call dfs if not seen.
            if not seen[next_node]:
                if dfs(next_node):
                    return True
                
        return False
    
    return dfs(source)
"""