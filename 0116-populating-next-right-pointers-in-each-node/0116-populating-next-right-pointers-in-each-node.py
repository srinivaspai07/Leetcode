from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            prev_node = None
            
            for _ in range(level_size):
                node = queue.popleft()
                
                if prev_node:
                    prev_node.next = node
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                prev_node = node
            
            prev_node.next = None  # Set the next pointer of the last node in the level to None
        
        return root
