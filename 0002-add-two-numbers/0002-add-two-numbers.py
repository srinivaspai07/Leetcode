# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
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

