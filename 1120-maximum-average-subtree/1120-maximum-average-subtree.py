class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        if not root:
            return 0
        
        max_avg = float("-inf")  # Initialize the maximum average
        
        def dfs(node):
            nonlocal max_avg
            
            if not node:
                return 0, 0  # Return sum and count as a tuple
            
            # Calculate the sum and count of values in the left subtree
            left_sum, left_count = dfs(node.left)
            # Calculate the sum and count of values in the right subtree
            right_sum, right_count = dfs(node.right)
            
            # Calculate the sum and count of values in the current subtree
            subtree_sum = left_sum + right_sum + node.val
            subtree_count = left_count + right_count + 1  # Add 1 for the current node
            
            # Calculate the average of the current subtree
            subtree_avg = subtree_sum / subtree_count
            
            # Update the maximum average if the current subtree average is greater
            max_avg = max(max_avg, subtree_avg)
            
            # Return the sum and count of values in the current subtree
            return subtree_sum, subtree_count
        
        # Start DFS traversal from the root
        dfs(root)
        
        return max_avg
