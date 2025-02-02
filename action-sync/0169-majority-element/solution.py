class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res = 0
        maxCount = 0
        for n in nums:
            count [ n ] = 1+ count.get(n,0)
            if count[n] > maxCount:
                maxCount =count[n] 
                res = n
        return res
        
