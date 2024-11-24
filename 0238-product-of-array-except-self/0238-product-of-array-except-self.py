class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n  # Initialize the result array with 1s

        # Step 1: Calculate prefix product for each index
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Step 2: Calculate suffix product for each index and update result
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
