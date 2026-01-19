from collections import defaultdict

def minReorder(n: int, connections: list[list[int]]) -> int:
    roads = set()
    graph = defaultdict(list)

    for x, y in connections:
        graph[x].append(y)
        graph[y].append(x)
        roads.add((x, y))

    def dfs(node: int):
        ans = 0

        for neighbour in graph[node]:
            if neighbour not in seen:
                if (node, neighbour) in roads:
                    ans += 1
                    
                seen.add(neighbour)
                ans += dfs(neighbour)

        return ans

    seen = {0}
    
    return dfs(0)