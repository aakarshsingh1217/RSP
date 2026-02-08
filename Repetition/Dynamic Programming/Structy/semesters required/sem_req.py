from collections import defaultdict

def sem_req(num_courses: int, prereqs: list[list[int]]):
    graph = defaultdict(list)
    distance = defaultdict(int)

    for a, b in prereqs:
        graph[a].append(b)

    for course in graph:
        if len(graph[course]) == 0:
            distance[course] = 1

    for course in graph:
        dp(course)

    def dp(node: int):
        if node in distance:
            return distance[node]
        
        max_dist = 0
        
        for neighbour in graph[node]:
            max_dist = max(
                max_dist,
                dp(neighbour)
            )

        distance[node] = 1 + max_dist

        return distance[node]
    
    return max(distance.values())