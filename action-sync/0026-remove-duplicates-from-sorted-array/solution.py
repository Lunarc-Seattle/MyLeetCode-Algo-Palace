class Solution(object):
    # 时间复杂度：$O(n)$，我们只需要遍历一次数组。空间复杂度：$O(1)$
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        # k 是慢指针，表示当前唯一元素的下标
        k = 0 
        # i 是快指针，用来扫描整个数组
        for i in range(1, len(nums)):
            # 如果发现了一个和当前唯一元素不同的新元素
            if nums[i] != nums[k]:
                k += 1          # 慢指针右移
                nums[k] = nums[i] # 交换
        
        # tricky的点：返回长度，长度等于下标 + 1
        return k + 1
        
