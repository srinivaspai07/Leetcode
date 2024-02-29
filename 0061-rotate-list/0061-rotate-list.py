# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Return head if head is None or if k is 0
        if not head or k == 0:
            return head
        
        # Calculate the length of the linked list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Determine the actual number of rotations needed
        k %= length
        
        # Return head if k becomes 0 after mod operation
        if k == 0:
            return head
        
        # Find the new head and new tail of the rotated list
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # Update the next pointer of the current tail to point to the original head
        tail.next = head
        
        # Update the next pointer of the node before the new head to None
        new_tail.next = None
        
        # Return the new head of the rotated list
        return new_head
