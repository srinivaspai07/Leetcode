from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 1)])  # Initialize the queue with the root and its depth
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:  # Check if it's a leaf node
                return depth
            if node.left:  # Add left child to the queue
                queue.append((node.left, depth + 1))
            if node.right:  # Add right child to the queue
                queue.append((node.right, depth + 1))
