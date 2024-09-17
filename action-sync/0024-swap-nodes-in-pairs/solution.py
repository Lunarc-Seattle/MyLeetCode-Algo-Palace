# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        res = ListNode()
        res.next = head
        cur = res

        while head and head.next:
            nxt = head.next 
            temp = nxt.next 

            cur.next = nxt
            nxt.next = head
            head.next = temp

            cur = head
            head = head.next

        return res.next


        
