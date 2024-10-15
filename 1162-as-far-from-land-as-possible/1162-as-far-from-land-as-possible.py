from typing import List
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()

        # Add all land cells (1) to the queue initially
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    queue.append((row, col, 0))  # (row, col, distance)

        # If there are no water cells or no land cells, return -1
        if not queue or len(queue) == n * n:
            return -1

        # Directions for moving up, down, left, and right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        max_distance = -1

        # Perform BFS from all land cells
        while queue:
            row, col, dist = queue.popleft()

            # Explore all 4 directions
            for dr, dc in directions:
                new_r, new_c = row + dr, col + dc

                # If the new cell is valid and is water (0)
                if 0 <= new_r < n and 0 <= new_c < n and grid[new_r][new_c] == 0:
                    # Mark the cell as visited by setting it to 1 (land)
                    grid[new_r][new_c] = 1
                    # Append the new cell with updated distance
                    queue.append((new_r, new_c, dist + 1))
                    # Update the maximum distance encountered
                    max_distance = max(max_distance, dist + 1)

        return max_distance
