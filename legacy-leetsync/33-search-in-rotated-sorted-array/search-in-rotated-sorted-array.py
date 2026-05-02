class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l+(r-l)//2
            if nums[mid] == target:
                 return mid
            #判断左半部分是不是有序
            if nums[l] <= nums[mid]:
                # target 是否在左半部分
                if nums[l] <= target < nums[mid]: 
                    # 这里需要保持单调
                    #如果你只写 target < nums[mid]，算法会失去方向
                    #在旋转数组里，仅仅知道 target 小于中点是不够的，你还必须确认 target 是否在左边界 nums[l] 的右侧。
                    #如果你想更直观地理解，可以想象你在爬一个被切成两段的梯子，当你看到 target 比你手里的高度（mid）低时，你得先确认它是掉在当前这段梯子的下面，还是在另一段梯子的下面。
                    r = mid - 1
                else:
                    l = mid + 1
            #否则右半部分一定有序
            else:
                if nums[mid] < target <= nums[r]:
                    # " = "!! 当 target 刚好等于右边界 nums[r] 时，你的条件 target < nums[r] 就不成立了。
#在 nums = [5, 1, 3], target = 3 这个例子中：
                    l = mid +1
                else:
                    r = mid - 1
        return   -1  

        