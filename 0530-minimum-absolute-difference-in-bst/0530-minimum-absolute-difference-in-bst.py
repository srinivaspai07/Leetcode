# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.min_diff = float('inf')
        self.prev_val = None
        
        # In-order DFS function
        def inorder(node):
            if not node:
                print(f"leaf node")
                return
            
            # Traverse left subtree
            inorder(node.left)
            
            # Process current node
            if self.prev_val is not None:
                print(f"computing diff abs {node.val}  {self.prev_val}")
                self.min_diff = min(self.min_diff, abs(node.val - self.prev_val))
            if self.prev_val is not None:
                print(f"prev val is {self.prev_val} and current val is {node.val} and min is {self.min_diff}")
            # Update previous node value
            self.prev_val = node.val
            
            # Traverse right subtree
            inorder(node.right)
        
        # Start in-order traversal
        inorder(root)
        
        return self.min_diff
