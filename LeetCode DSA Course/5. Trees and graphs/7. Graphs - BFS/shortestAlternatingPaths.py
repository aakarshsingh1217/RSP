from collections import defaultdict, deque

def shortestAlternatingPaths(n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
    RED = 0
    BLUE = 1

    graph = defaultdict(lambda: defaultdict(list))

    for x, y in redEdges:
        graph[RED][x].append(y)
    
    for x, y in blueEdges:
        graph[BLUE][x].append(y)

    ans = [float("inf")] * n
    queue = deque([(0, RED, 0), (0, BLUE, 0)])
    seen = {(0, RED), (0, BLUE)}

    while queue:
        node, colour, steps = queue.popleft()
        ans[node] = min(ans[node], steps)
        
        for neighbour in graph[colour][node]:
            if (neighbour, 1 - colour) not in seen:
                seen.add((neighbour, 1 - colour))
                queue.append((neighbour, 1 - colour, steps + 1))

    return [x if x != float("inf") else -1 for x in ans]