class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return -1
    
        beg, end = 0, len(nums) - 1
        
        while beg <= end:
            
            mid = (beg + end) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                end = end -1
            
            else:   
                beg = beg + 1
        
        return -1
                