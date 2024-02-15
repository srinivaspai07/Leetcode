class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        cur = root
        stack = []
        res = []

        while cur or stack:

            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        """
        res = []
        if root is None:
            return res  # Return an empty list for an empty tree
        
        # Traverse the left subtree
        res.extend(self.inorderTraversal(root.left))
        

        # Visit the current node
        res.append(root.val)
    
        # Traverse the right subtree
        res.extend(self.inorderTraversal(root.right))
        """
        return res
