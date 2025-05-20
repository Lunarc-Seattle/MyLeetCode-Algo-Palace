from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0              # 结果：有多少个子数组和为k
        curr_sum = 0           # 当前的前缀和
        prefix_sum_map = defaultdict(int)  # 记录前缀和出现次数
        prefix_sum_map[0] = 1  # 初始化：前缀和为0的时候也算一次（子数组从头开始）

        for num in nums:
            curr_sum += num  # 更新前缀和

            # 如果 curr_sum - k 在字典中，说明有子数组和为 k
            if (curr_sum - k) in prefix_sum_map:
                count += prefix_sum_map[curr_sum - k]

            # 更新当前前缀和出现的次数
            prefix_sum_map[curr_sum] += 1

        return count

