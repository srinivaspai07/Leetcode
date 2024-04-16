class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0  # Initialize the count of subarrays with sum equal to k
        sum_freq = {0: 1}  # Initialize a hashmap to store cumulative sum frequencies
        cumulative_sum = 0  # Initialize the cumulative sum
        
        for num in nums:
            cumulative_sum += num  # Update the cumulative sum
            
            # Check if (cumulative_sum - k) has been encountered before
            # If it has, add the frequency of (cumulative_sum - k) to the count
            if cumulative_sum - k in sum_freq:
                count += sum_freq[cumulative_sum - k]
            
            # Update the frequency of the current cumulative sum
            # in the sum_freq hashmap
            sum_freq[cumulative_sum] = sum_freq.get(cumulative_sum, 0) + 1
        
        return count
