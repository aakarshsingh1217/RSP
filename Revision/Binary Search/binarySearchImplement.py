def binarySearch(arr: list[int], target: int):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return
        
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left

"""
1. Left-most insertion point (lower bound) with left <= right:
  - Goal: first index i where arr[i] >= target.
  - Why this works:
    - All indices < left are < target.
    - ans always stores the best left-most valid index seen so
    far.
    - When arr[mid] >= target:
      - mid is a valid insertion point.
      - But maybe there's a smaller one -> move left.
    - When loop ends:
      - ans is first index where arr[i] >= target.
  - E.g.:
    - arr = [1, 2, 2, 2, 4, 5]
      target = 2
    - Result: return 1 (correct leftmost pos.).
  - Mental mode: every time arr[mid] >= target, you say "this
  could be the answer, but can I do better on the left?".

2. Right-most insertion point (upper bound) with left <= right:
  - Goal: first index i where arr[i] > target.
  - Why this works:
    - All indices < left are <= target.
    - ans tracks first index > target.
"""

def lowerBound(arr: list[int], target: int):
    left = 0
    right = len(arr) - 1

    ans = len(arr) # Default, insert at end.

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= target:
            ans = mid           # Possible answer.
            right = mid - 1     # Keep searching left.
        else:
            left = mid + 1

    return ans

def upperBound(arr: list[int], target: int):
    left = 0
    right = len(arr) - 1
    ans = len(arr)

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > target:
            ans = mid # Possible answer.
            right = mid - 1
        else:
            left = mid + 1

    return ans