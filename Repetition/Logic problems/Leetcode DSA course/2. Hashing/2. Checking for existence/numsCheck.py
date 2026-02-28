def doesExist(arr: list[int]) -> list[int]:
    nums_set = set()
    ans = set()

    for num in arr:
        nums_set.add(num)

    for num in arr:
        if num + 1 not in nums_set and num - 1 not in nums_set:
            ans.add(num)

    return ans