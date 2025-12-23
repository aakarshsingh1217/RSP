def selection_sort(unsorted_list: list[int]):
    list_len: int = len(unsorted_list)

    for i in range(0, list_len):
        min_index: int = i

        for j in range(i + 1, list_len):
            if (unsorted_list[j] < unsorted_list[min_index]):
                min_index = j
        
        temp: int = unsorted_list[min_index]
        unsorted_list[min_index] = unsorted_list[i]
        unsorted_list[i] = temp