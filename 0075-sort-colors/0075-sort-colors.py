class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointers for the next positions of 0 and 2
        left, right = 0, len(nums) - 1
        current = 0
        
        while current <= right:
            if nums[current] == 0:
                # Swap the current element with the leftmost unprocessed element
                nums[current], nums[left] = nums[left], nums[current]
                left += 1
                current += 1
            elif nums[current] == 2:
                # Swap the current element with the rightmost unprocessed element
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
            else:
                # If the element is 1, just move to the next element
                current += 1
