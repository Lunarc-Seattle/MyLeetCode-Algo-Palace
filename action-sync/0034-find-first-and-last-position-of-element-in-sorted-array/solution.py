class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums,target):
            left,right = 0, len(nums)-1
            while left <= right:
                mid = (right+left)//2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else: 
                    if mid ==0 or nums[mid-1] != target:
                        return mid
                    right = mid - 1
            return -1
        
        def findLast(nums,target):
            left,right = 0, len(nums)-1
            while left <= right:
                mid = (right+left)//2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else: 
                    if mid ==len(nums)-1 or nums[mid+1] != target:
                        return mid
                    left = mid + 1
            return -1
        
        first = findFirst(nums, target)
        last = findLast(nums, target)
        return [first, last]

        

