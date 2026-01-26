from heapq import *

def lastStoneWeight(stones: list[int]) -> int:
    stones = [-stone for stone in stones]
    heapify(stones) # turns arr. into heap linear time.

    while len(stones) > 1:
        first = abs(heappop(stones))
        second = abs(heappop(stones))

        if first != second:
            heappush(stones, -abs(first - second))

    return -stones[0] if stones else 0