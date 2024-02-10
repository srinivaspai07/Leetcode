# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        current = head
        prev = None
        while current:
            if current.next and current.next.val == current.val:
                while current.next and current.next.val == current.val:
                    current = current.next
                if prev is None:
                    head = current.next
                else:
                    prev.next = current.next
            else:
                prev = current
            
            current = current.next  
        
        return head

        