# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        results = []
        
        def dfs(node, curr_path):
            #if not node:
             #   return
            
            # Add current node's value to the path
            curr_path.append(str(node.val))
            
            # If it's a leaf node, add the path to the results
            if not node.left and not node.right:
                # Join the path elements as a string with '->'
                results.append("->".join(curr_path))
            
            # Recursively call for left and right children
            if node.left: dfs(node.left, curr_path)
            if node.right: dfs(node.right, curr_path)
            
            # Backtrack: Remove the current node's value before returning to the previous node
            curr_path.pop()
        
        # Start DFS from the root with an empty path
        dfs(root, [])
        return results
