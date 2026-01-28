from heapq import *

def findMaximizedCapital(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    projects = sorted(zip(capital, profits))
    n = len(projects)
    i = 0
    heap = []

    for _ in range(k):
        # Given money w, it finds all projects we can
        # currently afford, and puts their profit onto
        # max heap.
        while i < n and projects[i][0] <= w:
            heappush(heap, -projects[i][1])
            i += 1

        if len(heap) == 0:
            return w
        
        # Take most profitable projects each time, then
        # before taking next project in next iter. update
        # projects we can afford by using while loop.
        w += -heappop(heap)

    return w