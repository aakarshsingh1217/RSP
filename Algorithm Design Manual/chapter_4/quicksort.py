def quicksort(arr, low, high):
    if (low < high):
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)

def partition(arr, low, high):
    pivot_index = high
    first_high = low

    for i in range(low, high):
        if arr[i] < arr[pivot_index]:
            temp = arr[first_high]
            arr[first_high] = arr[i]
            arr[i] = temp
            first_high += 1
    
    temp = arr[pivot_index]
    arr[pivot_index] = arr[first_high]
    arr[first_high] = temp

    return first_high

test_arr = [4, 2, 7, 1, 3]