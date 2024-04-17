class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def closest_helper(node, closest):
            if not node:
                return closest
            closest = min(node.val, closest, key=lambda x: (abs(target - x), x))
            if target < node.val:
                return closest_helper(node.left, closest)
            elif target > node.val:
                return closest_helper(node.right, closest)
            else:
                return closest
        
        return closest_helper(root, root.val)
