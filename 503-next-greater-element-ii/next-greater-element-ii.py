class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(n*2):
            cur = nums[i%n]
            while stack and cur > nums[stack[-1]]:
                index = stack.pop()
                res[index] = cur
            if i < n:
                stack.append(i)
        return res