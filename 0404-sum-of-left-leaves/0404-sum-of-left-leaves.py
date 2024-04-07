# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        if not root.left and not root.right:
            return 0

        self.queue = collections.deque()
        self.queue.append([root,None])
        self.sum = 0

        def bfs():

            while self.queue:

                for _ in range(len(self.queue)):

                    currentNode,location = self.queue.popleft()

                    if currentNode.left == None and currentNode.right == None and location == 'l':
                        self.sum += currentNode.val
                    
                    if currentNode.left:
                        self.queue.append([currentNode.left,'l'])

                    if currentNode.right:
                        self.queue.append([currentNode.right,'r'])
                    
        bfs()
        return self.sum



        