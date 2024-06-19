class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if not nums1 and not nums2:
            return
        
        uniqueNums1 = set(nums1)
        uniqueNums2 = set(nums2)
        result = []

        if len(uniqueNums1) < len(uniqueNums2):

            for num in uniqueNums1:
                if num in uniqueNums2:
                    result.append(num)
        else:
            for num in uniqueNums2:
                if num in uniqueNums1:
                    result.append(num)
        
        return result
