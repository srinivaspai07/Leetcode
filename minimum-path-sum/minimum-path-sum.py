from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        
        # Initialize dp array with the same size as grid
        dp = [[0] * cols for _ in range(rows)]
        
        # Initialize the starting point
        dp[0][0] = grid[0][0]
        
        # Set the first row
        for col in range(1, cols):
            dp[0][col] = grid[0][col] + dp[0][col - 1]  # Use col for columns

        # Set the first column
        for row in range(1, rows):
            dp[row][0] = grid[row][0] + dp[row - 1][0]  # Use row for rows

        # Fill the rest of the dp array
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        # Return the minimum path sum to the bottom-right corner
        return dp[rows - 1][cols - 1]
