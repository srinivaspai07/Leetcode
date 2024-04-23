class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        self.max = 0

        def dfs(r,c):

            #print(f"point i {r} and {c}")
            if r == rows or r < 0 or c <0 or c == cols or grid[r][c] != 1:
                print(f"NO point i {r} and {c}")

                return 0
        
            grid[r][c] =2
            #"""  
            #both the ways are exact same... the way recursion works too is exact same..

            return (1 + dfs(r,c+1) + 
                dfs(r+1,c) +
                dfs(r-1,c) +
                dfs(r,c-1)
            )
            """
            right = dfs(r, c + 1)
            down = dfs(r + 1, c)
            up = dfs(r - 1, c)
            left = dfs(r, c - 1)
    
            return 1 + right + down + up + left
            """
        #print(f"end so count is {r} and {c}")
        #self.max = max(self.max,count)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    print("new points")
                    count = dfs(i,j)
                    self.max = max(self.max,count)

        
        return self.max
"""

BFS SOLUTION

from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        
        def bfs(r, c):
            area = 0
            queue = deque([(r, c)])
            while queue:
                row, col = queue.popleft()
                if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != 1:
                    continue
                grid[row][col] = 2  # Mark as visited
                area += 1
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    queue.append((row + dr, col + dc))
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, bfs(i, j))
        
        return max_area
"""