class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #总时间复杂度为 O(n*target)
        #空间复杂度只用了一个 dp 数组：O(target)
        total = sum(nums)

        if total%2 == 1:
            return False
        target = total//2
        #这里用地板除 为了转化为int，不然dp = [False]*(target+1)报错了

        
        dp = [False]*(target+1)
        dp[0] = True

        for n in nums:
            for i in range(target, n-1, -1):
                dp[i] = dp[i] or dp[i-n]
        return dp[target]

        
        
