from collections import defaultdict

def build_graph(edges: list[list[int]]) -> dict[int, list[int]]:
    graph = defaultdict(list)

    for x, y in edges:
        graph[x].append(y)
        # graph[y].append(x)
        # Uncomment above line if graph undir.

    return graph