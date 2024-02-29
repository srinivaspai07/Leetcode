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