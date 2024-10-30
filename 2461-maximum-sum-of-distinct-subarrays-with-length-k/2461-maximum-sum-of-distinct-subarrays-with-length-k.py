from typing import List
from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return 0

        maximum_sum = 0
        current_sum = 0
        count_map = defaultdict(int)
        
        # Initialize the first window of size k
        for i in range(k):
            current_sum += nums[i]
            count_map[nums[i]] += 1

        # Check if the first window meets the distinct condition
        if len(count_map) == k:
            maximum_sum = current_sum
        
        # Slide the window across the array
        for i in range(k, len(nums)):
            # Add the new element at the end of the window
            current_sum += nums[i]
            count_map[nums[i]] += 1
            
            # Remove the element going out of the window
            current_sum -= nums[i - k]
            count_map[nums[i - k]] -= 1
            
            # If an element's count becomes zero, remove it from the dictionary
            if count_map[nums[i - k]] == 0:
                del count_map[nums[i - k]]
            
            # Check if all elements in the current window are distinct
            if len(count_map) == k:
                maximum_sum = max(maximum_sum, current_sum)

        return maximum_sum
