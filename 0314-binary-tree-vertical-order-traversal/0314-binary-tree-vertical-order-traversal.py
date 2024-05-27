# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return 
        
        self.result = collections.defaultdict(list)
        self.queue = collections.deque()
        self.queue.append((root,0))
        
        while self.queue:
            
            for _ in range(len(self.queue)):
                
                node,verticalOrder = self.queue.popleft()
                
                if node.left:
                    self.queue.append((node.left,verticalOrder-1))
                
                if node.right:
                    self.queue.append((node.right,verticalOrder+1))
                
                self.result[verticalOrder].append(node.val)
        
        keys = sorted(self.result.keys())
        self.res = []
        
        for key in keys:
            self.res.append(self.result[key])
        
        
        return(self.res)
        
                
        
        