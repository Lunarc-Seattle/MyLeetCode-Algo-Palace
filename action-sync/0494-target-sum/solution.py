class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # nums分成A B组，A前面都是+，B前面都是-
        # A-B = target
        # A+B = total
        # 2A  = target+ total -> A = (target+ total)/2
        # 要从 nums 里面选出一部分数字，让这部分数字的和等于(target + total) / 2

        # "First, we can handle the corner cases to return early."
        # "We should rule out these two scenarios before moving to the core logic."
        #"Before diving into the DP, I’d like to address two edge cases where the answer is obviously zero.

        #情况一：target 太大
        total = sum(nums)
        if abs(target) > total:
            return 0
        #情况二： target + total 必须是偶数
        if (target + total)%2 == 1:
            return 0
        
        #dp[j]表示：用目前看过的数字，凑出和 j，有多少种方法
        bag = (target + total)// 2 
        #必须用 // 整除（Integer Division），而 / 是浮点除（Float Division）
        dp = [0]* (bag+1)
        #因为要从 dp[0] 开始，而且还要一路包含到 dp[bag]
        dp[0] = 1
        #获取0只有一种方法：什么也不拿

        for n in nums:
            for i in range(bag, n-1,-1):
                dp[i] += dp[i-n]
        return dp[bag]
        
        
