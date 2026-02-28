def twoSumSorted(arr: list[int], target: int) -> bool:
    start = 0
    end = len(arr) - 1

    while start < end:
        if arr[start] + arr[end] == target:
            return True
        elif arr[start] + arr[end] > target:
            end -= 1
        else:
            start += 1

    return False

print(twoSumSorted([1, 2, 4, 6, 8, 9, 14, 15], 13))