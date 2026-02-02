def  minCostClimbingStairs(cost: list[int]) -> int:
    """
    Array's length should be 1 longer than the length of cost, this
    is because we can treat the "top" floor as a step to reach.
    """
    minCost = [0] * (len(cost) + 1)

    """
    Start iteration from step 2, since min. cost of reaching step 0
    and step 1 is 0.
    """
    for i in range(2, len(cost) + 1):
        take_one_step = minCost[i - 1] + cost[i - 1]
        take_two_steps = minCost[i - 2] + cost[i - 2]

        minCost[i] = min(take_one_step, take_two_steps)

    # Final elem. in minCost refers to top floor.
    return minCost[-1]