from collections import defaultdict

def findCircleNum(isConnected: list[list[int]]) -> int:
    def dfs(node: int):
        for neighbour in graph[node]:
            if neighbour not in seen:
                seen.add(neighbour)
                dfs(neighbour)

    n = len(isConnected)
    graph = defaultdict(list)

    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j]:
                graph[i].append(j)
                graph[j].append(i)

    seen = set()
    ans = 0

    for i in range(n):
        if i not in seen:
            ans += 1
            seen.add(i)
            dfs(i)

    return ans