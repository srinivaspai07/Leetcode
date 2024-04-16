class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_pos_len = 0  # Maximum length of a subarray with positive product
        max_neg_len = 0  # Maximum length of a subarray with negative product
        max_len = 0  # Overall maximum length of a subarray with positive product

        for num in nums:
            if num == 0:
                max_pos_len = max_neg_len = 0  # Reset lengths if encountering 0
            elif num > 0:
                max_pos_len += 1  # Increment length of positive subarray
                if max_neg_len > 0:
                    max_neg_len += 1  # Increment length of negative subarray
            else:  # num < 0
                new_max_pos_len = max_neg_len + 1 if max_neg_len > 0 else 0
                new_max_neg_len = max_pos_len + 1
                max_pos_len = new_max_pos_len
                max_neg_len = new_max_neg_len

            max_len = max(max_len, max_pos_len)

        return max_len
