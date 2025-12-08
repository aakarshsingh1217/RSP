def insertion_sort(s: list[int]) -> None:
    n: int = len(s)

    for i in range(1, n):
        j: int = i

        while j > 0 and s[j] < s[j - 1]:
            temp: int = s[j - 1]
            
            s[j - 1] = s[j]
            s[j] = temp
            j -= 1