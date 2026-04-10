class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left , right = 0 , len(nums)-1
        while left< right:
            mid = (left+right)//2
            if mid%2 == 1:
                mid = mid-1

            if nums[mid] == nums[mid+1]:
                left = mid+2
            else:
                right = mid
        return nums[left]
        