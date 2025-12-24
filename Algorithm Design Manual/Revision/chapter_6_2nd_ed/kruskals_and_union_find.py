SET_SIZE = 1000
MAXV = 1000

class SetUnion:
    def __init__(self):
        self.parent_elem = [None] * (SET_SIZE + 1)
        self.size = [None] * (SET_SIZE + 1)
        self.num_elems_in_set = 0

class EdgeNode:
    def __init__(self, y, weight = None, next = None):
        self.y = y
        self.weight = weight
        self.next = next

class Edge:
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight

class Graph:
    def __init__(self):
        self.edges = [None] * (MAXV + 1) # adj. lists
        self.degree = [0] * (MAXV + 1) # outdeg. of each vert
        self.nvertices = 0 # num vertices
        self.nedges = 0 # num edges
        self.directed = False

def set_union_init(s: SetUnion, n: int):
    for i in range(1, n + 1):
        s.parent_elem[i] = i
        s.size[i] = 1

    s.num_elems_in_set = n

def find(s: SetUnion, x: int):
    if (s.parent_elem[x] == x):
        return x
    else:
        return find(s, s.parent_elem[x])
    
def union_sets(s: SetUnion, s1: int, s2: int):
    r1 = find(s, s1)
    r2 = find(s, s2)

    if (r1 == r2): return

    if (s.size[r1] >= s.size[r2]):
        s.size[r1] = s.size[r1] + s.size[r2]
        s.parent_elem[r2] = r1
    else:
        s.size[r2] = s.size[r1] + s.size[r2]
        s.parent_elem[r1] = r2

def same_component(s: SetUnion, s1: int, s2: int):
    return (find(s, s1) == find(s, s2))

"""
Kruskal needs one extra step compared to Prim:
Convert the adjacency lists into a flat list of edges, then sort it.

For undirected graphs, each edge appears twice in adjacency lists,
so we only include (x, y) when x < y.
"""

def to_edge_list(g: Graph):
    edges = []

    for x in range(1, g.nvertices + 1):
        p = g.edges[x]

        while p is not None:
            y = p.y
            w = p.weight

            """
            In an undirected graph, when you insert an
            edge 1 -- 2, your adj. list stores both
            dirs.:
                1: 2
                2: 1
            
            So when you iter. through adj. lists, you'll
            see:
              - edge(1, 2)
              - edge(2, 1)
            
            But these're the same edge.
            Kruskal's must only consider it once.

            This condition checks if graph is dir., which
            means every edge is unique and keep all edges.

            If g.directed is false, now we only incl. edges
            when x < y so one dir. is kept.

            E.g. 1 -- 2 graph:
              1: 2
              2: 1
              When x = 1, y = 2
              1 < 2, keep (1,2)
              When x = 2, y = 1
              2 < 1, skip (2, 1)

            Therefore edge only appears once.
            """
            if g.directed or x < y: # Avoid duplicates
                edges.append(Edge(x, y, w))

            p = p.next

    return edges

def kruskal(g: Graph):
    # 1. Initialize union-find
    s = SetUnion()
    
    set_union_init(s, g.nvertices)

    # 2. Get and sort edges
    edges = to_edge_list(g)
    edges.sort(key=lambda e: e.weight)

    mst = [] # edges in MST
    total_weight = 0

    # 3. Process edges in increasing weight
    for e in edges:
        if not same_component(s, e.x, e.y):
            union_sets(s, e.x, e.y)
            mst.append((e.x, e.y, e.weight))
            total_weight += e.weight

            if len(mst) == g.nvertices - 1:
                break

    return mst, total_weight