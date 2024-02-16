class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        current_node = head
        
        while current_node:
            next_node = current_node.next  # Store the next node temporarily
            current_node.next = prev_node  # Reverse the pointer
            
            # Move to the next pair of nodes
            prev_node = current_node
            current_node = next_node
        
        # After the loop, prev_node will point to the new head of the reversed list
        return prev_node
