class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper (arr):
            prev1, prev2 = 0 , 0
            #[ prev2 ]  -  [ prev1 ]  - [ 当前正在算的 curr ]
            # prev1 i-1
            # prev2 i-2
            for n in arr:
                curr = max(prev1, prev2+n)
                prev2 = prev1
                prev1 = curr 
            return prev1 
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[:-1]), helper(nums[1:]))
        #         不偷最后一个       不偷第一个
        
