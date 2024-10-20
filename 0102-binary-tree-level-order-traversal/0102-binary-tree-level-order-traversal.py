# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        if not root:
            return []
    
        queue = collections.deque()
        queue.append(root)
        results = []
        
        while queue:
            
            temp = []
            
            for _ in range(len(queue)):
                
                node = queue.popleft()
                temp.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            results.append(temp)
        
        return results
                

        
"""        
        if root is None:
            return ans
        q = collections.deque()
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans
"""

                