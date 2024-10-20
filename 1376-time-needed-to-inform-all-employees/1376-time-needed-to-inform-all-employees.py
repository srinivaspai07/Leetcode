from collections import defaultdict, deque
from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Create adjacency list
        adjList = defaultdict(list)
        
        for reportee in range(len(manager)):
            if manager[reportee] != -1:  # Do not add the head (who has no manager)
                adjList[manager[reportee]].append(reportee)
        
        # BFS Queue to process employees, starting with head (with accumulated inform time 0)
        queue = deque([(headID, 0)])
        maxTime = 0
        
        while queue:
            emp, currentTime = queue.popleft()
            # Update the max time required to inform everyone
            maxTime = max(maxTime, currentTime)
            
            # Traverse the direct reportees of the current employee
            for neigh in adjList[emp]:
                queue.append((neigh, currentTime + informTime[emp]))  # Add the accumulated time for each reportee
        
        return maxTime
