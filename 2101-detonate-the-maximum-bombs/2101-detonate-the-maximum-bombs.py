class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        def canDetonate(bomb1,bomb2):
            x1,y1,r1 = bomb1
            x2,y2,r2  = bomb2
            return (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r1 ** 2

        graph = collections.defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i!=j and canDetonate(bombs[i],bombs[j]):
                    graph[i].append(j)
        
        queue = collections.deque()

        def bfs(i):

            visited = set() #this is written here intentionally so that each time visited is a new set
            queue.append(i)
            visited.add(i)
            maxDetonate = 1

            while queue:

                node = queue.popleft()

                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
                        maxDetonate += 1
            return maxDetonate

        maxDetonate = float("-inf")

        for i in range(len(bombs)):
            
            maxDetonate = max(maxDetonate,bfs(i))
        
        return maxDetonate

