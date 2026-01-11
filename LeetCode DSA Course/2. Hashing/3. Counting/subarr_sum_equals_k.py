from collections import defaultdict

def subarraySum(self, nums: list[int], k: int) -> int:
    sum_count = defaultdict(int)
    sum_count[0] = 1
    curr = ans = 0

    for num in nums:
        curr += num
        ans += sum_count[curr - k]
        sum_count[curr] += 1

    return ans