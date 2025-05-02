class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 从最后一位开始填
        p1 = m - 1  # nums1有效部分的最后一位
        p2 = n - 1  # nums2的最后一位
        p = m + n - 1  # nums1的最后一位位置

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # 如果nums2还有剩的，直接复制
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

