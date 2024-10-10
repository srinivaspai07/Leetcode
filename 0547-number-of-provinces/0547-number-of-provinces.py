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

    
# this is a good problem
# this is not a grid traversal problem
# here, the graph is given as adjacency matrix and this problem teaches us how to traverse adjancy matrix

# for added info, if the input was given as adjacency list instead of matrix, below would be the solution

def findCircleNum(adj_list):
    # Number of cities
    n = len(adj_list)
    
    # To track visited cities
    visited = set()
    provinces = 0

    # DFS to mark all connected cities
    def dfs(city):
        for neighbor in adj_list[city]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)

    # Visit each city and run DFS if not visited
    for city in range(n):
        if city not in visited:
            visited.add(city)  # Mark city as visited
            dfs(city)          # Visit all cities in this province
            provinces += 1     # Increment province count

    return provinces
