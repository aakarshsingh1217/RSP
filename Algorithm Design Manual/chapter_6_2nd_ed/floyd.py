MAX_VERTICES = 1000
MAX_INT = 100000

class AdjacencyMatrix:
    def __init__(self):
        # adjacency/weight info
        self.weight = [[MAX_INT for _ in range(MAX_VERTICES)] for _ in range(MAX_VERTICES)]
        # number of vertices in graph
        self.n_vertices = 0