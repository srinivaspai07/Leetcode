class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0  # Left pointer
        current_sum = 0  # Current sum of the subarray
        min_length = float('inf')  # Initialize with positive infinity
        
        for right in range(len(nums)):
            current_sum += nums[right]  # Add the current element to the sum
            
            # If the sum exceeds or equals the target, adjust the window
            while current_sum >= target:
                
                min_length = min(min_length, right - left + 1)  # Update the minimum length
                current_sum -= nums[left]  # Remove the leftmost element from the sum
                left += 1  # Move the left pointer to the right
        
        return min_length if min_length != float('inf') else 0  # Return minimum length, or 0 if no valid subarray
