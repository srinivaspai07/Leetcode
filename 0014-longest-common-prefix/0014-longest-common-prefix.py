from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += s

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the input list is empty, return an empty string
        if not strs:
            return ""

        res = ""

        # Iterate through the characters of the first string in the list
        for i in range(len(strs[0])):
            # Iterate through all strings in the list
            for s in strs:
                #print(s[i])
                #print(s)
                if i == len(s) or s[i] != strs[0][i]:
                    # If so, return the common prefix found so far
                    return res
            # If all strings have the same character at the current index,
            # append this character to the common prefix
            res += strs[0][i]

        # Return the common prefix found
        return res

