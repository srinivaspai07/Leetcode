class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        if k > len(nums) or k == 1:
            return 0

        nums.sort()
        
        l , r = 0 , k-1
        difference = float("inf")
        
        while r < len(nums):
            difference = min(difference, nums[r]-nums[l])
            #print(difference)
            r += 1
            l += 1
        
        return difference
                
        