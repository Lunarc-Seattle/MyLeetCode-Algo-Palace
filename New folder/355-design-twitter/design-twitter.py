class Twitter:
    

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set) # userId -> set of followeeId
        ##关注关系：followMap -> 使用 HashSet结构：
        #原因：去重：一个用户不能关注同一个博主两次
        #性能：follow 和 unfollow 操作需要频繁添加和删除。HashSet 的 add 和 remove 操作平均时间复杂度是 $O(1)$，非常高效

        #defaultdict当你使用 defaultdict 时，如果访问的键不存在，它会自动调用你预设的工厂函数（比如 list 或 set）来为这个键创建一个默认值。
        self.tweetMap = defaultdict(list)

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        #因为有defaultdict，所以不用在乎没userId的情况
        self.count -= 1
        #  key：userId | value：list（数组）
        #{ 
        #   1: [(time1, tweetId1), (time2, tweetId2), ...],
        #   2: [(time3, tweetId3), (time4, tweetId4), ...],
        # } 
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                #主要是为了防止程序因为访问不存在的键而崩溃。
                #看看我关注的这个人到底有没有发过动态，如果有，我才把他最顶上的那条动态拿去排队。”
                #为什么 followMap 不需要这种判断？
# 你可能会注意到在 follow 操作中，通常使用 defaultdict(set)。这意味着即使一个用户没有关注任何人，访问它也只会返回一个空集合，不会报错。
                index = len(self.tweetMap[followeeId])-1
                #是“这个用户本人的推特”
                #followeeId =（你关注的人）
                count, tweetid = self.tweetMap[followeeId][index]
                minHeap.append([count,tweetid,followeeId,index-1])
                # idx - 1 是为了给 Heap（堆）留一个“线索”，好让它在弹出当前最晚的推文后，能立刻顺着线索去抓“同一个人发的上一条推文”
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10 :
            count,tweetid,followeeId,index = heapq.heappop(minHeap)
            res.append(tweetid)
            if index >= 0 :
                #！！！！！！！
                # 是为了确保该关注者还有“更旧的推文”可以继续拉取。
                # 这是**多路归并排序（K-way Merge）**的核心逻辑：
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]: #！！！！！！！！！！！！！！！！！
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)