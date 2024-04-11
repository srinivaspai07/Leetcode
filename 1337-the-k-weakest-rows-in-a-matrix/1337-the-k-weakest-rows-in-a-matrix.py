class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        if not mat: 
            return
        
        rows, cols = len(mat),len(mat[0])

        if k > rows:
            return

        self.minHeap = []
        self.res = []

        for i in range((rows)):

            count = 0

            for j in range((cols)):

                if mat[i][j] == 1:
                    count += 1

            heapq.heappush(self.minHeap,(-count,-i))
            
            if len(self.minHeap) > k:
                heapq.heappop(self.minHeap)
        
        
        for _ in range(len(self.minHeap)):

            count,row = heapq.heappop(self.minHeap)
            #print(f"count is {-count} and val is {row}")
            self.res.append(-row)

        return self.res[::-1]
