def rob(nums: list[int]) -> int:
    n = len(nums)
    memo = {}

    def dp(i: int) -> int:
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        
        if i in memo:
            return memo[i]

        memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])

        return memo[i]

    return dp(n - 1)

def robBottomUp(nums: list[int]) -> int:
    n = len(nums)
    dp = [0] * n

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        robPrevHouse = dp[i - 1]
        robCurrHouse = dp[i - 2] + nums[i]

        dp[i] = max(robPrevHouse, robCurrHouse)

    return dp[n - 1]

def robBottomUpBetterSpace(nums: list[int]) -> int:
    if len(nums) == 1:
        return  nums[0]
    
    n = len(nums)

    back_two = nums[0]
    back_one = max(nums[0], nums[1])

    for i in range(2, n):
        back_one, back_two = max(back_one, back_two + nums[i]),
        back_one

    return back_one