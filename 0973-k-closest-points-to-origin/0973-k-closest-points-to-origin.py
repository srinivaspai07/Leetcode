class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #compute distance of each co-ordinates from origin and push to max heap
        # when max heap reaches k, pop

        max_heap = []

        for point in points:
            distance = math.sqrt(((point[0] - 0)**2) + ((point[1] - 0)**2)) 
            
            heapq.heappush(max_heap,(-distance,point[0],point[1]))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        result = []
        for point in max_heap:
            result.append([point[1],point[2]])
        return result