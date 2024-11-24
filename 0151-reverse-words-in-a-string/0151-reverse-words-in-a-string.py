class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.strip().split()
    # Reverse the order of the words
        words.reverse()
        return " ".join(words)
        #print(type(words))
        