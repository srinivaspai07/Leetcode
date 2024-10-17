class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        
        rows, cols = len(grid), len(grid[0])
        
        if grid[row][col] == color:
            return grid
        
        originalColor = grid[row][col]
        border = set()
        visited = set()
        
        def dfs(i, j):
            # Mark the cell as visited
            visited.add((i, j))
            
            # Check if it's a border cell
            isBorder = False
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                isBorder = True  # On the edge
            else:
                # Check if adjacent cells have different colors
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if grid[x][y] != originalColor:
                        isBorder = True
            
            if isBorder:
                border.add((i, j))
            
            # Explore neighboring cells if not visited
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < rows and 0 <= y < cols and (x, y) not in visited and grid[x][y] == originalColor:
                    dfs(x, y)
        
        # Start DFS
        dfs(row, col)
        
        # Change color of the border cells
        for i, j in border:
            grid[i][j] = color
        
        return grid
