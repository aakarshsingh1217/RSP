def counting_change(amount: int, coins: list[int]):
    """
    i repr. current coin choosing for.
    """
    def dp(amount: int, i: int):
        if (amount, i) in memo:
            return memo[(amount, i)]
        if amount == 0:
            return 1
        if i == len(coins):
            return 0
        
        coin = coins[i] # Gives single coin val.

        """
        Let's say amount was 20, and curr. coin was just 5.
        20 / 5 = 4, which means you can take at most 4 5 cent
        coins rn. 2nd arg. in range func. is exclusive, so
        if you want to include it, add 1.

        If amt. was 22, 22 / 5 = 4.something, means you should
        take at most 4 out of this quantity. So round division
        down with integer divison.

        Then multiply quantity by coin and subtract from amt.
        (remaining amt.) and call dp on it recursively by increm.
        index because you just made decision for coin at index
        i.
        """
        total_ways = 0

        for qty in range(0, (amount // coin) + 1):
            remainder = amount - (qty * coin)
            total_ways = dp(remainder, i + 1)

        """
        Amount changes as well as index, so need to be sure
        to use both of those pieces of info. as keys of memo.
        W/ memoization, we're taking args. that dictate output
        or return for a func. and making it keys of a memo.
        """

        memo[(amount, i)] = total_ways

        return memo[(amount, i)]
    
    memo = {}
        
    return dp(amount, 0)