def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:
    def dfs(node: int):
        path.append(node)

        if node == len(graph) - 1:
            paths.append(path[:])

            return
        
        for nei in graph[node]:
            dfs(nei)
            path.pop()

    paths = []
    path = []

    if not graph or len(graph) == 0:
        return paths
    
    dfs(0)

    return paths