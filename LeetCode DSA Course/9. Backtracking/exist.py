def exist(board: list[list[str]], word: str) -> bool:
    def valid(row, col):
        return 0 <= row < m and 0 <= col < n
    
    def backtrack(row: int, col: int, i: int, seen: set):
        if i == len(word):
            return True
        
        for dx, dy in directions:
            next_row, next_col = row + dy, col + dx

            if valid(next_row, next_col) and (next_row, next_col) not in seen:
                if board[next_row][next_col] == word[i]:
                    seen.add((next_row, next_col))

                    if backtrack(next_row, next_col, i + 1, seen):
                        return True
                    
                    seen.remove((next_row, next_col))

            return False

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    m = len(board)
    n = len(board[0])

    for row in range(m):
        for col in range(n):
            if board[row][col] == word[0] and backtrack(row, col, 1, { (row, col) }):
                return True
            
    return False