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