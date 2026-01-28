def successfulPairs(spells: list[int], potions: list[int], success: int) -> list[int]:
    def binarySearch(arr, target):
        left = 0
        right = len(arr)

        while left < right:
            mid = (left + right) // 2

            if arr[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left
    
    potions.sort()
    ans = []
    m = len(potions)

    for spell in spells:
        i = binarySearch(potions, success / spell)
        ans.append(m - i)

    return ans