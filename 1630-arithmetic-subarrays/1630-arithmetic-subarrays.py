class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        retList = [True] * len(l)  # Use boolean values instead of strings
        for i in range(len(l)):
            subarr = nums[l[i]:r[i]+1]
            subarr.sort()
            check = subarr[0] - subarr[1]  # Initialize check for each subarray
            for index in range(len(subarr)-1):
                if subarr[index] - subarr[index+1] != check:
                    retList[i] = False  # Update with boolean False
                    break  # No need to continue checking once a discrepancy is found
        return retList
