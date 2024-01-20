class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        n = len(nums)
        if(n>0):
            for i in range(0,n):
                ans.append(i)
            i=0
            j=n-1
            k=n-1
            while(i<=j):
                x=nums[i]
                i2=x*x
                y=nums[j]
                j2=y*y
                if(j2>i2):
                    ans[k]=j2
                    j=j-1
                else:
                    ans[k]=i2
                    i=i+1
                k=k-1
            assert (k == -1)
        return ans


