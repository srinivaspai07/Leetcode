class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def get_leaf_nodes(node, leaf_nodes):
            if node is None:
                return

            if node.left is None and node.right is None:
                leaf_nodes.append(node.val)

            get_leaf_nodes(node.left, leaf_nodes)
            get_leaf_nodes(node.right, leaf_nodes)

        leaf_nodes1 = []
        leaf_nodes2 = []

        get_leaf_nodes(root1, leaf_nodes1)
        get_leaf_nodes(root2, leaf_nodes2)

        return leaf_nodes1 == leaf_nodes2
