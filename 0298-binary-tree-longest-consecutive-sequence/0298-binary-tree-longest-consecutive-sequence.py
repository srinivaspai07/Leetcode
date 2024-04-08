# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        if not root:
            return
        
        maxValue = 1

        def dfs(node,prev_value,length):

            nonlocal maxValue
            if not node:
                return

            if prev_value is not None and (node.val - prev_value == 1):
                length += 1
                maxValue = max(maxValue,length)
            else:
                length = 1

            dfs(node.left,node.val,length)
            dfs(node.right,node.val,length)
        
        dfs(root,None,maxValue)
        return maxValue


"""
        def dfs(node, parent_val, length):
            if not node:
                return length
            current_length = length + 1 if node.val == parent_val + 1 else 1
            return max(current_length, dfs(node.left, node.val, current_length), dfs(node.right, node.val, current_length))

        def helper(root):
            if not root:
                return 0
            return max(dfs(root.left, root.val, 1), dfs(root.right, root.val, 1))
        
        return helper(root)
"""