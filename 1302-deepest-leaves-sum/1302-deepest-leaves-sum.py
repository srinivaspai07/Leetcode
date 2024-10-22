# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        depth = 0
        summation = 0
        
        def findDepth(node,localDepth):
            nonlocal depth
            if not node:
                return 0
            
            depth = max(depth,localDepth)
            
            findDepth(node.left,localDepth+1)
            findDepth(node.right,localDepth+1)
        
        
        def findSum(node,localDepth):
            nonlocal summation
            if not node:
                return
            
            if localDepth == depth:
                summation += node.val
            
            findSum(node.left,localDepth+1)
            findSum(node.right,localDepth+1)
            
        findDepth(root,0)
        findSum(root,0)
        
        return summation
            
            
            
        