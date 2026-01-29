def minEffortPath(heights: list[list[int]]) -> int:
    m = len(heights)
    n = len(heights[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def valid(row: int, col: int):
        return 0 <= row < m and 0 <= col < n
    
    def check(row: int, col: int, effort: int, seen: set[tuple]):
        if (row, col) == (m - 1, n - 1):
            return True

        for dx, dy in directions:
            next_row = row + dx
            next_col = col + dy

            if valid(next_row, next_col) and (next_row, next_col) not in seen:
                if abs(heights[next_row][next_col] - heights[row][col]) <= effort:
                    seen.add((next_row, next_col))
                    if check(next_row, next_col, effort, seen):
                        return True

        return False
    
    left = 0
    right = max(max(row) for row in heights)

    while left <= right:
        seen = { (0, 0) }
        mid = (left + right) // 2
        
        if check(0, 0, mid, seen):
            right = mid - 1
        else:
            left = mid + 1
    
    return left