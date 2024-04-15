class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        found_path = [False]  # A list to hold the flag value

        def dfs(node, summation):
            if not node or found_path[0]:
                if node:
                    print(f"node now is {node.val}")  # If found_path is True, stop recursion
                return found_path[0]
            
            #print(node.val)
            summation += node.val
            
            # Check if it's a leaf node and if the summation equals the targetSum
            if not node.left and not node.right and summation == targetSum:
                found_path[0] = True  # Set the flag to True
                return True
            
            # Explore the left subtree
            left_result = dfs(node.left, summation)
            # Explore the right subtree
            right_result = dfs(node.right, summation)
            
            # Return True if either left_result or right_result is True
            return left_result or right_result
            
        return dfs(root, 0)
"""

working solution

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        check = False  # A boolean variable to track whether a path with the target sum has been found

        def dfs(node, summation):
            nonlocal check  # Declare check as nonlocal
            if not node or check:  # If check is True, stop recursion
                return
            
            summation += node.val
            
            # Check if it's a leaf node and if the summation equals the targetSum
            if not node.left and not node.right and summation == targetSum:
                check = True  # Set the flag to True
                return
            
            # Explore the left subtree
            dfs(node.left, summation)
            # Explore the right subtree
            dfs(node.right, summation)
            
        dfs(root, 0)
        return check  # Return the flag value
"""