class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow_ptr = head
        fast_ptr = head
        
        # Move fast pointer twice as fast as slow pointer
        while ( fast_ptr and  fast_ptr.next  ):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        # At this point, slow_ptr will be at the middle node
        print(slow_ptr.val)
        return slow_ptr
