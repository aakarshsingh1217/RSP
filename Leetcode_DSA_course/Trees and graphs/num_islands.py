"""
Example input: 
grid = [
  ["1","1","0"],
  ["0","1","0"],
  ["1","0","1"]
]
"""

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        # Check whether (row, col) is inside the grid AND is land ("1")
        # Example: valid(0,1) → True, valid(0,2) → False (water)
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"
        
        # Depth-First Search to visit all land cells connected to (row, col)
        # Example: dfs(0,0) will visit (0,0) → (0,1) → (1,1)
        def dfs(row, col):

            # Try all 4 directions: right, down, left, up
            for dx, dy in directions:

                # Compute next cell to explore
                # Example from (0,0): (0,1), (1,0), (0,-1), (-1,0)
                next_row, next_col = row + dy, col + dx
                
                # If next cell is land and hasn't been visited yet
                if (valid(next_row, next_col) and (next_row, next_col) not in seen):

                    # Mark the cell as visited
                    seen.add((next_row, next_col))

                    # Continue DFS from that cell
                    dfs(next_row, next_col)

        # Possible moves: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Set to track visited land cells
        seen = set()

        # Count of islands
        ans = 0

        # Number of rows (m) and columns (n)
        m = len(grid)
        n = len(grid[0])

        # Traverse every cell in the grid
        for row in range(m):
            for col in range(n):

                # If we find unvisited land, it's a NEW island
                # Example: (0,0), then later (2,0), then (2,2)
                if (grid[row][col] == "1" and (row, col) not in seen):

                    # Found a new island
                    ans += 1

                    # Mark starting cell as visited
                    seen.add((row, col))

                    # Visit all connected land cells
                    dfs(row, col)

        # Return total number of islands found
        return ans
