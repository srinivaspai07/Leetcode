# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if not root:
            
            return 
        
        self.queue = collections.deque()
        self.queue.append(root)
        
        self.average = []
        
        def bfs(node):
            
            while self.queue:
                
                summation = 0
                
                for i in range(len(self.queue)):
                    
                    currentNode = self.queue.popleft()
                    summation += currentNode.val

                    if currentNode.left:
                        self.queue.append(currentNode.left)
                        
                    if currentNode.right:
                        self.queue.append(currentNode.right)
                    
                self.average.append((summation)/(i+1))
        
        bfs(root)
        return self.average