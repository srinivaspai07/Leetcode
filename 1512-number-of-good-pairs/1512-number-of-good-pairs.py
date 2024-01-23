class Solution:
    def numIdenticalPairs(self, nums):
        count = 0  # Initialize the count of good pairs to zero
        num_count = {}  # Create a dictionary to store the count of occurrences of each number

        for num in nums:
            if num in num_count:
                # If the number is already in the dictionary, increment the count by the current count
                count += num_count[num]
                # Update the count of occurrences for the current number in the dictionary
                num_count[num] += 1
            else:
                # If the number is not in the dictionary, add it with a count of 1
                num_count[num] = 1

        return count  # Return the final count of good pairs
