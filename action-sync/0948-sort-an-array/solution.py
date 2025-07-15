class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(nums, left,right):
            if left>= right:
                return 
            l,r = left, right
            pivot = nums[(left+right)//2]
            while l<=r:
                while nums[l]<pivot:
                    l += 1
                while nums[r]>pivot:
                    r -= 1
                if l<=r:
                    nums[l], nums[r] = nums[r],nums[l]
                    l += 1
                    r -= 1
            quicksort(nums,left,r)
            quicksort(nums,l,right)    

        quicksort(nums,0,len(nums)-1)  
        return nums      
                

        
