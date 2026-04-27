class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #因为我们要一个“不可能的最大值”，方便后面取最小
        dp = [amount+1]*(amount+1)
        dp[0] = 0

        for i in range (1, amount+1):
            for c in coins:
                if i>= c:#如果i=1，coin只有2的话就太大了，凑不了
                #“沉默规则”。如果手里的硬币都太大，if i >= coin 这个条件就永远不会成立。既然进不去这个 if 内部，那 dp[i] 就会停留在它出生时的样子。
                    dp[i] = min(dp[i],dp[i-c]+1)
                #为什么+1？
                #因为从最后一枚硬币往前推，是旧的方案
                #+1 是旧的方案 + 一枚新硬币
                #当你计算 dp[i - coin] 时，你其实是在翻看你的历史记录本。比如你想凑 7块钱，手里抓着一枚 2块钱 的硬币。你往前看：“凑齐 5 块钱最少需要几枚？”
                #记事本告诉你：dp[5] = 1（也就是那一枚 5 块钱硬币）。这个 1 就是你说的 “旧方案”。
                #2. 为什么“+1”？这一步就是动作的执行。
                #你现在决定把手里这枚 2块钱 投进储钱罐。动作：你增加了一枚硬币。数学表达：就是在旧方案的枚数上 +1。
        if dp[amount] == amount+1:
            return -1
        return dp[amount]
            
        