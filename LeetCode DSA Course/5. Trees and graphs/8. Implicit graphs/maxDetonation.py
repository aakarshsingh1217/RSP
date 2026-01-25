from collections import defaultdict

def maxDetonation(bombs: list[list[int]]) -> int:
    graph = defaultdict(list)
    n = len(bombs)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            xi, yi, ri = bombs[i]
            xj, yj, _ = bombs[j]

            # Create a path from node i to node j, if bomb i
            # detonates bomb j.
            if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                graph[i].append(j)

    # DFS to get num. nodes reachable from given node cur.
    def dfs(curr, visited):
        visited.add(curr)

        for neib in graph[curr]:
            if neib not in visited:
                dfs(neib, visited)

        return len(visited)
    
    ans = 0

    for i in range(n):
        visited = set()
        ans = max(ans, dfs(i, visited))

    return ans