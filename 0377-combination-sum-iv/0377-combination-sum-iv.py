class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Memoization dictionary to store results of subproblems
        memo = {}

        # Backtracking with memoization
        def backtrack(remaining: int) -> int:
            # Base case: If the target is hit, return 1 (one valid combination)
            if remaining == 0:
                return 1
            
            # If the remaining becomes negative, no valid combination
            if remaining < 0:
                return 0
            
            # If the result for the current remaining target is already computed
            if remaining in memo:
                return memo[remaining]
            
            # Compute combinations recursively
            result = 0
            for num in nums:
                result += backtrack(remaining - num)
            
            # Store the result in the memo before returning
            memo[remaining] = result
            return result
        
        # Start backtracking from the full target
        return backtrack(target)
