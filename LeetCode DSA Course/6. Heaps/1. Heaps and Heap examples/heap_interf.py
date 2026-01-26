# heapq only implems. min heaps.
from heapq import *

# Decl.: heapq doesn't give you a heap DS, you just use a normal
# list, and heapq provides you with methods that can be used on
# this list to perform heap opers.
heap = []

# Add to heap
heappush(heap, 1)
heappush(heap, 2)
heappush(heap, 3)

# Check min. elem.
heap[0] # 1

# Pop min. elem.
heappop(heap) # 1

# Get size
len(heap) # 2

# Bonus: convert list to a heap in linear time
nums = [43, 2, 13, 634, 120]
heapify(nums) # 2 13 43 120 634