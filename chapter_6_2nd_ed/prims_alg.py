MAX_VERTICES = 1000
MAX_INT = 10**9


class EdgeNode:
    def __init__(self, y, weight, next_edge=None):
        self.y = y                  # adjacent vertex
        self.weight = weight        # edge weight
        self.next_edge = next_edge  # next edge in adjacency list


class Graph:
    def __init__(self):
        self.edges = [None] * (MAX_VERTICES + 1)
        self.n_vertices = 0
        self.is_directed = False


def insert_edge(graph, x, y, weight, directed=False):
    graph.edges[x] = EdgeNode(y, weight, graph.edges[x])

    if not directed:
        graph.edges[y] = EdgeNode(x, weight, graph.edges[y])


def prim(graph, start):
    """
    Prim's Algorithm — Minimum Spanning Tree (MST)

    This function builds a Minimum Spanning Tree (MST) for a connected,
    undirected, weighted graph using Prim's algorithm.

    The algorithm grows a tree one vertex at a time, always choosing
    the cheapest edge that connects a vertex already in the tree
    to a vertex not yet in the tree.

    ------------------------------------------------------------
    DATA STRUCTURES USED
    ------------------------------------------------------------

    intree[v]:
        True if vertex v has already been added to the MST.
        False otherwise.

    distance[v]:
        The minimum weight of any edge that can connect v
        to the current MST.
        (This is NOT a path distance — just the cheapest edge.)

    parent[v]:
        The vertex in the MST that v is connected to by its
        cheapest edge.

    ------------------------------------------------------------
    EXAMPLE GRAPH (4 vertices)
    ------------------------------------------------------------

    Edges:
        1-2 (1)
        1-3 (4)
        1-4 (3)
        2-4 (2)
        3-4 (5)

    Start vertex: 1

    ------------------------------------------------------------
    INITIAL STATE
    ------------------------------------------------------------

    intree   = [False, False, False, False, False]
    distance = [inf, 0, inf, inf, inf]
    parent   = [-1, -1, -1, -1, -1]

    v = 1

    ------------------------------------------------------------
    ITERATION 1: v = 1
    ------------------------------------------------------------

    Mark 1 as in the tree:
        intree[1] = True

    Relax edges from 1:
        edge (1,2) weight 1 → distance[2] = 1, parent[2] = 1
        edge (1,3) weight 4 → distance[3] = 4, parent[3] = 1
        edge (1,4) weight 3 → distance[4] = 3, parent[4] = 1

    Arrays now:
        intree   = [F, T, F, F, F]
        distance = [inf, 0, 1, 4, 3]
        parent   = [-1, -1, 1, 1, 1]

    Next vertex chosen: 2 (smallest distance = 1)

    ------------------------------------------------------------
    ITERATION 2: v = 2
    ------------------------------------------------------------

    Mark 2 as in the tree:
        intree[2] = True

    Relax edges from 2:
        edge (2,4) weight 2 < current distance[4] (3)
        → distance[4] = 2, parent[4] = 2

    Arrays now:
        intree   = [F, T, T, F, F]
        distance = [inf, 0, 1, 4, 2]
        parent   = [-1, -1, 1, 1, 2]

    Next vertex chosen: 4 (smallest distance = 2)

    ------------------------------------------------------------
    ITERATION 3: v = 4
    ------------------------------------------------------------

    Mark 4 as in the tree:
        intree[4] = True

    Relax edges from 4:
        edge (4,3) weight 5 > current distance[3] (4)
        → no update

    Arrays now:
        intree   = [F, T, T, F, T]
        distance = [inf, 0, 1, 4, 2]
        parent   = [-1, -1, 1, 1, 2]

    Next vertex chosen: 3

    ------------------------------------------------------------
    ITERATION 4: v = 3
    ------------------------------------------------------------

    Mark 3 as in the tree:
        intree[3] = True

    No useful edges to relax.

    All vertices now in MST → algorithm stops.

    ------------------------------------------------------------
    FINAL MST
    ------------------------------------------------------------

    Edges selected (via parent array):

        1 - 2 (weight 1)
        2 - 4 (weight 2)
        1 - 3 (weight 4)

    Total MST weight = 7

    ------------------------------------------------------------
    RETURN VALUES
    ------------------------------------------------------------

    parent[v]:
        Defines the MST structure.
        For each v (except start), parent[v] is the vertex
        it connects to in the MST.

    distance[v]:
        Weight of the edge (parent[v], v).

    Time Complexity:
        O(V^2) for this implementation (array-based selection).
        Can be improved to O((V + E) log V) using a priority queue.
    """
    intree = [False] * (MAX_VERTICES + 1)
    distance = [MAX_INT] * (MAX_VERTICES + 1)
    parent = [-1] * (MAX_VERTICES + 1)

    distance[start] = 0
    v = start

    while not intree[v]:
        intree[v] = True
        curr_edge = graph.edges[v]

        # Relax edges from v
        while curr_edge is not None:
            neighbor = curr_edge.y
            weight = curr_edge.weight

            if not intree[neighbor] and weight < distance[neighbor]:
                distance[neighbor] = weight
                parent[neighbor] = v

            curr_edge = curr_edge.next_edge

        # Select next vertex with minimum distance
        v = -1
        best_dist = MAX_INT

        for i in range(1, graph.n_vertices + 1):
            if not intree[i] and distance[i] < best_dist:
                best_dist = distance[i]
                v = i

        if v == -1:  # graph fully processed
            break

    return parent, distance

def main():
    g = Graph()
    g.n_vertices = 4

    insert_edge(g, 1, 2, 1)
    insert_edge(g, 1, 3, 4)
    insert_edge(g, 1, 4, 3)
    insert_edge(g, 2, 4, 2)
    insert_edge(g, 3, 4, 5)

    parent, distance = prim(g, start=1)

    print("Minimum Spanning Tree edges:")
    for i in range(1, g.n_vertices + 1):
        if parent[i] != -1:
            print(f"{parent[i]} - {i} (weight {distance[i]})")

if __name__ == "__main__":
    main()