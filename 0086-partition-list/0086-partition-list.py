# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # Initialize two dummy heads for the two partitions
        less_head = ListNode(0)
        less_tail = less_head
        greater_head = ListNode(0)
        greater_tail = greater_head
        
        # Iterate through the original linked list
        current = head
        while current:
            if current.val < x:
                # Append the node to the less than x partition
                less_tail.next = current
                less_tail = less_tail.next
            else:
                # Append the node to the greater than or equal to x partition
                greater_tail.next = current
                greater_tail = greater_tail.next
            current = current.next
        
        # Connect the two partitions
        less_tail.next = greater_head.next
        greater_tail.next = None
        
        return less_head.next
