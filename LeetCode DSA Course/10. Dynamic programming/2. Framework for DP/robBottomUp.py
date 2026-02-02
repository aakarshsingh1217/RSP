def rob(nums: list[int]) -> int:
    # To avoid out of bounds error from setting base case.
    if len(nums) == 1:
        return nums[0]
    
    n = len(nums)
    dp = [0] * n

    # Base cases.
    back_two = nums[0]
    back_one = max(nums[0], nums[1])

    for i in range(2, n):
        # back_two becomes back_one, and back_one gets updated
        back_one, back_two = max(back_one, back_two + nums[i]), back_one

    return back_one

"""
def rob(nums: list[int]) -> int:
    # To avoid out of bounds error from setting base case.
    if len(nums) == 1:
        return nums[0]
    
    n = len(nums)
    dp = [0] * n

    # Base cases.
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        # Recurrence relation.
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[n - 1]
"""