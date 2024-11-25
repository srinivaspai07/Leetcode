class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_indices = {}  # Dictionary to store indices of numbers
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # If the number is already in the dictionary and the absolute difference
            # between the current index and the previous index is less than or equal to k,
            # return True
            if num in num_indices and i - num_indices[num] <= k:
                return True
            # Otherwise, update the index of the number in the dictionary
            num_indices[num] = i

        # If no such pair of indices is found, return False
        return False

        # Removed misplaced code block with incorrect indentation
        """
          does not work for all inputs... example:
 input [1,2,3,1,2,3] , k = 2
Output
true
Expected
false

        nums.sort()
        
        for i in range(len(nums)-1):
            
            if (abs(nums[i] - nums[i]-1)) <= k:
                return True
        return False
        """
  
