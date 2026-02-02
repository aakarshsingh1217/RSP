def minCostClimbingStairs(cost: list[int]) -> int:
    n = len(cost)
    # Step 2.
    dp = [0] * (n + 1)

    # Step 3: Base casses implicitly defined as they're 0.

    # Step 4.
    for i in range(2, n + 1):
        # Step 5.
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

    # Step 6

    return dp[n]