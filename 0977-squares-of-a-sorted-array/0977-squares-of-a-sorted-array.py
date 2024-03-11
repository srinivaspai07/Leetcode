class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l = 0
        r = len(nums) - 1

        while l <= r:  # Update the loop termination condition to include cases where l == r
            if abs(nums[l]) > abs(nums[r]):  # Compare absolute values
                res.append(nums[l] * nums[l])
                l += 1
            else:
                res.append(nums[r] * nums[r])
                r -= 1  # Decrement r since we're appending the square of nums[r]

        # Reverse the result array since we are appending squares from the end
        return res[::-1]
