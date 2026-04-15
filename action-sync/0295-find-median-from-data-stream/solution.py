class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []
        #large (Min-Heap): 存储较大的一半数字，我们想快速拿到其中的最小值。
        #small (Max-Heap): 存储较小的一半数字，我们想快速拿到其中的最大值。


    def addNum(self, num: int) -> None:
        #比较极数大小
        if self.largeHeap and num>self.largeHeap[0]:
            heapq.heappush(self.largeHeap,num)
        else:
            heapq.heappush(self.smallHeap,-1*num)
            #-1*num是smallHeap里最大的

        #比较长度
        if len(self.smallHeap) < len(self.largeHeap):
            temp = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap,-1*temp)
        elif len(self.smallHeap) > len(self.largeHeap):
            temp = heapq.heappop(self.smallHeap)
            # 只要涉及到smallHeap取出来的就要-1
            heapq.heappush(self.largeHeap,-1*temp)
        
    def findMedian(self) -> float:
        if len(self.largeHeap) > len(self.smallHeap):
            return self.largeHeap[0]
        elif len(self.largeHeap) < len(self.smallHeap):
            return self.smallHeap[0]*-1
        return (self.smallHeap[0]*-1+self.largeHeap[0])/2.0
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
