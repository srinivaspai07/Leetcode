class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        adjList = defaultdict(list)
        
        for index,value in enumerate(graph):
            adjList[index].append(value)
        
        results = []
        visited = set()
        
        def dfs(node, destination, cur):
            
            if node == destination:
                cur.append(node)
                results.append(cur.copy())
                return
            
            cur.append(node)
            #visited.add(node)
            
            for neighbour in graph[node]:
                #if neighbour not in visited:
                dfs(neighbour,destination,cur)
                cur.pop()
        dfs(0,len(graph)-1,[])
        return results
                

                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
"""
        #working bfs sol

        n = len(graph) - 1
        result = []
        queue = collections.deque()
        queue.append((0, n, []))  # Initialize the queue with a tuple

        while queue:
            u, v, path = queue.popleft()
            path.append(u)  # Append the current node to the path

            if u == v:
                result.append(path[:])  # Make a copy of the current path when the destination node is reached
            else:
                for neighbor in graph[u]:
                    queue.append((neighbor, v, path[:]))  # Append neighbors with updated path
+
        return result
"""
"""
working dfs sol
        n = len(graph) - 1
        result = []
        
        def dfs(u, v, path):
            path.append(u)
            if u == v:
                result.append(path[:])  # Make a copy of the current path
                #path.pop()
            else:
                for neighbour in graph[u]:
                    dfs(neighbour, v, path)
            path.pop()  # Backtrack: remove the last node from the path
        
        dfs(0, n, [])
        return result
"""