class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1
        result = []
        
        def dfs(u, v, path):
            path.append(u)
            if u == v:
                result.append(path[:])  # Make a copy of the current path
            else:
                for neighbour in graph[u]:
                    dfs(neighbour, v, path)
            path.pop()  # Backtrack: remove the last node from the path
        
        dfs(0, n, [])
        return result
