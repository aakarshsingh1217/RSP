"""
- If we fix one num. in triplet, prob. reduced to finding
other two, leading to following observ.:
  - For any triple [a, b, c], if we fix 'a' we can focus
  on finding pair [b, c] that sums to -a.

- First thing to do is sort the input:
  - [-2, -1, -1, 1, 2, 2].

- Now starting at first elem. (-2), use pair_sum_sorted on
res. to find pair whose sum = 2 (i.e. -a).

- No pairs found with sum of 2, so increment main ptr.
and try again.
  - a = -1, -a = 1, pair found at index 2 and index 5,
  -1 and 2 (-1 + 2 = 1).

- If we continue process, find that [-1, -1, 2] only triplet
whose sum is 0.

- To avoid duplicate triples, we must first avoid duplicate 'a'
vals. (keep increasing i where nums[i] repr. val. a) until it
reaches diff. val. from prev. one.

- To avoid duplicate b vals., we notice for a fixed target val.
-a, pairs that start with the same number 'b' always the same,
we don't need to handle c vals. as it's determined by eq.
c = -(a = b), so each unique [a, b] pair res. in a unique
'c' val.

- Triplets that sum to 0 cannot be formed using pos. nums.
alone, therefore, we can stop trying to find triplets once
we reach a positive 'a' val. since this implies that 'b' and
'c' would also be pos.
"""

def triplet_sum(nums: list[int]) -> list[list[int]]:
    ans = []
    nums.sort()

    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        pairs = pair_sum_sorted_all_pairs(nums, i + 1, -nums[i])

        for pair in pairs:
            ans.append([nums[i]] + pair)

    return ans

def pair_sum_sorted_all_pairs(nums: list[int], start: int, target: int) -> list[int]:
    pairs = []
    left, right = start, len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            pairs.append([nums[left], nums[right]])
            left += 1

            while left < right and nums[left] == nums[left - 1]:
                left += 1
        elif sum < target:
            left += 1
        else:
            right -= 1

    return pairs