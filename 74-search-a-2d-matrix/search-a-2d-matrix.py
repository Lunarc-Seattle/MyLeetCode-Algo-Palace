class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        #n 是列数！
        left, right = 0, m*n-1

        while left <= right:
            mid = left + (right-left)//2
            #在二分查找中使用 (right - left) // 2 而不是直接 (left + right) // 2，最核心的原因是为了防止“溢出” (Overflow)，
            mid_val = matrix[mid//n][mid%n]
            #象你在排队，每排站 n 个人。要算出你在当前排的第几个，你应该用总人数除以每排的人数 n 取余数，而不是除以总共有多少排 m
              #n 是列数！
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid+1
            else:
                right = mid-1
        return False

        