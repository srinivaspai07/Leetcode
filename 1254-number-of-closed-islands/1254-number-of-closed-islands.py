class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        self.rows = len(grid)
        self.cols = len(grid[0])
        self.numIslands = 0

        def dfs(r,c):

            if not (0 <= r < self.rows and 0 <= c < self.cols):  # Check if out of bounds
                return 0
            if grid[r][c] != 0:
                return 1
            
            grid[r][c] = 2  # Marking as visited

            # Explore neighbors
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)

            # If any neighbor returns 0 (indicating it's not a closed island)
            # then this island is not closed
            return min(up, down, left, right)


        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 0:
                    if dfs(i,j):
                        self.numIslands += 1

        
        return self.numIslands


