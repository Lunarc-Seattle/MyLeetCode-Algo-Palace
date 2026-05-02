class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 只在 nums1 上试探（i）, nums2 被动配合（j）j = len(m+n) - i

        # 找最短的
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0 , m
        half = (m+n+1)//2

        while low <= high :
            i = (low+high)//2
            j = half - i

            nums1left = float('-inf') if i == 0 else nums1[i-1]
            nums1right = float('inf') if i == m else nums1[i]

            nums2left = float('-inf') if j == 0 else nums2[j-1]
            nums2right = float('inf') if j == n else nums2[j]
            
            if nums1left <= nums2right and nums1right >= nums2left:
                if (m+n)%2 == 1:
                    return max(nums1left,nums2left)
                else:
                    return (max(nums1left,nums2left)+min(nums1right,nums2right))/2
            elif nums1left > nums2right:
                high = i - 1
            else:
                low = i + 1
