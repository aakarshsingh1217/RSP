def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while (left <= right):
        mid = (left + right) // 2

        if (arr[mid] == target):
            # Do something
            return
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    # Target not in arr, but left is at insertion point
    return left