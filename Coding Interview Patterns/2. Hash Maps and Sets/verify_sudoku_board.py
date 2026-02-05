"""
- Primary objective is to check every row, col. and each of the
9 3*3 subgrids, for any duplicate nums.

- Can use a hashset to improve time compl. from O(n^2), by using
hashset, can keep track of which nums. visited prev. as we iter.
through row.
- When we encounter new num, check if it's already in set in
O(1) time, if it then it's a duplicate.

- If we had hashset for each of 9 rows, could keep track of dupl.
in each row separately.
- Can do this for cols. and subgrids as well, w/ one hashset for
each col. and subgrid.
- Challenge is determining which hashseets corresp. to each cell's
row, col and subgrid, so we know which hashset to refr.

- Identifying rows straightforward as we have index.
- Same applies to cols., therefore, can creat arr. of 9
hashseets for each row and col allowing us to access row/cols
hashset by its index.
- Similarly, we can setup an arr. of hashsets for each col.:
  - row_sets = [hashset(), ..., hashset()]
                    0               8
  - col_sets = [hashset(), ..., hashset()]
                    0               8

- Subgrids pose interesting challenge bc. we can't immediately
identify which subgrid a cell belongs to unlike index-based
identif. for rows and cols.
- There's only 9 subgrids like rows and cols., if we visualize
subgrids, can see them displayed in a 3*3 grid.

- Need to index each of these subgrids as if indexing 3*3
matrix.
- To do this, req. method to convert indexes ranging from 0
to 8 to corresp. adjusted indexes from 0 to 2.

- Since we got these adjusted indexes from shrinking 9*9 grid
to 3*3 grid (dividing num. rows and cols. by 3), we can get
new subgrid row and col. indexes by diving by 3 (using int.
division) as well.
  - 0  1  2    3  4  5    6  7  8
    / 3 = 0    / 3 = 1    / 3 = 2

- With these modified indexes, can organise 9 hashsets within
3*3 table, one for each subgrid.
- Each cell in table repr. corresp. subgrid in 3*3 repr.
- So we can access hashset of a subgrid at any cell by using
adjusted index (subgrid_sets[r // 3][c // 3]).

- Now can do one pass sol.
- Start by init. hashsets, 9 for each row, 9 for each col.
9 for each subgrid, using 3*3 arr.

- As we iter. through each cell in grid, check if prev.
encountered num. alr. exists in curr. row, col.  or subgrid,
by querying appropriate hashsets.
  - If no. in any of these hashsets, ret. false, otherwise add
  to corresp. row, col. and subgrid hashsets.

- Space compl.: O(n^2) for arbitrary n * n board because of
n * n sets (e.g. row_sets has n sets, can hold up to n nums.).
"""

def verify_sudoku_board(board: list[list[int]]) -> bool:
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]

            if num == 0:
                continue

            if num in row_sets[r]:
                return False
            if num in col_sets[c]:
                return False
            if num in subgrid_sets[r // 3][c // 3]:
                return False
            
            row_sets[r].add(num)
            col_sets[c].add(num)
            subgrid_sets[r // 3][c // 3].add(num)

    return True