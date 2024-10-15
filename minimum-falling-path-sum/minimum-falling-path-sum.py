class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        if not matrix:
            return 0
        
        n = len(matrix)
        
        dp = [[0] * n for _ in range (n)]
        
        # first, let's fill the top row
        
        for i in range(n):
            
            dp[0][i] = matrix[0][i]
        
        # filling the rest of the matrix
        
        for i in range(1,n):
            for j in range(0,n):
                if j == 0:
                    dp[i][j] = matrix[i][j] + min (dp[i-1][j], dp[i-1][j+1])
                elif j == n-1:
                    dp[i][j] = matrix[i][j] + min (dp[i-1][j], dp[i-1][j-1])
                else:
                    dp[i][j] = matrix[i][j] + min (dp[i-1][j], dp[i-1][j+1], dp[i-1][j-1])
        
        return min(dp[n-1])

