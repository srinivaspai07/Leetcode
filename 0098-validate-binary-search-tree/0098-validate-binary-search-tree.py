# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(node,min_val,max_val):

            if not node:
                return True
            
            if min_val >= node.val or node.val >= max_val:
                return False
            
            left = check(node.left,min_val,node.val)
            right = check(node.right,node.val,max_val)

            result = left and right
            return result


        return( check(root,float(-inf),float(inf)))

"""
Alternatively: this is a better solution as it stops the recursion when we get False and propagates upwards

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkBST(node, min_val, max_val):
            if not node:
                return True
            
            if not (min_val < node.val < max_val):
                return False
            
            return (checkBST(node.left, min_val, node.val) and
                    checkBST(node.right, node.val, max_val))

        return checkBST(root, float('-inf'), float('inf'))
"""