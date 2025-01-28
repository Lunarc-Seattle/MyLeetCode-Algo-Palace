class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        diction = {}
        for n in nums:
            if n in diction:
                return True
            diction[n] = 1
        return False
            
        
