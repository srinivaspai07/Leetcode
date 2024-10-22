class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Memoization dictionary to store the results of subproblems
        dp = {}
        
        # Backtracking function with memoization
        def backtrack(i, total):
            # Base case: when we've processed all numbers
            if i == len(nums):
                # If the total matches the target, we've found a valid combination
                return 1 if total == target else 0
            
            # If this state has been computed before, return the memoized result
            if (i, total) in dp:
                return dp[(i, total)]
            
            # Explore the two options: add nums[i] or subtract nums[i]
            add = backtrack(i + 1, total + nums[i])
            subtract = backtrack(i + 1, total - nums[i])
            
            # Store the result of the current state in the memoization dictionary
            dp[(i, total)] = add + subtract
            return dp[(i, total)]
        
        # Initial call to the backtracking function
        return backtrack(0, 0)
