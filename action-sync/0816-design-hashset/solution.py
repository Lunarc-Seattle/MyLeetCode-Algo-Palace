class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None
class MyHashSet:

    def __init__(self):
        self.set = []
        for i in range( 10**4 ):
            self.set.append(ListNode(0))
        
        

    def add(self, value: int) -> None:
        cur = self.set[value%len(self.set)]
        while cur.next:
            if cur.next.key == value:
                return
            cur = cur.next
        cur.next = ListNode(value)
        

    def remove(self, value: int) -> None:
        cur = self.set[value%len(self.set)]
        while cur.next:
            if cur.next.key == value:
                cur.next = cur.next.next
                return
            cur = cur.next
        

    def contains(self, value: int) -> bool:
        cur = self.set[value%len(self.set)]
        while cur.next:
            if cur.next.key == value:
                return True
            cur = cur.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
