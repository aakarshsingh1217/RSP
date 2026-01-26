from heapq import *

def halveArray(nums: list[int]) -> int:
    sum = 0
    
    for num in nums:
        sum += num

    nums = [-num for num in nums]
    heapify(nums)
    numOpers = 0

    currSum = sum

    while currSum > sum / 2:
        currElem = -1 * heappop(nums)
        currElem /= 2
        currSum -= currElem
        heappush(nums, -1 * currElem)
        numOpers += 1

    return numOpers

halveArray([5,19,8,1])