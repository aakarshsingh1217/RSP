def combine(arr1: list[int], arr2: list[int]):
    combined_arr = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            combined_arr.append(arr1[i])
            i += 1
        else:
            combined_arr.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        combined_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        combined_arr.append(arr2[j])
        j += 1

    return combined_arr

arr1 = [1, 4, 7, 20]
arr2 = [3, 5, 6]

new_arr = combine(arr1, arr2)

for k in range(len(new_arr)):
    print(f"{new_arr[k]} ", end="")

print()