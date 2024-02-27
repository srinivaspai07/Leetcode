class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        checkOpen = {'(': ')', '[': ']', '{': '}'}
        res = 1

        for char in s:
            if char in checkOpen:
                stack.append(char)
            else:
                if not stack:  # If stack is empty, no corresponding opening bracket
                    return False
                prev = stack.pop()
                if checkOpen[prev] != char:  # Check if closing bracket matches the last opening bracket
                    return False

        return not stack  # Check if stack is empty after iterating through the string

