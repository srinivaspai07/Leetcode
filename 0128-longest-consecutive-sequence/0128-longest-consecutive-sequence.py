class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return 1
        
        nums.sort()
        start = 0
        result = 0
        while start < len(nums) - 1:
            count = 1
            index = start
            while index < len(nums) - 1 and nums[index + 1] - nums[index] <= 1:
                if nums[index + 1] - nums[index] == 1:
                    count += 1
                index += 1
            start = index + 1  # Update the custom start position
            result = max(result, count)

        return result
