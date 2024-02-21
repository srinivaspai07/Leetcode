# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Initialize a dictionary to store the parent nodes of each node
        parent_map = {}
        
        
        def build_parent_map(node, parent=None):
            if node:
                parent_map[node] = parent
                build_parent_map(node.left, node)  
                build_parent_map(node.right, node) 
    
        # Function to perform depth-first search from the target node
        def dfs(node, distance):
            if not node:
                return
            if distance == k:
                result.append(node.val)
                return
            visited.add(node)
            if node.left and node.left not in visited:
                dfs(node.left, distance + 1)
            if node.right and node.right not in visited:
                dfs(node.right, distance + 1)
            if parent_map[node] and parent_map[node] not in visited:
                dfs(parent_map[node], distance + 1)
        
        # Initialize the result list
        result = []
        # Initialize a set to keep track of visited nodes
        visited = set()
        
        # Build the parent map of the tree
        build_parent_map(root)
        
        # Perform DFS from the target node
        dfs(target, 0)
        
        return result
