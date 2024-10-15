from typing import List
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        # Add all land cells (1) to the queue initially
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    queue.append((row, col))
        
        # If there are no water cells or no land cells, return -1
        if len(queue) == 0 or len(queue) == rows * cols:
            return -1

        # Directions for moving up, down, left, and right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        maxDistance = -1

        # Perform BFS from all land cells
        while queue:
            row, col = queue.popleft()

            # Explore all 4 directions
            for dr, dc in directions:
                newR, newC = row + dr, col + dc

                # If the new cell is valid and is water (0)
                if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == 0:
                    # Mark the water cell as visited by setting it to 1
                    grid[newR][newC] = grid[row][col] + 1  # Propagate the distance
                    queue.append((newR, newC))
                    # Update the maximum distance encountered
                    maxDistance = max(maxDistance, grid[newR][newC] - 1)

        return maxDistance
