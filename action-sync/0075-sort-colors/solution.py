class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, cur, high = 0,0,len(nums)-1
        while cur<=high:
            if nums[cur] == 0:
                temp = nums[cur]
                nums[cur] = nums[low]
                nums[low] = temp
                low+=1
                cur+=1
            elif nums[cur] ==1:
                cur+=1
            else:
                temp = nums[cur]
                nums[cur] = nums[high]
                nums[high] = temp
                high-=1
        
