# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if k == 0 or not head or not head.next:
            return head

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # move
        k = k %length

        tail.next = head
        steps_to_new_tail = length-k
        new_tail = head
        for _ in range(steps_to_new_tail-1):
            new_tail = new_tail.next

        #剪断
        new_head = new_tail.next
        new_tail.next = None

        return new_head


        
