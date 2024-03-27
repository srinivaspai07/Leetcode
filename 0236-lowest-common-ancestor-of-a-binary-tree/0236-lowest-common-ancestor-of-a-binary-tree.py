# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return None #not really needed as problem says all nodes are present
        
        # Base case: if root is either p or q, return root
        if  (root == p or root == q):
            return root
        
        # Recur on left and right subtrees
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)
        
        
        # If both left and right subtrees return non-None values, then root is the LCA
        if left_lca and right_lca:
            return root
        
        # If only one subtree returns a non-None value, return that value (potential LCA)
        return left_lca if left_lca else right_lca
