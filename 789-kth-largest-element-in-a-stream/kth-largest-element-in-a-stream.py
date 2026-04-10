class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        #heapq是一个工具箱，heapify和heappop都是工具
        heapq.heapify(self.minHeap)
        while  len(self.minHeap) > k:
        #既然它没排好序，为什么 heappop 就能拿到最小的值？因为堆有一个核心特性：最小值永远在堆顶（索引为 0 的位置）
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)