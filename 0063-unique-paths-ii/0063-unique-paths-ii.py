from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # Create dp array
        dp = [[0] * n for _ in range(m)]
        
        # Initialize dp[0][0] if it's not an obstacle
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        # Fill the first row
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
        
        # Fill the first column
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        
        # Fill the rest of the dp array
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # Return the number of unique paths to reach bottom-right corner
        return dp[m-1][n-1]

