"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        
        # creat new node
        cur = head
        while cur:
            newNode = Node(cur.val)
            newNode.next = cur.next
            cur.next = newNode
            cur = newNode.next
        
        # 2 Step 2: Assign random pointers

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
                #！！记得判断！
            else:
                cur.next.random = None

            cur = cur.next.next

         # Step 3: Separate original and copied lists
        cur = head
        res = head.next
        while cur:
            copy = cur.next
            cur.next = copy.next
            if cur.next:# 处理 影子娃娃a牵影子娃娃b
                copy.next = copy.next.next
            
            cur = cur.next
        return res


        
