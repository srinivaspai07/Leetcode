class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If the total sum is odd, we can't partition it into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        # Initialize a DP array to store if a sum is possible
        dp = [False] * (target + 1)
        dp[0] = True  # Zero sum is always possible
        
        # Process each number in the nums array
        for num in nums:
            # Update the DP array from the back to avoid using the same number twice
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]
