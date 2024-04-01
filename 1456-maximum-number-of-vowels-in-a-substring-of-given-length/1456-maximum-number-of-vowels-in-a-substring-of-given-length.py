class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vowels = curr_vowels = sum(1 for char in s[:k] if char in vowels)  # Count vowels in the first window
        for i in range(k, len(s)):
            if s[i - k] in vowels:  # Remove outgoing character from the window
                curr_vowels -= 1
            if s[i] in vowels:  # Add incoming character to the window
                curr_vowels += 1
            max_vowels = max(max_vowels, curr_vowels)
        return max_vowels
