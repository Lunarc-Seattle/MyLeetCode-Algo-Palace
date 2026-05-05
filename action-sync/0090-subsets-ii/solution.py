class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        def back(start):
            #为什么需要 start？因为排列 Permutations 里面： [1, 2, 3] [2, 1, 3] 是不同答案。 所以排列每一层都要从头看一遍不用start
            #在 Subsets / Combination 里，顺序不重要。正因为顺序不重要，所以我们要用 start 强制它只能往右走，避免出现 [1,2] 和 [2,1] 两份重复答案。
            res.append(path[:])
            for i in range(start,len(nums)):
                if i> start and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])
                back(i+1)
                path.pop()
        back(0)
        return res
        
