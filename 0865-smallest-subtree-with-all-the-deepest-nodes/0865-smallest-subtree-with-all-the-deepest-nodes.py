class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return None
        
        self.result = None
        self.max_depth = float("-inf")
        
        def dfs(node, depth):
            
            if not node:
                return depth, None
            
            left_depth, left_node = dfs(node.left, depth + 1)
            right_depth, right_node = dfs(node.right, depth + 1)
            
            if left_depth == right_depth:
                return left_depth, node
            elif left_depth > right_depth:
                return left_depth, left_node
            else:
                return right_depth, right_node
        
        max_depth, self.result = dfs(root, 0)
        return self.result
