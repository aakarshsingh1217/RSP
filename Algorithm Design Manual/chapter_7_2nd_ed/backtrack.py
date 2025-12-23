"""
Given an int arr nums that may contain duplicates, return all
possible subsets (sol cannot contain duplicate subsets but
can be in any order).

E.g. input: nums = [1, 2, 2]
     output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

Backtracking is like solving a maze, if path leads to dead
end, backtrack to last known decision point and try diff
path.

5 steps to backtracking alg:

1. Start (begin with no numbers chosen)
2. Choose (each num, decide to use or skip)
3. Move forward (if you use a num, consider next one, if
   you skip a num, move to next num but dont add curr one)
4. End point (When you've considered all numbers, you've
   made a group. If you see repeated numbers, avoid making
   same group again)
5. Go back (if one group is made, go back to last choice and
   try a different way, meaning removing last number used and
   thinking about next choice)

E.g.: [1, 2, 2]

Start with empty subset []
For first num 1, decide to include [1]
For next number 2, decide to include it [1, 2]
For last number 2, decide to include it [1, 2, 2]
Now backtrack, remove last num and decide to excl [1, 2]
But no more numbers to consider, so backtrack again
[1]
[2]
[2, 2]
[2] (second 2 is backtracked)
Repeat process until all paths (or subsets) explored
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        def backtrack(start, current):
            # add current subset to final result
            result.append(list(current))
            # iterate over nums to gen all possible subsets
            for i in range(start, len(nums)):
                # 1. skip duplicates
                if (i > start and nums[i] == nums[i - 1]):
                    continue
                # 2. include nums[i] in curr subset and 
                # move forward
                current.append(nums[i])
                backtrack(i + 1, current)
                # 3. exclude nums[i] from curr subset (backtrack)
                current.pop()


        result = []
        # sort numbers to handle duplicates
        nums.sort()
        # initiate backtracking from index 0 (empty subset)
        backtrack(0, [])

        return result