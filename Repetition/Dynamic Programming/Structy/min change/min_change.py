def min_change(amount: int, coins: list[int]):
    def dp(amount: int, coins: list[int]):
        if amount in memo:
            return memo[amount]
        if amount < 0:
            return float("inf")
        if amount == 0:
            return 0
        
        min_coins = float("inf")
        
        for coin in coins:
            min_coins = min(min_coins, 1 + dp(amount - coin, coins))

        memo[amount] = min_coins

        return memo[amount]
    
    memo = {}

    ans = dp(amount, coins)

    if ans == float("inf"):
        return -1
    else:
        return ans