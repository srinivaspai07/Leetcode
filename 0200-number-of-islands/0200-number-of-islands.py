class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        numberIslands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            
            grid[r][c] = "2"
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    numberIslands += 1
        
        return numberIslands
        
"""
        rows, cols = len(grid), len(grid[0])

        visited = set()
        islands = 0
        queue = collections.deque()

        def bfs(r, c):
            queue.append((r, c))

            while queue:
                r, c = queue.popleft()
                directions = [[0, 1], [-1, 0], [1, 0], [0, -1]]
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == '1' and (new_r, new_c) not in visited:
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands
"""
