class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkTree(p, q):
            if not p and not q:             
               return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            left_same = checkTree(p.left, q.left)
            right_same = checkTree(p.right, q.right)
            
            if not left_same or not right_same:
                return False
            return True

        return checkTree(p, q)
