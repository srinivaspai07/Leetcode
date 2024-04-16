class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque([(0, 0)])
        grid[0][0] = -1  # Mark the starting cell as visited
        
        path_length = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return path_length
                
                for dr, dc in [[0, 1], [1, 0], [1, 1], [0, -1], [-1, 0], [-1, 1], [-1, -1], [1, -1]]:
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 0: #this is a way to avoid using range function i.e new_r in range(rows)
                        queue.append((new_r, new_c))
                        grid[new_r][new_c] = -1  # Mark the cell as visited
            path_length += 1
        
        return -1
""" for the above solution, this queue logic can also be used

while queue:
    r, c, path = queue.popleft()

    if r == rows - 1 and c == cols - 1 and grid[r][c] == 0:
        return path + 1
    directions = [[0, 1], [1, 0], [1, 1], [0, -1], [-1, 0], [-1, 1], [-1, -1], [1, -1]]
    for dr, dc in directions:
        new_r, new_c = r + dr, c + dc 
        if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited and grid[new_r][new_c] == 0:
            visited.add((new_r, new_c))
            queue.append((new_r, new_c, path + 1))
"""
"""

my soltion which also works but not super optimized

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return -1
        
        rows = len(grid)
        cols = len(grid[0]) 

        if grid[0][0] != 0 or grid[rows-1][cols-1] != 0:
            return -1
        
        #def bfs(source):

        queue = collections.deque()
        queue.append((0,0,0))
        visited = set()
        visited.add((0,0))

        while queue:

            r,c,path = queue.popleft()

            if r == rows-1 and c == cols-1 and grid[r][c] == 0:
                #print("hi")
                return path+1
            directions = [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,1],[-1,-1],[1,-1]]
            for dr,dc in directions:
                new_r, new_c = r + dr, c + dc 
                #print(f"considering new row {new_r} and new col {new_c} and type of {type(grid[new_r][new_c])} and val is {grid[new_r][new_c]}")
                if new_r in range(rows) and new_c in range(cols) and (new_r,new_c) not in visited and grid[new_r][new_c] == 0:
                    print(f"adding new row {new_r} and new col {new_c}")
                    visited.add((new_r,new_c))
                    queue.append((new_r,new_c,path+1))
        
        return -1

"""