def twoSum(nums: list[int], target: int) -> list[int]:
    dic = {}

    for i in range(len(nums)):
        num = nums[i]
        complement = target - num

        if complement in dic:
            return [i, dic[complement]]
        
        dic[num] = i

    return [-1, -1]