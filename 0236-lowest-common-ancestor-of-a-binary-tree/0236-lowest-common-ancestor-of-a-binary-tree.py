# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # Define the dfs function
        def dfs(node):
            # Base case: If the current node is None, or matches p or q, return the node
            if not node or node == p or node == q:
                return node
            
            # Recur for the left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If both left and right are non-null, this node is the LCA
            if left and right:
                return node
            
            # If only one side has a non-null result, propagate that upwards
            return left if left else right
        
        # Call the dfs function starting from the root
        return dfs(root)
