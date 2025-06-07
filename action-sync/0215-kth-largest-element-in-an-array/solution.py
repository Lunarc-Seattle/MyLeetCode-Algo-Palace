class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        minv = min(nums)
        maxv = max(nums)

        count = [0]*(maxv-minv+1)

        for num in nums:
            count[num-minv] += 1
        remaining = k

        for i in range(len(count)-1, -1, -1):
            remaining -= count[i]

            if remaining <=0:
                return i+ minv
        
