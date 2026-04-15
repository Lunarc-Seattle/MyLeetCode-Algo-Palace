class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2, prev1 = 0 , 0 
        #prev2 = dp[i-2]
        # prev1 = dp[i-1]
        # prev2， prev1， curr
        for i in range(2,len(cost)+1):
            curr = min(
                prev1+cost[i-1],
                prev2+cost[i-2]
            )
            prev2 = prev1 # prev2 ← prev1
            prev1 = curr
        return prev1
        #prev1 = 最终的 dp[n]


