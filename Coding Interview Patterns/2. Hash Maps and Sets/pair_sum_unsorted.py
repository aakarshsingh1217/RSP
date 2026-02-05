"""
- We're asked to find a pair (x, y) such that x + y == target.
- In this eq., there're 2 unknowns: x and y.
- An important observ. is that if we know one of these nums.,
we can easily calc. what the other nums. should be.

- For each num. x in nums, we need to find another num. y such
that x + y = target, or in other words, y = target - x, which
is the complement of x.

- Need to return the indexes of the pair of nums., not pair
itself, so we'll need a way to find a number's complement
as well as its index.

- Could loop through arr. to find each nums. complement and
corresp. index, but this takes O(n^2) time since we'd need
to do linear traversal to search for each nums. complement.
- Instead, need efficient way to determine index of any num.
in arr. w/o needing to search arr.

- Hashmap works great because we can store and lookup vals.
in O(1) time, each num. and its index can be stored in
hashmap as key-val. pairs.

- Allows us to retrieve index of any number's complement
efficiently.
- Duplicate nums. don't need to be considered here since
only one valid pair needs to be found.

- Most intuitive way to incorp. a hashmap is to:
  1. In first pass, populate hashmap with each num. and its
  corresp. index.
  2. In second pass, scan through arr. to check if each nums.
  complement exists in hashmap, if it does, return indexes
  of that num. and its complement.

- One pass sol. implies that we'd need to populate hashmap
while searching for complements, consider e.g. below:
  - [-1, 3, 4, 2], target = 3.
      0  1  2  3
  - Start at index 0, complement is 3 - (-1) = 4, does our
  hashmap have 4 in it? No it's empty, so let's add -1
  and its index to hashmap.
  - Next index 1, its complement (0) doesn't exist in
  hashmap, so just add 3 and its index to hashmap.
  - At index 2, notice 4's complement (-1) exists in
  hashmap, means we found pair that sums to target, now
  can return indexes of two vals.
"""

def pair_sum_sorted_two_pass(nums: list[int], target: int) -> list[int]:
    num_map = {}

    for i in range(len(nums)):
        num_map[nums[i]] = i

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in num_map and num_map[complement] != i:
            return [i, num_map[complement]]
        
    return []

def pair_sum_unsorted(nums: list[int], target: int) -> list[int]:
    hashmap = {}

    for i in range(len(nums)):
        if target - nums[i] in hashmap:
            return [hashmap[target - nums[i]], i]
        
        hashmap[nums[i]] = i

    return []