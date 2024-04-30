from collections import defaultdict
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = defaultdict(int)
        
        # Count the number of rabbits claiming each color
        for answer in answers:
            counts[answer] += 1
        
        # Calculate the minimum number of rabbits needed
        min_rabbits_count = 0
        for x, count in counts.items():
            # Calculate the minimum number of rabbits needed for this color
            # (count + x) // (x + 1) rounds up to the nearest multiple of (x + 1)
            # Multiply by (x + 1) to get the total minimum rabbits needed for this color
            min_rabbits_count += ((count + x) // (x + 1)) * (x + 1)
        
        return min_rabbits_count
