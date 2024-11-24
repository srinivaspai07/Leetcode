class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        if len(pattern) != len(s.split()):
            return False

        words = s.split()
        i = 0
        wordMap = dict()
        visited = []
        f = 1
        for word in words:
            if word not in wordMap and pattern[i] not in visited:
                
                wordMap[word] = pattern[i]
                visited.append(pattern[i])
            else:

                present = wordMap.get(word,0)     
                if not present:
                    f = 0
                    break
                if wordMap[word] != pattern[i]:
                    f= 0
                    break
                    
            i +=1

        return f
   

# this is a better cleaner solution from chatpgt....

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()  # Split the string into words
        if len(pattern) != len(words):  # Lengths must match
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            # Check if the pattern character maps to the current word
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word

            # Check if the word maps to the current pattern character
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char

        return True
