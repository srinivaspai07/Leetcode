class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # Function to compute the left boundary of the binary tree
        def left_boundary(root):
            if not root or (not root.left and not root.right):
                return
            boundary.append(root.val)
            if root.left:
                left_boundary(root.left)
            else:
                left_boundary(root.right)

        # Function to compute the right boundary of the binary tree
        def right_boundary(root):
            if not root or (not root.left and not root.right):
                return
            if root.right:
                right_boundary(root.right)
            else:
                right_boundary(root.left)
            boundary.append(root.val)

        # Function to compute the leaves of the binary tree
        def leaves(root):
            if not root:
                return
            if not root.left and not root.right:
                boundary.append(root.val)
                return
            leaves(root.left)
            leaves(root.right)

        boundary = [root.val]
        
        # Compute left boundary (excluding root)
        left_boundary(root.left)
        
        # Compute leaves (excluding left and right boundaries)
        leaves(root.left)
        leaves(root.right)
        
        # Compute right boundary (excluding root)
        right_boundary(root.right)
        
        return boundary
