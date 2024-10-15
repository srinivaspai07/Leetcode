class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = [0] * (len(triangle)+ 1)
        for row in triangle[::-1]:
            for index, value in enumerate(row):
                dp[index] = value + min (dp[index], dp[index+1])
        
        return dp[0]
        