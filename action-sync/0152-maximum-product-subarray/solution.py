class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #维护以当前元素结尾的最大值和最小值，利用“负负得正”在遇到负数时翻转两者，从而捕捉潜在的全局最大乘积
        curMax = nums[0]
        curMin = nums[0]
        res = nums[0]

        for n in nums[1:]:
            #要从1:开始
            temp = curMax

            curMax = max(n, n*curMax, n*curMin)
            curMin = min(n, n*temp, n*curMin)
            #这里temp注意，n*temp, n*curMin
            res = max(res, curMax)
        return res


        
