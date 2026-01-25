from collections import defaultdict

def calcEq(equations, values, queries) -> list[float]:
    def answer_query(start, end):
        if start not in graph:
            return -1
        
        seen = {start}
        stack = [{start, 1}]

        while stack:
            node, ratio = stack.pop()

            if node == end:
                return ratio
            
            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    stack.append((neighbour, ratio * graph[node][neighbour]))

        return -1

    """
    In this prob., edges weighted, so each edge assoc. with value, therefore
    we'll map labels to another hashmap which'll map neighbours to their vals.
    """
    graph = defaultdict(dict)

    for i in range(len(equations)):
        numerator, denominator = equations[i]
        val = values[i]
        graph[numerator][denominator] = val
        graph[denominator][numerator] = 1 / val

    ans = []

    for numerator, denominator in queries:
        ans.append(answer_query(numerator, denominator))

    return ans