from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder_traversal(node, prev, min_diff):
            if not node:
                return min_diff, prev
            
            min_diff, prev = inorder_traversal(node.left, prev, min_diff)
            if prev is not None:
                min_diff = min(min_diff, abs(node.val - prev))

            prev = node.val
            min_diff, prev = inorder_traversal(node.right, prev, min_diff)
            
            return min_diff, prev
        
        min_diff, _ = inorder_traversal(root, None, float('inf'))
        return min_diff
