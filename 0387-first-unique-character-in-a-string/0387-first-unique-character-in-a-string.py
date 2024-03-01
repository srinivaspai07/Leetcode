class Solution:
    def firstUniqChar(self, s: str) -> int:

        checkMap = {}

        for index, char in enumerate(s):

            if char not in checkMap:
                checkMap[char] = index
            else:
                checkMap[char] = -1
        
        final = [x for x in checkMap.values() if x!= -1]

        if final:
            return(min(final))
        else:
            return -1
        