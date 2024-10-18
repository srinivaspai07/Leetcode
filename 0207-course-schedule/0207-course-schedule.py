class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        
        adjList = defaultdict(list)
        visited = set()
        
        for u, v in prerequisites:
            adjList[u].append(v)
        
        
        def dfs(crs):
            
            if crs in visited:
                return False
            
            if adjList[crs] == []:
                return True
            
            visited.add(crs)
            
            for neighbour in adjList[crs]:
                #print(f"first neighbour is {neighbour} and visited is {visited}")

                if not dfs(neighbour):
                    return False
            
            #print(f"neighbour is {neighbour} and visited is {visited} and crs is {crs}")
            visited.remove(crs)
            adjList[neighbour] = []
            
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

            
"""
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        preMap = {i: [] for i in range(numCourses)}

        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            print(f"visiting is {visiting}")
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            print(f"course is {crs} and visiting0 is {visiting}")
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        
"""