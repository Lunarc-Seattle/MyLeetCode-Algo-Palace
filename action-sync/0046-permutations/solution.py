class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def back ():
            if len(path) == len(nums):
                res.append(path[:])# !
                return

            #为什么排列不需要 start？因为排列里：[1, 2, 3]和：[2, 1, 3]是不一样的答案。
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                
                back()
                path.pop()
                used[i] = False
        back()
        return res
            
        
