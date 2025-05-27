# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # 快慢 找中点
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            #slow 是中间节点
        
        # reverse later half
        prev = None
        curr = slow.next
        slow.next = None  # 切断前半部分和后半部分

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #merge
        first = head
        second = prev
         
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
            

        
