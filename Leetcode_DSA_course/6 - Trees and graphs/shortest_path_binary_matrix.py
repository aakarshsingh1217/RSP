"""
Example grid:
grid = [
  [0, 1, 0],
  [0, 0, 0],
  [1, 0, 0]
]
"""

# Import deque for efficient FIFO queue operations (O(1) pops from left)
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:

        # If the starting cell is blocked, no path is possible
        # Example: if grid[0][0] == 1 → return -1 immediately
        if grid[0][0] == 1:
            return -1
        
        # Helper function to check if a cell is:
        # 1) inside the grid
        # 2) not blocked (value == 0)
        # Example: valid(1,1) → True, valid(0,1) → False (blocked)
        def valid(row, col):
            return 0 <= row < n and 0 <= col < n and grid[row][col] == 0
        
        # Grid size (n x n)
        # Example grid → n = 3
        n = len(grid)

        # Set to track visited cells so we don’t revisit them
        # Start by marking (0,0) as visited
        seen = {(0, 0)}

        # BFS queue storing (row, col, steps_so_far)
        # Start at (0,0) with path length = 1
        queue = deque([(0, 0, 1)])

        # All 8 possible directions:
        # right, down, down-right, up-left, up-right, down-left, left, up
        directions = [
            (0, 1), (1, 0), (1, 1),
            (-1, -1), (-1, 1), (1, -1),
            (0, -1), (-1, 0)
        ]
        
        # Continue BFS while there are cells to explore
        while queue:

            # Pop the front of the queue (current BFS level)
            row, col, steps = queue.popleft()

            # If we reached the bottom-right cell, return path length
            # Example: reaching (2,2) → return steps
            if (row, col) == (n - 1, n - 1):
                return steps
            
            # Try moving in all 8 directions
            for dx, dy in directions:

                # Compute the next cell
                # Example from (1,1): could go to (2,2), (1,2), (0,1), etc.
                next_row, next_col = row + dy, col + dx

                # If the next cell is valid and unvisited
                if valid(next_row, next_col) and (next_row, next_col) not in seen:

                    # Mark the cell as visited
                    seen.add((next_row, next_col))

                    # Add it to the queue with step count increased by 1
                    queue.append((next_row, next_col, steps + 1))
        
        # If BFS finishes without reaching bottom-right, no path exists
        return -1
