# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        res =[0]*len(values)
        stack = [ ]
        
        for i in range(len(values)):
            while stack and values[i] > values[stack[-1]]:
                index = stack.pop()
                res[index] =  values[i]

            stack.append(i)
        return res        