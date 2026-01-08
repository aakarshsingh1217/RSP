def subarrayProdLessThanK(nums: list[int], k: int) -> int:
    if k <= 1:
        return 0

    numSubArrs = left = 0
    currProd = 1

    for right in range(len(nums)):
        currProd *= nums[right]

        while currProd >= k:
            currProd //= nums[left]
            left += 1

        numSubArrs += right - left + 1

    return numSubArrs

nums = [10, 5, 2, 6]
k = 100

print(f"Num subarrays: {subarrayProdLessThanK(nums, k)}")