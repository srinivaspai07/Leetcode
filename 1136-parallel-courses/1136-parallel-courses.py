class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        adjList = defaultdict(list)
        inDegree = [0] * (n +1)
        queue = collections.deque()
        minSemester =0
        
        for u,v in relations:
            adjList[u].append(v)
            inDegree[v] += 1
        
        
        for index,value in enumerate(inDegree):
            if index ==0:
                continue
            if value == 0:
                queue.append(index)
        print(inDegree)
        print(adjList)
        print(queue)
        
        while queue:
            
            for _ in range(len(queue)):
                
                preReq = queue.popleft()
                
                for req in adjList[preReq]:
                    inDegree[req] -= 1
                    if inDegree[req] == 0:
                        queue.append(req)
                        
            minSemester += 1
            
        
        print()
        return minSemester if sum(inDegree) == 0 else -1