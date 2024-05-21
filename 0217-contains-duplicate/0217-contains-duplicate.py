class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        arr = collections.Counter(nums)
        for value in arr.values():
            if value >= 2:
                return True
        return False