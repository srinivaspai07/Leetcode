class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        # The target sum we are trying to achieve
        if (target + total_sum) % 2 != 0 or total_sum < abs(target):
            return 0
        
        subset_sum = (target + total_sum) // 2
        
        # DP array to store the number of ways to achieve a given subset sum
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # There's one way to make a sum of 0: using no elements
        
        # Fill the dp array
        for num in nums:
            # Update in reverse order to avoid recomputation issues
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]
        
        return dp[subset_sum]
