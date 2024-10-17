class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        enclaves = 0
        
        def dfs(i,j):
            
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
                return
        
            
            grid[i][j] = 0
            
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i,j-1)
            
            
        for i in range(cols):
            if grid[0][i] == 1:
                dfs(0,i)
        
        for i in range(cols):
            if grid[rows-1][i] == 1:
                dfs(rows-1,i)
    
            
        for i in range(rows):
            if grid[i][0] == 1:
                dfs(i,0)
        
        for i in range(rows):
            if grid[i][cols-1] == 1:
                dfs(i,cols-1)
        
        
        for row in grid:
            enclaves += sum(row)
        
        return enclaves
