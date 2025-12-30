from collections import deque

"""
1 ---- 2 ---- 3
|
|
|
|
4

index 1: 4 -> 2 -> X
index 2: 3 -> 1 -> X
index 3: 2 -> X
index 4: 1 -> X
"""

MAXV = 1000

class EdgeNode:
    def __init__(self, y, weight = None, next = None):
        self.y = y
        self.weight = weight
        self.next = next

class Graph:
    def __init__(self):
        self.edges = [None] * (MAXV + 1) # adj. lists
        self.degree = [0] * (MAXV + 1) # outdeg. of each vert
        self.nvertices = 0 # num vertices
        self.nedges = 0 # num edges
        self.directed = False

def initialize_graph(g: Graph, directed: bool):
    g.nvertices = 0
    g.nedges = 0
    g.directed = directed

    for i in range(1, MAXV + 1):
        g.degree[i] = 0
        g.edges[i] = None

def insert_edge(g: Graph, x: int, y: int, directed: bool):
    p = EdgeNode(y = y, weight = None, next = g.edges[x])

    g.edges[x] = p
    g.degree[x] += 1

    if not directed:
        insert_edge(g, y, x, True)
    else:
        g.nedges += 1

def read_graph(g: Graph, directed: bool):
    initialize_graph(g, directed)
    
    nvertices, m = map(int, input().split())
    g.nvertices = nvertices

    for _ in range(m):
        x, y = map(int, input().split())
        insert_edge(g, x, y, directed)

def print_graph(g: Graph):
    for i in range(1, g.nvertices + 1):
        print(f"{i}: ", end="")
        
        p = g.edges[i]

        while p is not None:
            print(f" {p.y}", end="")
            p = p.next

        print()

def dfs(g: Graph, start: int, target: int):
    seen = set()

    def dfs_visit(node):
        if node == target:
            return True

        print(node)
        p = g.edges[node]

        while p is not None:
            neighbour = p.y

            if neighbour not in seen:
                seen.add(neighbour)
                dfs_visit(neighbour)
            
            p = p.next

    seen.add(start)
    dfs_visit(start)

    return False

def bfs(g: Graph, start: int):
    seen = set()
    queue = deque()

    seen.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()

        print(node)

        p = g.edges[node]

        while p is not None:
            neighbour = p.y

            if neighbour not in seen:
                seen.add(neighbour)
                queue.append(neighbour)
            
            p = p.next

def bfs_contains(g: Graph, start: int, target: int) -> bool:
    seen = set()
    queue = deque()

    seen.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()

        if node == target:
            return True
        
        p = g.edges[node]

        while p is not None:
            neighbour = p.y

            if neighbour not in seen:
                seen.add(neighbour)
                queue.append(neighbour)

            p = p.next

    return False

"""
**************************    
Example graph (undirected)
**************************

Edges:
1 - 2
1 - 3
2 - 4
3 - 5

Adj. lists (linked lists):
1: 3 -> 2
2: 4 -> 1
3: 5 -> 1
4: 2
5: 3

Start DFS at node 1.
dfs(g, start = 1)

seen = { 1 }
dfs_visit(1)

print(1)
Neighbours of 1: 3 -> 2

Go to neighbour 3:
seen = { 1, 3 }
dfs_visit(3)

print(3)
Neighbours of 3: 5 -> 1
1 already seen -> skip.
5 not seen -> dfs_visit(5)
seen = { 1, 3, 5 }

print(5)
Neighbours of 5: 3
3 already seen -> stop.
return to node 3

Backtrack to node 1
Next neighbour of 1 is 2.
seen = { 1, 2, 3, 5 }
dfs_visit(2)

print(2)
Neighbours of 2: 4 -> 1
1 seen -> skip
4 not seen -> dfs_visit(4)
seen = { 1, 2, 3, 4, 5 }

print(4)
Neigbhoours of 4: 2 already seen.

Return.
"""