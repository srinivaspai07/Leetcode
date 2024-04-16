# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        maximum = float("-inf")
        def dfs(node):
            
            nonlocal maximum
            if not node:
                return 0
            
            left = max(0,dfs(node.left))
            right = max(0,dfs(node.right))
            #print(f"max is  {maximum} and the val is {left+right+node.val}")
            maximum = max(maximum,left+right+node.val)
            return (max(left+node.val,right+node.val))

        dfs(root)
        return maximum