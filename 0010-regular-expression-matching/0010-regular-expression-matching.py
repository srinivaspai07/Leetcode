class Solution:
    def isMatch(self, s, p):
        # Create a DP table initialized to False
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Base case: both empty string and pattern match
        dp[0][0] = True
        
        # Handle patterns like "a*", "b*", etc. for empty string cases
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (p[j - 2] == '.' or p[j - 2] == s[i - 1]))
        
        return dp[-1][-1]

