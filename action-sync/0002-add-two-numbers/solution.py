# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyHead = ListNode(0)
        currentHead = dummyHead
        carry = 0

        while l1 is not None or l2 is not None:
            if l1 is not None:
                x = l1.val
            else: x = 0

            if l2 is not None:
                y = l2.val
            else: y= 0

            digit = (x+y+carry)%10
            carry = (x+y+carry)//10

            newNode = ListNode(digit)
            currentHead.next = newNode
            currentHead = currentHead.next

            if l1 is not None:
                l1 = l1.next
            
            if l2 is not None:
                l2 = l2.next
                

            result = dummyHead.next

        if carry>0:
            currentHead.next = ListNode(carry)
        return result
