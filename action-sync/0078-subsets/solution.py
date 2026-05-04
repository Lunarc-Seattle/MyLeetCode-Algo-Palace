class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    
        res = [[]]
        for n in nums:
            for s in res[:] : #通过使用 res[:]，你实际上是在遍历 res 的一个副本
                res.append(s+[n])

        return res

        
