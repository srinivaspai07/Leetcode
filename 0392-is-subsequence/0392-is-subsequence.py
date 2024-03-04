class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = 0

        if not s:
            return True

        for char in t:

            if s[i] == char:
                i += 1
                if i == len(s):
                    return True
        return False

        