from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = defaultdict(list)
        inDegree = [0] * numCourses
        queue = collections.deque()
        results = []
        
        for u,v in prerequisites:
            adjList[u].append(v)
            inDegree[v] += 1
        
        if 0 not in inDegree:
            return results   
        
        for index,value in enumerate(inDegree):
            if value == 0:
                queue.append(index)
        
        
        while queue:
            
            crs = queue.popleft()
            results.append(crs)
            
            for neighbour in adjList[crs]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)
        
        return results[::-1] if len(results) == numCourses else [] #here i have reversed the code before of the way i have built the adjacency list
    # in the below code, adjacency list is built the other way around and thus, does not need any reversal at the end
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
"""        
        # Step 1: Build the adjacency list and in-degree array
        adjacencyList = defaultdict(list)
        inDegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            adjacencyList[prereq].append(course)
            inDegree[course] += 1
        
        # Step 2: Initialize the queue with courses having zero in-degree
        queue = deque()
        for course in range((numCourses)):
            if inDegree[course] == 0:
                queue.append(course)
        
        # Step 3: Perform topological sorting
        verticesVisited = []
        print(f"adj is {adjacencyList}")
        while queue:
            current = queue.popleft()
            verticesVisited.append(current)
            
            # Decrement the in-degree of each neighbor
            for neighbor in adjacencyList[current]:
                print(neighbor)
                inDegree[neighbor] -= 1
                # If the neighbor's in-degree becomes zero, add it to the queue
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: Check if all courses are included in the topological order
        if len(verticesVisited) == numCourses:
            return verticesVisited
        else:
            return []  # Cycle detected, return an empty list
            
"""

