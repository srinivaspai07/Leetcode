from typing import List

class Solution:
    """
    A class to solve the maxProduct problem.

    Attributes:
    None
    """
    
    def maxProduct(self, nums: List[int]) -> int:
        """
        Solves the maxProduct problem.

        Args:
        nums: A list of integers.

        Returns:
        The maximum product of any contiguous subarray.
        """
        if not nums:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for num in nums[1:]:
            temp_max = max(num, max_so_far * num, min_so_far * num)
            min_so_far = min(num, max_so_far * num, min_so_far * num)
            max_so_far = temp_max
            result = max(max_so_far, result)

        return result