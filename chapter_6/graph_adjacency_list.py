from enum import Enum

# represent edges using array of linked lists

MAX_VERTICES = 1000

class Color(Enum):
    UNCOLORED = 0
    WHITE = 1
    BLACK = 2

# vertex processed after we;ve traversed all outgoing edges
processed  = [False] * (MAX_VERTICES + 1)
# vertex discovered first time we visit it
discovered = [False] * (MAX_VERTICES + 1)
parent = [None] * (MAX_VERTICES + 1)
color = [Color.UNCOLORED] * (MAX_VERTICES + 1)
entry_time = [0] * (MAX_VERTICES + 1)
exit_time = [0] * (MAX_VERTICES + 1)
time = 0

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if (not self.items):
            return None
        
        val = self.items[0]
        del self.items[0]

        return val
    
    def empty_queue(self):
        if (not self.items):
            return True
        
        return False

class EdgeNode:
    def __init__(self, y, weight = None, next_edge = None):
        # adjacency info
        self.y = y
        # edge weight, if any
        self.weight = weight
        # next edge in list
        self.next_edge_node = next_edge

class Graph:
    def __init__(self):
        # adjacency info
        self.edges = [None] * (MAX_VERTICES + 1)
        # outdegree of each vertex
        self.degree = [0] * (MAX_VERTICES + 1)
        # number of vertices in graph
        self.n_vertices = 0
        # number of edges in graph 
        self.n_edges = 0
        # is the graph directed?
        self.is_directed = False

def initialize_graph(graph, is_directed):
    graph.n_vertices = 0
    graph.n_edges = 0
    graph.is_directed = is_directed

    for i in range(1, MAX_VERTICES + 1):
        graph.degree[i] = 0
        graph.edges[i] = None

def read_graph(graph, is_directed):
    initialize_graph(graph, is_directed)
    
    graph.n_vertices = int(input("Enter the num vertices in graph: "))
    num_edges = int(input("Enter the number of edges in the graph: "))

    for i in range(1, num_edges + 1):
        x = int(input("Enter x vertex in edge: "))
        y = int(input("Enter y vertex in edge: "))
        insert_edge(graph, x, y, is_directed)

def insert_edge(graph, x, y, is_directed):
    new_edge_node = EdgeNode(y)
    new_edge_node.next_edge_node = graph.edges[x]

    graph.edges[x] = new_edge_node
    graph.degree[x] += 1

    if (is_directed):
        graph.n_edges += 1
    else:
        insert_edge(graph, y, x, True)

def print_graph(graph):
    for i in range(1, graph.n_vertices + 1):
        print(f"{i}: ", end="")

        curr_edge = graph.edges[i]

        while (curr_edge is not None):
            print(f" {curr_edge.y}", end="")
            curr_edge = curr_edge.next_edge_node

        print()

def initialize_search(graph):
    for i in range(1, graph.n_vertices + 1):
        processed[i] = discovered[i] = False

# x = the current vertex you are expanding
# y = a neighbor of x, reached by following one edge
# edge (x, y) literally means:
# There is an edge from vertex x to vertex y.
"""
Conceptual meaning:
x ───▶ y
- x is the vertex currently being explored
- y is one of its adjacent vertices
- (x, y) is an edge in the graph

Skiena uses:
    x = source of the edge
    y = destination of the edge
"""
def bfs(graph, start):
    queue = Queue()
    queue.enqueue(start)
    discovered[start] = True

    while (not queue.empty_queue()):
        vertex = queue.dequeue()
        process_vertex_early(vertex)
        processed[vertex] = True
        # Here: vertex → x
        # curr_edge.y → y
        # So process_edge(vertex, y)
        # is process_edge(x, y)
        curr_edge = graph.edges[vertex]

        while (curr_edge is not None):
            y = curr_edge.y

            if (processed[y] == False or graph.is_directed):
                process_edge(vertex, y)

            if (discovered[y] == False):
                queue.enqueue(y)
                discovered[y] = True
                parent[y] = vertex
            
            curr_edge = curr_edge.next_edge_node

        process_vertex_late(vertex)


def process_vertex_early(vertex):
    print(f" {vertex}", end="")

def process_edge(x, y):
    if (color[x] == color[y]):
        bipartite = False
        print(f"Warning: not bipartite due to ({x}, {y})")

    color[y] = complement(color[x])

def process_vertex_late(x):
    pass
    # print("Nothing happening right now...")

def find_path(start, end, parents):
    if (start == end or end == -1):
        print(f"\n{start}")
    else:
        find_path(start, parents[end], parents)
        print(f" {end}", end="")

def connected_components(graph):
    component_num = 0
    initialize_search(graph)

    for i in range(1, graph.n_vertices + 1):
        if (discovered[i] is False):
            component_num += 1
            print(f"Component: {component_num} -> ", end="")
            bfs(graph, i)
            print()

def two_color(graph):
    bipartite = True

    initialize_search(graph)

    for i in range(1, graph.n_vertices + 1):
        if (discovered[i] is False):
            color[i] = Color.WHITE
            bfs(graph, i)

def complement(color):
    if (color == Color.WHITE): return Color.BLACK
    if (color == Color.BLACK): return Color.WHITE

    return Color.UNCOLORED

def dfs(graph, vertex):
    global time

    discovered[vertex] = True
    time += 1
    entry_time[vertex] = time

    process_vertex_early(vertex)

    edge_node = graph.edges[vertex]

    while (edge_node is not None):
        y = edge_node.y

        if (not discovered[y]):
            parent[y] = vertex
            process_edge(vertex, y)
            dfs(graph, y)
        elif ((not processed[y]) or graph.is_directed):
            process_edge(vertex, y)

        edge_node = edge_node.next_edge_node

    process_vertex_late(vertex)
    time += 1
    exit_time[vertex] = time
    processed[vertex] = True

def main():
    g = Graph()
    initialize_graph(g, is_directed=False)

    # Build graph with two components
    g.n_vertices = 6

    # Component 1
    insert_edge(g, 1, 2, g.is_directed)
    insert_edge(g, 2, 3, g.is_directed)

    # Component 2
    insert_edge(g, 4, 5, g.is_directed)

    # Vertex 6 is isolated

    print("=== Graph adjacency lists ===")
    print_graph(g)

    print("\n=== Connected components ===")
    connected_components(g)

if __name__ == "__main__":
    main()