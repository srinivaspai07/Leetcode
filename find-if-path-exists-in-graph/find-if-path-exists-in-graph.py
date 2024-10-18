from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
 

        graph = defaultdict(list)
    
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        
        def dfs(node, destination):
            
            if node == destination:
                return True
            
            visited.add(node)
            
            for neighbour in graph[node]:
                if neighbour not in visited:
                    if dfs(neighbour,destination):
                        return True
            
            return False
        
        res = dfs(source,destination)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       