from collections import defaultdict

def build_graph(edges):
    graph = defaultdict(list)

    for edge in edges:
        graph[edge[0]].append(edge[1])
        # graph[y].append(x)
        # Uncomment above line if graph is undirected
        # Above syntax shows pythonic way of getting elems. out
        # of 2D array of lists, needs for x y in edges:

    return graph
