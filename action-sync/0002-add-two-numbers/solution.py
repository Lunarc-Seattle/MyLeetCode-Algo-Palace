# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy_head = ListNode(0)
        current =dummy_head

        while l1 is not None or l2 is not None:
            if l1 is not None:
                x = l1.val
            else: x=0 
            if l2 is not None:
                y = l2.val
            else: y = 0

            sum = x + y + carry
            digit = sum % 10
            carry = sum //10

            newNode = ListNode(digit)
            current.next = newNode
            current = current.next

            if l1 is not None:
                l1 = l1.next
            
            if l2 is not None:
                l2 = l2.next
               
            
        result = dummy_head.next
        if carry>0:
            current.next = ListNode(carry)
        return result

            

