class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        res = {}

        for i in range(n):
            dif = target - nums[i]
            if dif in res:
                return [i, res[dif]]
            res [nums[i]] = i
        return []
        
                    
