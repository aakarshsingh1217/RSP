def sum_possible(amount: int, nums: list[int]):
    def dp(amount: int, nums: list[int]):
        if amount in memo:
            return memo[amount]
        if amount < 0:
            return False
        if amount == 0:
            return True
        
        for num in nums:
            if dp(amount - num, nums):
                memo[amount] = True
                return True
        
        memo[amount] = False

        return False
    
    memo = {}
    
    return dp(amount, nums)