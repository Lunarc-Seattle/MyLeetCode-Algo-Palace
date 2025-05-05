class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 1<= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        # 再扫一遍，找第一个「没放对」的位置
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # 如果全放对了，就返回n+1
        return n + 1
        
