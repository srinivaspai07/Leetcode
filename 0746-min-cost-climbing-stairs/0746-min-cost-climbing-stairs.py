class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            # Calculate the minimum cost to reach step i
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        # The minimum cost to reach the top is the minimum of reaching the last two steps
        return min(dp[n-1], dp[n-2])
