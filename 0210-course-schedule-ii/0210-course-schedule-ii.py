from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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

