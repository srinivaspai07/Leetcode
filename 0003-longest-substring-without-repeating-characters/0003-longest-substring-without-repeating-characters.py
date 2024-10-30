class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        
        l , r = 0 , 0
        longest = set()
        maximum = 0
        
        for _ in range(len(s)):
            
            if s[r] in longest:        
                while s[r] in longest:
                    longest.remove(s[l])
                    l += 1
            longest.add(s[r])
            r += 1
        
            
            maximum = max(maximum,r-l)
        
        return maximum
                    
            
        
        
        
        
"""        
        l = 0  # Left pointer of the sliding window
        longest = 0  # Length of the longest substring
        substr = set()  # Set to store characters in the current substring

        for r in range(len(s)):
            # If the character at index 'r' is already in the substring,
            # move the left pointer to the right of the last occurrence of that character
            while s[r] in substr:
                substr.remove(s[l])
                l += 1
            
            # Add the character at index 'r' to the substring
            substr.add(s[r])
            
            # Update the length of the longest substring
            longest = max(longest, r - l + 1)
        
        return longest
"""