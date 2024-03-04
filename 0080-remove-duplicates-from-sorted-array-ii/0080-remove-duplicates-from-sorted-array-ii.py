class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 0
        check = collections.Counter(nums)
        
        print(check)
        for num in nums:
            
            if check.get(num) > 2:
                check[num] = check[num] - 1
            else:
                nums[k] = num
                k += 1
        return k
            
        