from math import ceil

def minEatingSpeed(piles: list[int], h: int):
    def check(k):
        hours = 0

        for bananas in piles:
            hours += ceil(bananas / k)

        return hours <= h
    
    left = 1
    right = max(piles)

    while left <= right:
        mid = (left + right) // 2

        if check(mid):
            right = mid - 1
        else:
            left = mid + 1