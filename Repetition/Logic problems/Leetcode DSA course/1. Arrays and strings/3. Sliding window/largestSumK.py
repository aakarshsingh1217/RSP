def largestSumK(arr: list[int], k: int):
    currSum = 0

    for i in range(k):
        currSum += arr[i]

    ans = currSum

    for i in range(k, len(arr)):
        currSum += arr[i]
        currSum -= arr[i - k]
        ans = max(ans, currSum)

    return ans