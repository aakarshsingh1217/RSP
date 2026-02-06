"""
- Prob recap:
  - Stones have heights: heights[i].
  - Start at stone 0.
  - Goal: reach stone n - 1.
  - From stone i, can jump to:
    - i + 1 (1 step).
    - i + 2 (2 steps).
  - Jump cost = abs. height diff.
- Need min. total cost to reach last stone.

- E.g.:
  - height = [10, 30, 40, 20]
    index     0   1   2   3

- Step 1: Define DP meaning:
  - dp[i] = min. energy needed to reach stone i.
- Step 2: Base cases:
  - Start at stone 0, so dp[0] = 0.
  - To reach stone 1, only one possib. jump:
    - dp[1] = |height[1] - height[0]|.
            = 20.
- Step 3: Recuurrence (choice at every stone):
  - To reach stone i, last jump was either:
    - Option 1 - from i - 1:
      - dp[i - 1] + |height[i] - height[i - 1]|.
    - Option 2 - from i - 2:
      - dp[i - 2] + |height[i] - height[i - 2]|
  - Choose cheaper one:
    - dp[i] = min(option1, option2).
- Step 4: E.g. execution (bottom up thinking).
  - Stone 0: dp[0] = 0
  - Stone 1: dp[1] = |30 - 10| = 20
  - Stone 2:
    - From stone 1: dp[1] + |40 - 30| = 20 + 10 = 30.
    - From stone 0: dp[0] + |40 - 10| = 0 + 30 = 30.
    - Take min: dp[2] = 30.
"""

def frog_jump_top_down(height: list[int]) -> int:
    n = len(height)
    memo = {}

    def dp(i):
        if i == 0:
            return 0
        if i == 1:
            return abs(height[1] - height[0])
        
        if i in memo:
            return memo[i]
        
        one = dp(i - 1) + abs(height[i] - height[i - 1])
        two = dp(i - 2) + abs(height[i] - height[i - 2])

        memo[i] = min(one, two)

        return memo[i]
    
    return dp(n - 1)

print(frog_jump_top_down([10, 30, 40, 20]))

def frog_jump_bottom_up(heights: list[int]) -> int:
    n = len(heights)
    dp = [0] * (n)

    dp[1] = abs(heights[1] - heights[0])

    for i in range(2, n):
        one = dp[i - 1] + abs(heights[i] - heights[i - 1])
        two = dp[i - 2] + abs(heights[i] - heights[i - 2])

        dp[i] = min(one, two)

    return dp[n - 1]

print(frog_jump_bottom_up([10, 30, 40, 20]))