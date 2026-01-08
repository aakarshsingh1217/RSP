def findSum(nums: list[int], k: int) -> int:
    curr = 0

    for i in range(k):
        curr += nums[i]

    largestSum = curr

    for i in range(k, len(nums)):
        curr += nums[i]
        curr -= nums[i - k]
        largestSum = max(largestSum, curr)

    return largestSum

arr = [1, 3, 2, 5, -7, 9, 2]
k = 3

print(f"Largest sum: {findSum(arr, k)}")