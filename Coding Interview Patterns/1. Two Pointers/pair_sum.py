"""
- Given this e.g. use two pointers:
    [-5, -2, 3, 4, 6]  target = 7
      0   1  2  3  4

  - Look at the smallest and largest values (first and
  last elems.), sum of them -5 + 6 = 1.

  - Since 1 less than target, need to move one of the
  pointers to find a new pair w/ larger sum.
    - Left pointer: points to a val. less than or equal
    to val. at right pointer bc. arr. sorted, increm. it
    results in a sum >= curr. sum of 1.
    - Right pointer: decrem. right ptr. results in sum
    <= 1.
    - Therefore, increm. left pointer to find larger sum.

- Left = -2, right = 6, -2 + 6 = 4 (too small), increment
left again:
    - Left = 3, right = 6, 3 + 6 = 9 (too large, increm.
    right ptr.).

- Right = 4, left = 3, 4 + 3 = 7 which is target (indexes
2 and 3).

- This is inward traversal.

- Complexity analysis: O(n) time, as in worst case we visit every
element, O(1) space as we only alloc. constant num. vars.
"""

def pair_sum_sorted(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]

        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            return [left, right]
        
    return []