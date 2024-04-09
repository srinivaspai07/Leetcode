from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])
        level = 0

        while queue:
            prev_val = None

            # Determine whether the current level should be increasing or decreasing
            if level % 2 == 0:  # Even level (odd-indexed)
                increasing = True
            else:  # Odd level (even-indexed)
                increasing = False

            level_length = len(queue)

            for _ in range(level_length):
                node = queue.popleft()

                # Check if the value meets the conditions
                if (level % 2 == 0 and (node.val % 2 == 0 or (prev_val is not None and node.val <= prev_val))) \
                        or (level % 2 == 1 and (node.val % 2 != 0 or (prev_val is not None and node.val >= prev_val))):
                    return False

                # Update prev_val for the next iteration
                prev_val = node.val

                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Increment the level after processing each level
            level += 1

        return True
