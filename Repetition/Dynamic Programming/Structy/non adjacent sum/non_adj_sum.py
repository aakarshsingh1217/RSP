def non_adj_sum(nums: list[int], i: int) -> int:
    def dp(nums: list[int], i: int):
        if i in memo:
            return memo[i]
        if i >= len(nums):
            return 0
        """    
        ([a, b, c, d]), say you were making a call on this arr. You 
        would get a + ([c, d]) (rest of the arr. that's non adj.)
        """
        include = nums[i] + dp(nums, i + 2)
        exclude = dp(nums, i + 1)

        memo[i] = max(include, exclude)

        return memo[i]
    
    memo = {}
    
    return dp(nums, 0)