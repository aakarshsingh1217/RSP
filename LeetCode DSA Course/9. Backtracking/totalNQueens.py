def totalQueens(n: int):
    def backtrack(row: int, diags: list[int], anti_diags: list[int], cols: list[int]):
        if row == n: 
            return 1
        
        solutions = 0

        for col in range(n):
            curr_diag = row - col
            curr_anti_diag = row + col
            
            if (col in cols or 
                curr_diag in diags or
                curr_anti_diag in anti_diags):
                continue

            cols.add(col)
            diags.add(curr_diag)
            anti_diags.add(curr_anti_diag)

            solutions += backtrack(row + 1, diags, anti_diags, cols)

            cols.remove(col)
            diags.remove(curr_diag)
            anti_diags.remove(curr_anti_diag)

        return solutions
    
    return backtrack(0, set(), set(), set())