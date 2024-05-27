# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in range(min_column, max_column + 1)]
"""
working solution but time complexity is O (n log n) due to sorting

        if not root:
            return 
       
        self.result = collections.defaultdict(list)
        self.queue = collections.deque()
        self.queue.append((root,0))
        
        while self.queue:
            
            for _ in range(len(self.queue)):
                
                node,verticalOrder = self.queue.popleft()
                
                if node.left:
                    self.queue.append((node.left,verticalOrder-1))
                
                if node.right:
                    self.queue.append((node.right,verticalOrder+1))
                
                self.result[verticalOrder].append(node.val)
        
        keys = sorted(self.result.keys())
        self.res = []
        
        for key in keys:
            self.res.append(self.result[key])
        
        
        return(self.res)
        
"""
        
        