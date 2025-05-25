class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}  # 字典，用来记录数字上次出现的位置

        for i in range(len(nums)):   
            num = nums[i]
            if num in last_seen:   
                if i - last_seen[num] <= k:  # 如果位置差小于等于 k
                    return True   
            last_seen[num] = i   

        return False  
