class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+ right)//2
            if mid%2 == 1:
                mid -= 1
            if nums[mid] == nums[mid+1]:
                # break point is in the right
                left = mid+2
            else:
                # 断了 → 答案在左边（包括 mid）
                right = mid
        return nums[left]
        