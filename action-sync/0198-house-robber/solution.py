class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0

        for n in nums:
            cur = max(prev1, prev2+n)
            prev2 = prev1
            prev1 = cur
    
        return prev1
        #prev1 always holds the maximum money you can rob up to the current house.

