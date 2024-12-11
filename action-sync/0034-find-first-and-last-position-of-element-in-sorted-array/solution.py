class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst( nums, target):
            l = 0
            r = len(nums)-1
            while l <= r :
                mid = (l+r)//2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid -1
                else:
                    if mid == 0 or nums[mid-1] != target:
                        return mid
                    r = mid -1
            return -1
        

        def findLast( nums, target ):
            l, r = 0, len(nums)-1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else: 
                    if mid == len(nums)-1 or nums[mid+1] != target:
                        return mid
                    l = mid + 1
            return -1
        start  = findFirst(nums, target)
        last = findLast(nums, target)
        return [start, last]




        


        
