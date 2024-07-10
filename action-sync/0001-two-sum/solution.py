class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        n = len(nums)

        for i in range(n):
            com = target-nums[i]
            if com in map:
                return [map[com], i]
            map[nums[i]] = i
        return []
