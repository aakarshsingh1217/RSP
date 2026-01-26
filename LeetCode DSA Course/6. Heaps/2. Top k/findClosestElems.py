from heapq import *

def findClosestElems(arr: list[int], k: int, x: int) -> list[int]:
    heap = []

    for num in arr:
        distance = abs(x - num)
        heappush(heap, (-distance, -num))

        if len(heap) > k:
            heappop(heap)

    return sorted([-pair[1] for pair in heap])