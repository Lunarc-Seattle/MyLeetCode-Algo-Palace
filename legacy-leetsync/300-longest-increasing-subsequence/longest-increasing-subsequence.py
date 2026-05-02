class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 每个位置都至少有一个可以作为subsequence
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                #看i之前的元素有没有符合条件的
                #如果之前的j 小于 现在的i
                if nums[j]< nums[i]:
                    dp[i] = max(1+dp[j],dp[i])


        
        return max(dp)


        