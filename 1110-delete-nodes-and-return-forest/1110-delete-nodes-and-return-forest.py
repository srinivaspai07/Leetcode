class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = []  # List to store final results

        if not root:
            return result

        # Helper function to perform DFS traversal and construct forest
        def dfs(node, is_root):
            if not node:  # Base case: empty node
                return None

            # Check if current node needs to be deleted
            delete_node = node.val in to_delete

            # If current node is a root of a new tree, add it to result
            if is_root and not delete_node:
                result.append(node)

            # Traverse left and right subtrees
            node.left = dfs(node.left, delete_node)
            node.right = dfs(node.right, delete_node)

            # If current node needs to be deleted, return None
            return None if delete_node else node

        # Start DFS traversal from the root
        dfs(root, True)
        return result
