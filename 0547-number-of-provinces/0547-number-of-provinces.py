class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:        
        n = len(isConnected)
        visited = set()  # Track whether each city has been visited
        provinces = 0

        # DFS function to visit all cities in the same province
        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)  # Mark as visited
                    dfs(neighbor)  # Recursively visit all its neighbors

        # Loop over all cities and run DFS for unvisited cities
        for city in range(n):
            if city not in visited:
                visited.add(city)  # Mark city as visited
                dfs(city)  # Visit all cities in this province
                provinces += 1  # Count this as one province

        return provinces
