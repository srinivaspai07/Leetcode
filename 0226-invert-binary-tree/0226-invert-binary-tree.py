class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: If root is None, return None
        if root is None:
            return None
        
        # Swap the left and right subtrees of the current node
        root.left, root.right = root.right, root.left
        
        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root  # Return the root of the inverted tree
