from collections import defaultdict
from heapq import *

def topKFreq(nums: list[int], k: int) -> list[int]:
    hashmap = defaultdict(input)

    for num in nums:
        hashmap[num] += 1

    heap = []

    for key, val in hashmap.items():
        heappush(heap, (val, key))

        if len(heap) > k:
            heappop(heap)

    return [pair[1] for pair in heap]

"""
My sol:

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashMap = defaultdict(int)

        for elem in nums:
            hashMap[elem] += 1

        heap = [(-v, k) for k, v in hashMap.items()]
        heapify(heap)
        ans = []
        i = 0

        while len(heap) > 0 and i < k:
            ans.append(heappop(heap)[1])
            i += 1

        return ans
"""