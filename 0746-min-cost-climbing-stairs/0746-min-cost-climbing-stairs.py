class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        # Initialize variables to store the minimum costs of the last two steps
        prev1 = cost[0]
        prev2 = cost[1]
        
        for i in range(2, n):
            # Calculate the minimum cost to reach step i
            curr_cost = cost[i] + min(prev1, prev2)
            
            # Update prev1 and prev2 for the next iteration
            prev1, prev2 = prev2, curr_cost
        
        # The minimum cost to reach the top is the minimum of reaching the last two steps
        return min(prev1, prev2)
