from collections import deque

class Solution:
    def shortestBridge(self, grid):
        def get_neighbors(i, j):
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    yield ni, nj

        def dfs(i, j):
            visited.add((i, j))
            island.add((i, j))
            for ni, nj in get_neighbors(i, j):
                if grid[ni][nj] == 1 and (ni, nj) not in visited:
                    dfs(ni, nj)

        def bfs():
            queue = deque(island)
            level = 0
            while queue:
                size = len(queue)
                for _ in range(size):
                    i, j = queue.popleft()
                    for ni, nj in get_neighbors(i, j):
                        if (ni, nj) in other_island:
                            return level
                        if (ni, nj) not in visited:
                            visited.add((ni, nj))
                            queue.append((ni, nj))
                level += 1

        n = len(grid)
        visited = set()
        island = set()
        other_island = set()

        # Find the first island using DFS
        found_island = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    if not found_island:
                        dfs(i, j)
                        found_island = True
                    else:
                        other_island.add((i, j))

        # Use BFS to find the shortest bridge
        return bfs()
