"""
- If we have two vertical lines, heights[i] and heights[j],
the amt. of water that can be contained between these two
lines is min(heights[i], heights[j]) * (j - 1), where j - i
repr. the width of the container.
- Can take min. height because filling water abv. this
height would result in overflow.

- In other words, area of container depends on:
  - Width of rectangle.
  - Height of rectangle, as dictated by shorter of two lines.

- Brute force approach involves checking all pairs of lines
and returning largest area found between each pair.

- We'd like both height and width to be as large as possible
to have largest container.

- Not immediately obv. how to find cont. with largest height,
as heights of lines in arr. don't follow clear pattern.
- However, we know container with max width: one starting at
index 0 and ending at index n - 1.

- So start by max. width by setting pointer at each end of arr.
- Then, gradually reduce width by moving these two pointers
inward, hoping to find container with a larger height that
potentially yields larger area.

- We encounter situation where height of left and right lines
are equal, which pointer should we move inward?
- Regardless of which one, next cont. guaranteed to store less
water than curr. one.

- Moving either pointer inward yields cont. of shorter width,
leaving height as determining factor, and regardless of which
pointer moved inward, other ptr. remains on same line and
will restrict height of water.
  - Since we can't incr. height by moving just one ptr., move
  both inwards.

- Logic:
  1. If left line is smaller, move left ptr. inward.
  2. If right line is smaller, move right ptr. inward.
  3. If both lines have same height, move both ptrs. inward.
"""

def largest_container(heights: list[int]) -> int:
    max_water = 0
    left, right = 0, len(heights) - 1

    while left < right:
        water = min(heights[left], heights[right]) * (right - left)
        max_water = max(max_water, water)

        if heights[left] < heights[right]:
            left += 1
        elif heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
            right -= 1

    return max_water