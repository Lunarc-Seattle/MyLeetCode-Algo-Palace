class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix),len(matrix[0])
        # len(matrix) 就是行数。

        # 先做一个 (rows+1) x (cols+1) 的前缀和表，全部填0
        self.sums = [ [0]* (cols+1) for _ in range(rows+1)]

        for r in range(rows):
            for c in range(cols):
                 self.sums[r + 1][c + 1] = (
                    self.sums[r + 1][c] +  # 左
                    self.sums[r][c + 1] -  # 上
                    self.sums[r][c] +      # 左上
                    matrix[r][c]           # 自己
                )
            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.sums[row2 + 1][col2 + 1]
                - self.sums[row1][col2 + 1]
                - self.sums[row2 + 1][col1]
                + self.sums[row1][col1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
