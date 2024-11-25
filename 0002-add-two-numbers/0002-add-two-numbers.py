# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        
        newList = ListNode(0)
        dummy = newList
        
        while l1:
            
            num = l1.val + l2.val
            carry = num//10
            num = num % 10
            
            node = ListNode(num)
            newList.next = node
            newList = node
        
        return dummy.next.next
            
            
            
            
        
"""        
        fp = l1
        sp = l2
        fl = []
        sl = []

        while fp or sp:
            if fp:
                fl.append(fp.val)
                fp = fp.next

            if sp:
                sl.append(sp.val)
                sp = sp.next
        
        while fp:
            fl.append(fp.val)
            fp = fp.next

        while sp:
            sl.append(sp.val)
            sp = sp.next

        fl.reverse()
        sl.reverse()
        
        fl = int(''.join(map(str,fl)))
        sl = int(''.join(map(str,sl)))

        sum = fl + sl

        final = list(str(sum))
        final.reverse()

        node = ListNode(0)
        dummypointer = node

        for i in final:

            temp = ListNode(i)
            node.next = temp
            node = node.next
        
        return(dummypointer.next)
"""
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next
