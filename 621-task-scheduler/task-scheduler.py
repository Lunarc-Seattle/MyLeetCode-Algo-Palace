class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #还有一个另一个版本（带 jump）代码更好
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1+heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time
        # edge case： [a,a,a]
        # 就会有maxHeap是空的 就会if not maxHeap:
                #time = q[0][1]   # ⭐ 跳时间