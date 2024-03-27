class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # Initialize the diameter
        
        def findHeight(node):
            if not node:
                return 0
            
            left_height = findHeight(node.left)
            right_height = findHeight(node.right)
            
            # Update the diameter
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return the height of the subtree rooted at the current node
            return 1 + max(left_height, right_height)
        
        findHeight(root)
        return self.diameter
