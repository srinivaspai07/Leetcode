class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def findMax(node, depth):
            if not node:
                return 0
            else:
                left_depth = findMax(node.left, depth + 1)
                right_depth = findMax(node.right, depth + 1)
                current_depth = max(left_depth, right_depth) + 1
                return current_depth
        
        return findMax(root, 0)
