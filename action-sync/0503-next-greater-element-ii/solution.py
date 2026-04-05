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
            #如果不加这个 if，你的 stack 里会塞进很多无效的“第二轮下标”，最后可能会导致 res 数组下标越界（Index Out of Range）或者结果错误
            if i < n:
                stack.append(i)
        return res
