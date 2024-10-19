from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return
        
        rows, cols = len(rooms), len(rooms[0])
        queue = collections.deque()
        
        for i in range(rows):
            for j in range(cols):
                
                if rooms[i][j] == 0:
                    queue.append((i,j,0))
        
        directions = [[-1,0],[0,1],[1,0],[0,-1]]
        visited = set()
        
        while queue:
            
            for _ in range(len(queue)):
                
                i,j,distance = queue.popleft()
                
                visited.add((i,j))
                
                if rooms[i][j] == 2147483647:
                    rooms[i][j] = distance            
        
                for dr,dc in directions:
            
                    newR, newC = i + dr, j + dc
            
                    if 0 <= newR < rows and 0 <= newC < cols and rooms[newR][newC] == 2147483647 and (newR,newC) not in visited:
                        queue.append((newR,newC,distance+1))
        
        return rooms
                
                

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
"""        
        
        
        rows = len(rooms)
        cols = len(rooms[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Find gates and initialize the queue with them
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        while queue:
            row, col = queue.popleft()
            distance = rooms[row][col] + 1  # Distance to be filled in adjacent cells
            print(distance)

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and rooms[new_row][new_col] == 2147483647:
                    rooms[new_row][new_col] = distance
                    queue.append((new_row, new_col))

        return
"""