class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # o(n3)已经是最优解
        #dp[left][right]表示：
        #戳爆 left 和 right 中间的所有气球，最多能得到多少钱(不包括 left 和 right )
        # why left在左 right在右： 因为只有left到right 才是有意义的，
        #right在左 left在右就无意义    dp[left][right]
        nums = [1] + nums + [1]
        m = len(nums)

        dp = [[0]*m for _ in range (m)]

        # length 是区间长度
        for length in range(2, m):
            for left in range(0, m-length):
                right = left+ length

                # enumerate枚举每一个最后被戳爆的气球
                for k in range(left+1,right): # 不包括left and right
                    coins = ( 
                        dp[left][k]+
                        nums[left]*nums[k]*nums[right]+
                        dp[k][right]
                    )   
                    dp[left][right] = max( coins, dp[left][right] )
                    # left- right(两头不包)之间 所有的气球都要当作最后的k过一遍
                    # 每次拿一个新的方案 coins，和当前最好答案 dp[left][right] 比较
                    # 老答案 vs 新方案，谁大留谁
        return dp[0][m-1]
        # 因为我们左右加了虚拟气球
        # 戳爆最左边虚拟气球和最右边虚拟气球中间的所有真实气球
        
