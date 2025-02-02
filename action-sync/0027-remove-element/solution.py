class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k =0
        n = len(nums)
        while k < n:
            if nums[k] == val:
                n -= 1
                nums[k] = nums[n]
            else: k += 1
        return n

        
