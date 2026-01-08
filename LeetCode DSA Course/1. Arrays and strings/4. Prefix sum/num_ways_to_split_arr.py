def num_ways_to_split_arr(nums: list[int]) -> int:
    prefix = [nums[0]]

    for i in range (1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    ans = 0

    # len(nums) - 1 as we can't split at last index
    for i in range(len(nums) - 1):
        leftSect = prefix[i]
        rightSect = prefix[-1] - prefix[i]

        if leftSect >= rightSect:
            ans += 1

    return ans