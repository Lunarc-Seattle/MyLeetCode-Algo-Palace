class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        # 凑出 0 元，有 1 种方法：什么都不选

        #循环顺序决定你是在数“组合”还是“排列”
        # 先遍历硬币，保证算的是“组合”，不是“排列”
        for c in coins:
            for i in range(c,amount+1):
                dp[i] += dp[i-c]
    
        return dp[amount]
        
