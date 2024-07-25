from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        original_color = image[sr][sc]

        # If the original color is the same as the new color, no need to proceed
        if original_color == color:
            return image

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or image[i][j] != original_color:
                return

            image[i][j] = color

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        dfs(sr, sc)
        return image
