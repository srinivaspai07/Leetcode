from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        if not matrix:
            return result
        
        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows - 1, 0, cols - 1
        
        while top <= bottom and left <= right:
            # Traverse top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            # Traverse right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            # Check if we have traversed all rows or columns
            if top <= bottom:
                # Traverse bottom row
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                # Traverse left column
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result

