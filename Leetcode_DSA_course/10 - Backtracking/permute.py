class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(curr):
            # We've used all nums and hit a leaf node.
            if (len(curr) == len(nums)):
                # curr[:] is list slicing, and here means "make
                # a shallow copy of list curr" (saves curr perm.
                # as list).
                # curr[:] creates a new list with same elems.,
                # so ans.append(curr[:]) stores seperate copy
                # unaffected by later pop() calls.
                ans.append(curr[:])

                return
            
            for num in nums:
                if (num not in curr):
                    curr.append(num)
                    backtrack(curr)
                    # Moving up tree, need to remove elem. to go down
                    # next path.
                    curr.pop()
        
        ans = []
        backtrack([])

        return ans