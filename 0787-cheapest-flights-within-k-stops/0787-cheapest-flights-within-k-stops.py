from collections import defaultdict, deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # Build the graph as an adjacency list
        adjList = defaultdict(list)
        for u, v, p in flights:
            adjList[u].append((v, p))
        
        # Use BFS with a queue
        queue = deque([(src, 0, 0)])  # (currentNode, currentCost, currentStops)
        min_cost = [float('inf')] * n
        min_cost[src] = 0
        
        # Perform BFS until we exhaust all possible paths within k stops
        while queue:
            currentNode, currentCost, currentStops = queue.popleft()
            
            # If we have used more stops than allowed, skip
            if currentStops > k:
                continue
            
            # Explore neighbors
            for neighbor, price in adjList[currentNode]:
                newCost = currentCost + price
                
                # Only proceed if the new path is cheaper
                if newCost < min_cost[neighbor]:
                    min_cost[neighbor] = newCost
                    queue.append((neighbor, newCost, currentStops + 1))
        
        # Return the cheapest cost to the destination within k stops
        return -1 if min_cost[dst] == float('inf') else min_cost[dst]
