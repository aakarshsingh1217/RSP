"""
Acutal sol:

- Need to treat entire matrix as single sorted 1D arr., and convert
1D index back into (row, col) using division and modulo.

Step 1 - flatten matrix:
  - Each row sorted, first elem. of each row greater than last
  elem. of prev. row.
  - So this equiv. to 1D sorted arr.:
    - matrix = [
                  [ 1,  3,  5],
                  [ 7,  9, 11],
                  [13, 15, 17]
               ]

Step 2 - Binary search over flattened arr.:
  - Instead of doing:
    - Binary search on rows.
    - Then binary search on cols.
  - You do:
    - left = 0
      right = m * n - 1
  - At any point: mid = (left + right) // 2.
  - Key question: what elem. in matrix does flat[mid] corresp.
  to?, need index mapping.

Step 3: Map 1D index -> 2D pos.
  - Let: n = num. cols.
  - row = mid // n
    col = mid % n
  - This works because each row has exactly n elems.
  - Integer divison (//) tells you how many full rows you
  skip.
  - Modulo (%) tells you how far into the row you go.
"""

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    m = len(matrix)
    
    if m == 0:
        return False
    
    n = len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        pivot_idx = (left + right) // 2
        pivot_elem = matrix[pivot_idx // n][pivot_idx % n]

        if target == pivot_elem:
            return True
        else:
            if pivot_elem > target:
                right = pivot_idx - 1
            else:
                left = pivot_idx + 1

    return False

"""
my sol:

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        currRowLeft = 0
        currRowRight = len(matrix) - 1
        
        while currRowLeft <= currRowRight:
            currRowMid = (currRowLeft + currRowRight) // 2
            currColLeft = 0
            currColRight = len(matrix[0]) - 1

            while currColLeft <= currColRight:
                currColMid = (currColLeft + currColRight) // 2

                if matrix[currRowMid][currColMid] == target:
                    return True
                
                if matrix[currRowMid][currColMid] > target:
                    currColRight = currColMid - 1
                else:
                    currColLeft = currColMid + 1

            if matrix[currRowMid][0] > target:
                currRowRight = currRowMid - 1
            else:
                currRowLeft = currRowMid + 1

        return False
"""