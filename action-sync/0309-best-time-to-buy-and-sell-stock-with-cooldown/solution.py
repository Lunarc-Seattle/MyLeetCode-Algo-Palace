class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sell = 0
        rest = 0

        for p in prices[1:]:
            prev_hold = hold
            prev_sell = sell
            prev_rest = rest
            #只有这三种状态： 买 卖 rest

            #另一类题（多股交易）本题只能持有一个

            hold = max(prev_rest-p,prev_hold)
            #1 hold（今天手里有股票）
            # 问：今天结束时我手里有股票，怎么来的？
            # 只有两种可能：
            # 情况1：继续持股：昨天我就拿着股票，今天我什么都不做 dp[i][hold] = dp[i-1][hold]
            # 情况2：今天买入：我昨天必须是“休息”状态（避开冷冻期），今天花钱买入--dp[i][hold] = dp[i-1][rest] - price
            # 所以hold = max(昨天hold, 昨天rest - price)
            
            sell = prev_hold+p
            #rest（今天休息）可以从哪来？
            # 情况1：昨天就在休息，今天继续休息
            # 情况2：昨天刚卖，今天被迫冷冻（也是休息）
            # 所以 rest = max(昨天rest, 昨天sell)
            rest = max( prev_sell ,  prev_rest )
        return max(sell, rest)
            #时间复杂度 O(n)
            #空间复杂度 O(1)

        
