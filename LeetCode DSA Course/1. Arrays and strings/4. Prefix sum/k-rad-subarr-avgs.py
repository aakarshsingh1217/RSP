def getAverages(nums: list[int], k: int) -> list[int]:
    prefix = [nums[0]]
    avg = []

    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    for i in range(len(nums)):
        if k == 0:
            avg.append(nums[i])
        elif i - k >= 0 and i + k < len(nums):
            if (i - k == 0):
                avg.append(prefix[i + k] // (k * 2 + 1))
            else:
                avg.append((prefix[i + k] - prefix[i - k - 1]) // (k * 2 + 1))
        else:
            avg.append(-1)

    return avg

nums = [7,4,3,9,1,8,5,2,6]
k = 3
avgs = getAverages(nums, k)

for avg in avgs:
    print(avg)

"""
Better sol.

def getAverage(nums: list[int], k: int) -> list[int]:
    # When a single elem. is considered then its average
    # will be num. itself only.
    if k == 0:
        return nums

    windowSize = 2 * k + 1
    n = len(nums)
    averages = [-1] * n

    # Any index will not have 'k' elems. in its left and right
    if windowSize > n:
        return averages

    # Generate prefix array for nums.
    # prefix[i + 1] will be sum of all nums from index 0
    # to index i.

    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    # Iterate only on indices which have atleast 'k' elems.
    # in their left and right, i.e. indices from k to
    # n - k.

    for i in range(k, n - k):
        leftBound, rightBound = i - k, i + k
        subArraySum = prefix[rightBound + 1] - prefix[leftBound]
        average = subArraySum // window_size
        averages[i] = average

    return average
"""