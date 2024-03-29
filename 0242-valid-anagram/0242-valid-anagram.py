class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        word1 = collections.Counter(s)
        word2 = collections.Counter(t)
        
        sorted_word1 = dict(sorted(word1.items(), key=lambda item: item[1]))
        sorted_word2 = dict(sorted(word2.items(), key=lambda item: item[1]))
        
        return 1 if sorted_word1 == sorted_word2 else 0
        
        