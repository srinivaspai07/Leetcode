from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Construct graph using adjacency list representation
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        #print(graph)

        # Perform BFS traversal
        return self.bfs(source, destination, graph)

    def bfs(self, source, destination, graph):
        # Initialize queue and visited set
        queue = deque([source])
        visited = set([source])

        # Perform BFS
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
            

        return False
        
"""
this is adjacency matrix... this solution will not run completely becuase of memory limit issues...

        # Construct adjacency matrix representation of the graph
        graph = [[0] * n for _ in range(n)]
        for u, v in edges:
            graph[u][v] = 1
            graph[v][u] = 1
        
        # Perform DFS to check for a valid path from source to destination
        visited = set()
        return self.dfs(source, destination, graph, visited)
    
    def dfs(self, node, destination, graph, visited):
        # If the current node is the destination, return True
        if node == destination:
            return True
        
        # Mark the current node as visited
        visited.add(node)
        
        # Iterate through the neighbors of the current node
        for neighbour in range(len(graph[node])):
            print(neighbour)
            # If there is a connection to the neighbour and it has not been visited, recursively call dfs on it
            if graph[node][neighbour] == 1 and neighbour not in visited:
                if self.dfs(neighbour, destination, graph, visited):
                    return True
        
        # If no valid path is found from the current node, return False
        return False
"""

"""
this approach terminates recursion as soon as node is found

        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def dfs(u, destination):

            if u == destination:
                return True
            
            visited.add(u)

            for neighbour in graph[u]:
                print(f"we are now in {graph[u]} and checking {neighbour} and u is {u}")

                if neighbour not in visited:
                    if dfs(neighbour, destination):
                        return True
            
            return False

        return dfs(source, destination)
"""
""" 
in this approach, even after we find destination node, it will continue the recursion which may not be efficient 

        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        self.result = False

        def dfs(u, destination):

            if u == destination:
                self.result = True
                return 
            
            visited.add(u)

            for neighbour in graph[u]:
                print(f"we are now in {graph[u]} and checking {neighbour} and u is {u}")

                if neighbour not in visited:
                    if dfs(neighbour, destination):
                        self.result = True
                        #return True
            
            #return False

        dfs(source, destination)
        return self.result
"""