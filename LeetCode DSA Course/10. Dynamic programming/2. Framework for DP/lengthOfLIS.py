def lengthOfLIS(nums: list[int]) -> int:
    def dp(i):
        if i in memo:
            return memo[i]
        
        ans = 1 # Base case: LIS ending at i atleast 1

        # Recurrence relation
        for j in range(i):
            if nums[i] > nums[j]:
                ans = max(ans, dp(j) + 1)

        memo[i] = ans

        return ans

    memo = {}

    return max(dp(i) for i in range(len(nums)))