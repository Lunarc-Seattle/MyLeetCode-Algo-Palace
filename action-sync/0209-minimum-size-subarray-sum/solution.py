class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        l = 0
        sum = 0
        for r in range(len(nums)):
            sum += nums[r]

            while sum >= target:
                if r - l + 1 < res:
                    res = r - l + 1
                sum -= nums[l]
                l += 1
        return res if res != float("inf") else 0
        
