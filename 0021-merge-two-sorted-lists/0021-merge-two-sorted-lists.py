class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Initialize dummy node
        dummy = ListNode()
        # Initialize current pointer
        current = dummy
        print(type(current))
        
        # Merge lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append remaining nodes of list1 or list2
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # Return the head of the merged list
        return dummy.next
