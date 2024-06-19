from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # Calculate the frequency of characters in both strings
        count_s = Counter(s)
        count_t = Counter(t)
        
        # Initialize the number of steps to 0
        steps = 0
        
        # Iterate through the character frequencies in t
        for char in count_t:
            if count_t[char] > count_s.get(char, 0):
                steps += count_t[char] - count_s.get(char, 0)
        
        return steps
