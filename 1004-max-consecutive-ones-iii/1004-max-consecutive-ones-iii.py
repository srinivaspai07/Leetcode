class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        max_len = 0
        zeros_count = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeros_count += 1

            # Shrink the window until we have at most k zeros
            while zeros_count > k:
                if nums[l] == 0:
                    zeros_count -= 1
                l += 1

            # Update the maximum length of the window
            max_len = max(max_len, r - l + 1)

        return max_len
