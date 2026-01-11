from collections import defaultdict

def numOfSubarrays(nums: list[int], k: int):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in nums:
        curr += num % 2
        ans += counts[curr - k]
        counts[curr] += 1