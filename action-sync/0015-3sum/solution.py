class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 第一步：排序
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 跳过重复的第一个数

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # 跳过重复的第二个数
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 跳过重复的第三个数
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1  # 总和太小，往右边找更大的数
                else:
                    right -= 1  # 总和太大，往左边找更小的数

        return res

