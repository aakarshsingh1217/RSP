MAXV = 1000
MAXINT = 100000

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

def prim(g: Graph, start: int):
    intree = [False] * (MAXV + 1)
    distance = [MAXINT] * (MAXV + 1)
    parent = [-1] * (MAXV + 1)

    distance[start] = 0
    curr_vert = start

    while not intree[curr_vert]:
        intree[curr_vert] = True
        curr_edge = g.edges[curr_vert]

        while curr_edge is not None:
            w = curr_edge.y
            weight = curr_edge.weight

            if not intree[w] and distance[w] > weight:
                distance[w] = weight
                parent[w] = curr_vert

            curr_edge = curr_edge.next

        # pick next closest non-tree vertex
        curr_vert = -1
        min_dist = MAXINT

        for i in range(1, g.nvertices + 1):
            if not intree[i] and distance[i] < min_dist:
                min_dist = distance[i]
                curr_vert = i

        if curr_vert == -1:  # no reachable vertex left
            break

    return parent, distance