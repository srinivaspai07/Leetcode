# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        
        res = 0

        def dfs(node,carry):

            nonlocal res
            if not node:
                return 
            carry = node.val + carry*10
            print(carry)
            if node.left == None and node.right == None:
                res += carry
            
            dfs(node.left,carry)
            dfs(node.right,carry)

        dfs(root,0)
        return res
    
"""

wprking solution to stop recursion from making extra calls once leaf node is reached

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # Return 0 if the tree is empty
        
        res = 0

        def dfs(node, carry):
            nonlocal res
            
            carry = node.val + carry * 10
            
            if not node.left and not node.right:  # Check if it's a leaf node
                res += carry
                return
            
            if node.left:
                dfs(node.left, carry)
            
            if node.right:
                dfs(node.right, carry)

        dfs(root, 0)
        return res
"""