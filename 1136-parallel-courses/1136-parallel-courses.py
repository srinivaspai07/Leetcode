from collections import defaultdict, deque
from typing import List

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        adjList = defaultdict(list)
        inDegree = [0] * (n + 1)
        queue = deque()
        minSemester = 0
        
        # Correct adjacency list and in-degree array construction
        for v, u in relations:
            adjList[v].append(u)  # u depends on v, so v -> u
            inDegree[u] += 1       # Increase in-degree of u
        
        # Initialize the queue with courses having zero in-degree (no prerequisites)
        for index in range(1, n + 1):  # Iterate over 1 to n, not 0 to n
            if inDegree[index] == 0:
                queue.append(index)
        
        
        # Track the number of courses we can process
        coursesProcessed = 0
        
        # Process the graph using BFS
        while queue:
            # Increment the semester at the beginning of each "layer" of courses
            minSemester += 1
            
            # Process all courses that can be taken in the current semester
            for _ in range(len(queue)):
                preReq = queue.popleft()
                coursesProcessed += 1  # Count this course as processed
                
                # Process all its dependent courses (adjList[preReq])
                for req in adjList[preReq]:
                    inDegree[req] -= 1
                    if inDegree[req] == 0:  # If no more prerequisites, take this course next
                        queue.append(req)
        
        # If all courses are processed, return the number of semesters, otherwise return -1
        return minSemester if coursesProcessed == n else -1

