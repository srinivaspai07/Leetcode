class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize an array to store the length of the longest increasing subsequence
        dp = [1] * len(nums)
        
        # Iterate through the array
        for i in range(1, len(nums)):
            # For each number, iterate through the previous numbers
            for j in range(i):
                # If the current number is greater than the previous number
                if nums[i] > nums[j]:
                    # Update the length of the longest increasing subsequence ending at the current number
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # Return the maximum value in the dp array
        return max(dp)
