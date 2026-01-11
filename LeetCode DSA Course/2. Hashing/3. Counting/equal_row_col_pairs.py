from collections import defaultdict

def equalPairs(grid: list[list[int]]) -> int:
    def convert_to_key(arr):
        return tuple(arr)
    
    dic1 = defaultdict(int)

    for row in grid:
        dic1[convert_to_key(row)] += 1

    dic2 = defaultdict(int)

    for col in range(len(grid[0])):
        curr_col = []

        for row in range(len(grid)):
            curr_col.append(grid[row][col])

        dic2[convert_to_key(curr_col)] += 1

    ans = 0

    for arr in dic1:
        ans += dic1[arr] * dic2[arr]

    return ans