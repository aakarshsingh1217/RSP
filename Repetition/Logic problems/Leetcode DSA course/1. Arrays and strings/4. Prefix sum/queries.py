def findQueries(nums: list[int], queries: list[list[int]], limit: int) -> list[bool]:
    prefix = [nums[0]]
    ans = []

    for i in range(1, len(nums)):
        prefix.append(prefix[i - 1] + nums[i])

    for x, y in queries:
        if prefix[y] - prefix[x] + nums[x] < limit:
            ans.append(True)
        else:
            ans.append(False)

    return ans

print(findQueries(
    [1, 6, 3, 2, 7, 2], 
    [[0, 3], [2, 5], [2, 4]],
    13
))