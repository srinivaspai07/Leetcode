class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        rows, cols = len(board), len(board[0])
        
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != 'O':
                return
            
            board[row][col] = '#'  # Mark as visited
            
            # Explore 4 directions
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        # Traverse first and last rows
        for col in range(cols):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[rows - 1][col] == 'O':
                dfs(rows - 1, col)
        
        # Traverse first and last columns
        for row in range(rows):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][cols - 1] == 'O':
                dfs(row, cols - 1)
        
        # Flip 'O's to 'X's and revert '#' back to 'O's
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '#':
                    board[row][col] = 'O'
