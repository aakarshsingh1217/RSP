def binary_search(arr, key, low, high):
    if (low > high):
        return -1
    
    middle = (low + high) // 2

    if (arr[middle] == key):
        return middle
    
    if (arr[middle] > key):
        return binary_search(arr, key, low, middle - 1)
    else:
        return binary_search(arr, key, middle + 1, high)

# count how many times a key k appears
# if k = 4, ans should be 3
# naive idea, do binary search, find one occurence
# scan left until values differ, scan right until values differ
# worst case, array = [4, 4, 4, 4], scanning is O(n)
sorted_arr = { 1, 2, 4, 4, 4, 5, 7}

# fast idea (always O(log n)), modify binary search to find
# left boundary (first index where arr[i] >= k) and right
# boundary (first index where arr [i] > k).
# remove if (arr[middle] == key), if arr[middle] >= key, go left
# else if arr[middle] < key, go right

def first_ge(arr, key):
    low = 0
    high = len(arr) - 1
    result = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= key:
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result

def first_gt(arr, key):
    low = 0
    high = len(arr) - 1
    result = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > key:
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result

def count_occurrences(arr, key):
    left = first_ge(arr, key)
    right = first_gt(arr, key)
    return right - left