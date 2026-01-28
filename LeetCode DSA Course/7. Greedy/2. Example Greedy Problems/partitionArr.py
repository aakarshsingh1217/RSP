def partitionArr(nums: list[int], k: int) -> int:
    nums.sort()
    ans = 1
    x = nums[0]

    for i in range(1, len(nums)):
        if x + k < nums[i]:
            x = nums[i]
            ans += 1

    return ans