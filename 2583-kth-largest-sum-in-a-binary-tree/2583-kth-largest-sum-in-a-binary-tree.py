# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root:
            return
        
        self.queue = collections.deque()
        self.queue.append(root)
        self.minHeap = []

        def bfs():
            
            while self.queue:
            
                self.sum = 0

                for _ in range(len(self.queue)):
                    
                    currentNode = self.queue.popleft()
                
                    self.sum += currentNode.val
                
                    if currentNode.left:
                        self.queue.append(currentNode.left)
            
                    if currentNode.right:
                        self.queue.append(currentNode.right)
                    
                heapq.heappush(self.minHeap,self.sum)
            
                if len(self.minHeap) > k:
                    heapq.heappop(self.minHeap)
                
        bfs()
        return -1 if (len(self.minHeap) < k) else  self.minHeap[0]
                    
                    
        