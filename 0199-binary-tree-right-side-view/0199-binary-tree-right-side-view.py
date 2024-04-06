# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return
        
        res = []
        queue = collections.deque()
        queue.append(root)

        def bfs(node):

            while queue:

                length = len(queue)
                for i in range(len(queue)):

                    currentNode = queue.popleft()

                    if currentNode.left:
                        queue.append(currentNode.left)
                    if currentNode.right:
                        queue.append(currentNode.right)
            
                    if (i == (length -1)):
                        res.append(currentNode.val)
        bfs(root)
        return res
            
            
        