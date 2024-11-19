import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        freshOrange = 0
        queue = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Step 1: Count fresh oranges and add all rotten oranges to the queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    freshOrange += 1  # Count fresh oranges
                elif grid[i][j] == 2:
                    queue.append((i, j))  # Add all initially rotten oranges to the queue

        # Step 2: BFS to propagate the rotting process
        minutes = 0
        while queue and freshOrange > 0:
            minutes += 1  # Increment time at the start of each minute
            for _ in range(len(queue)):  # Process all rotten oranges at the current level
                i, j = queue.popleft()
                
                for dr, dc in directions:
                    newR, newC = i + dr, j + dc

                    # Only process valid fresh oranges that can be turned rotten
                    if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == 1:
                        grid[newR][newC] = 2  # Turn fresh orange to rotten
                        queue.append((newR, newC))  # Add the newly rotten orange to the queue
                        freshOrange -= 1  # Decrease count of fresh oranges

        # Step 3: Return the result, if all fresh oranges have rotted
        return minutes if freshOrange == 0 else -1
