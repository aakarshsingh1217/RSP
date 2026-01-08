def sol(nums: list[int], queries: list[list[int]], limit: int):
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[i - 1])

    boolArr = []

    for i in range(len(queries)):
        index1 = queries[i][0]
        index2 = queries[i][1]

        if prefix[index2] - prefix[index1] + nums[index1] < limit:
            boolArr.append(True)
        else:
            boolArr.append(False)

    return boolArr


nums = [1, 6, 3, 2, 7, 2]
queries = [[0, 3], [2, 5], [2, 4]]
limit = 13

boolArr = sol(nums, queries, limit)

for i in range(len(boolArr)):
    print(f"{i}: {boolArr[i]}")

"""
Better sol.:

def answer_queries(nums, queries, limit):
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[i - 1])

    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)

    return ans
"""