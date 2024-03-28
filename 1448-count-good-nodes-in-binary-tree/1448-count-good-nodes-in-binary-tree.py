class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.nodes = 0 
        
        def search(node, max_value):
            if not node:
                return
            
            if node.val >= max_value:
                self.nodes += 1
                max_value = node.val
            
            search(node.left, max_value)
            search(node.right, max_value)
        
        search(root, float('-inf'))  # Start with negative infinity as the initial max_value
        return self.nodes
