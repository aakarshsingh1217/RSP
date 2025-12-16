class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        # Declare hash map (maps elements to their indices)
        dict = {}

        # Loop over elems and put elems into hashmap
        for i in range(len(nums)):
            num = nums[i]
            # Before adding to hash map, check if complement
            # (whatever num that would pair with curr num to
            # create target) has already been seen
            complement = target - num

            # If in dictionary, means we saw it earlier so we
            # can return pair of indices
            if complement in dict:
                return [i, dict[complement]]
            
            # Otherwise put onto hashmap and move onto future elems
            dict[num] = i

        return [-1, -1]