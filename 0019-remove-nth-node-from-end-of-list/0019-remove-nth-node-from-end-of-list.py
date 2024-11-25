class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Move the second pointer ahead by n+1 steps
        for _ in range(n + 1):
            second = second.next
        # Move first and second pointers simultaneously until second reaches the end
        while second:
            first = first.next
            second = second.next
        
        print(first.val)
        # Remove the nth node from the end
        first.next = first.next.next
        
        return dummy.next
