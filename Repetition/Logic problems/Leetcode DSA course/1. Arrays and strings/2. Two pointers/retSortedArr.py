def retSorted(arr1: list[int], arr2: list[int]) -> list[int]:
    i = j = 0
    newArr = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            newArr.append(arr1[i])
            i += 1
        else:
            newArr.append(arr2[j])
            j += 1

    while i < len(arr1):
        newArr.append(arr1[i])
        i += 1

    while j < len(arr2):
        newArr.append(arr2[j])
        j += 1

    return newArr

print(retSorted([1, 2, 2, 3, 4, 6], [-1, -3, 0, 0, 2, 6]))