MAX_VERTICES = 1000
MAXINT = 10**9

parent = [-1] * (MAX_VERTICES + 1)

class EdgeNode:
    def __init__(self, y, weight, next_edge=None):
        self.y = y
        self.weight = weight
        self.next_edge = next_edge

class Graph:
    def __init__(self):
        self.edges = [None] * (MAX_VERTICES + 1)
        self.n_vertices = 0
        self.is_directed = False

def insert_edge(graph, x, y, weight, directed=False):
    graph.edges[x] = EdgeNode(y, weight, graph.edges[x])
    if not directed:
        graph.edges[y] = EdgeNode(x, weight, graph.edges[y])

def dijkstra(graph, start):
    intree = [False] * (MAX_VERTICES + 1)
    distance = [MAXINT] * (MAX_VERTICES + 1)

    for i in range(1, graph.n_vertices + 1):
        parent[i] = -1

    distance[start] = 0
    v = start

    while not intree[v]:
        intree[v] = True
        p = graph.edges[v]

        # Relax all outgoing edges of v
        while p is not None:
            w = p.y
            weight = p.weight

            if distance[w] > distance[v] + weight:
                distance[w] = distance[v] + weight
                parent[w] = v

            p = p.next_edge

        # Select next vertex with smallest tentative distance
        dist = MAXINT
        next_v = -1
        for i in range(1, graph.n_vertices + 1):
            if not intree[i] and distance[i] < dist:
                dist = distance[i]
                next_v = i

        if next_v == -1:
            break

        v = next_v

    return distance, parent