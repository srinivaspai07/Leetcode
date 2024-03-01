from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        num_special = 0
        rows = len(mat)
        cols = len(mat[0])

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    # Check if all other elements in row i are 0
                    row_sum = sum(mat[i])
                    # Check if all other elements in column j are 0
                    col_sum = sum(mat[r][j] for r in range(rows))

                    if row_sum == 1 and col_sum == 1:
                        num_special += 1

        return num_special
