def climbStairs(n: int) -> int:
    memo = [0] * (n + 1)

    return climb_Stairs(0, n, memo)

def climb_Stairs(i: int, n: int, memo: list[int]) -> int:
    if i > n:
        return 0
    if i == n:
        return 1
    if memo[i] > 0:
        return memo[i]
    
    memo[i] = climb_Stairs(i + 1, n, memo) + climb_Stairs(i + 2, n, memo)

    return memo[i]