class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def get_leaf_values(root,leaf):
            if not root:
                return 

            if not root.left and not root.right:
                leaf.append(root.val)
                return [root.val]
            get_leaf_values(root.left,leaf)
            get_leaf_values(root.right,leaf)
          
        leaf1, leaf2 = [],[]
        get_leaf_values(root1,leaf1)
        get_leaf_values(root2,leaf2)
        
        return leaf1 == leaf2
