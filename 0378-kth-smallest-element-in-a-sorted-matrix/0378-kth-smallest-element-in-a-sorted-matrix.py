class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        if not matrix:
            return
        
        minHeap = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):

                heapq.heappush(minHeap,-matrix[i][j])
                while len(minHeap) > k:
                    heapq.heappop(minHeap)
        return(-minHeap[0])
