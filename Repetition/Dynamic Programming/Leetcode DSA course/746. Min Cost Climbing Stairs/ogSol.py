def minCostClimbingStairs(cost: list[int]):
    def dp(i):
        if i <= 1:
            return 0
        
        if i in memo:
            return memo[i]
        
        memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])

        return memo[i]
        
    memo = {}

    return dp(len(cost))

def minCostClimbingStairsBottomUp(cost: list[int]):
    n = len(cost)
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

    return dp[n]