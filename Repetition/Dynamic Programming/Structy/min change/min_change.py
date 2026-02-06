def min_change(amount: list[int], coins: int):
    def dp(amount: list[int], coins: int):
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

        return min_coins
    
    memo = {}

    ans = dp(amount, coins)

    if ans == float("inf"):
        return -1
    else:
        return ans