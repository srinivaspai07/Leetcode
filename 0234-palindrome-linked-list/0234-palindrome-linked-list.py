class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Function to reverse a linked list
        def reverseList(node):
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev
        
        # Function to find the middle of the linked list
        def findMiddle(node):
            slow = fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        # Function to compare two linked lists
        def compareLists(l1, l2):
            while l1 and l2:
                if l1.val != l2.val:
                    return False
                l1 = l1.next
                l2 = l2.next
            return True
        
        if not head or not head.next:
            return True
        
        # Find the middle of the linked list
        middle = findMiddle(head)
        
        # Reverse the second half of the linked list starting from the middle
        second_half = reverseList(middle)
        
        # Compare the first half with the reversed second half
        return compareLists(head, second_half)
