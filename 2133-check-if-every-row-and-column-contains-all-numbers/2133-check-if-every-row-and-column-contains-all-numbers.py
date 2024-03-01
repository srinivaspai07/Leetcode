from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        # Check rows
        for row in matrix:
            if sorted(row) != list(range(1, n+1)):
                return False

        # Check columns
        for j in range(n):
            col = [matrix[i][j] for i in range(n)]
            if sorted(col) != list(range(1, n+1)):
                return False

        return True
"""

BETTER SOLUTION BELOW

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in matrix:
            if len(set(i))!= n:
                return False
        for i in zip(*matrix):
            if len(set(i))!= n:
                return False
        return True
"""