class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [ [ ] ]
        res = [ ] # !!!attention 

        perms = self.permute(nums[1:]) # [[]], [[], [3]], [[], [2], [2,3], [3,2]], [[],]
        for perm in perms:
            for i in range(len(perm)+1):
                temp = perm.copy()
                temp.insert(i, nums[0])
                res.append(temp)

        return res  
        

