class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue
                
                box_index = (i//3)*3+j//3
                
                if val in rows[i] or val in columns[j] or val in boxes[box_index]:
                    return False
                
                rows[i].add(val)
                columns[j].add(val)
                boxes[box_index].add(val)
        return True
#         平均时间复杂度：O(1)

# 所以不会放大复杂度。

# 为什么不是 O(n²)？

# 因为：

# n 不是输入规模

# 数独大小 永远固定是 9×9
# 空间复杂度为什么也是 O(1)？
# 使用了哪些额外空间？
# rows = [set() for _ in range(9)]
# cols = [set() for _ in range(9)]
# boxes = [set() for _ in range(9)]


# 3 个 list

# 每个 list 里 9 个 set

# 每个 set 最多存 9 个字符

# 👉 最大空间是固定的

# 3 × 9 × 9 = 243 个元素（上限）


# 还是常数。

# 面试常见追问（你可以这样答）

# Q：如果是 n×n 的数独呢？

# 时间复杂度：O(n²)

# 空间复杂度：O(n²)

# 👉 但本题 不是这种情况

# 一句“显得很懂”的总结

# 虽然代码形式上是双重循环，但由于数独规模固定为 9×9，
# 时间和空间复杂度都退化为 O(1)。不会出现 100×100 或 n×n 的情况

# 👉 面试官默认：常量问题 → O(1)
        
