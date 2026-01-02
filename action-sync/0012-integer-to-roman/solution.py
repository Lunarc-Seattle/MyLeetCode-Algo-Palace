class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        list1 = [
            (1000,"M"),
            (900,"CM"),
            (500, "D"),
            (400,"CD"),
            (100,"C"),
            (90,"XC"),
            (50,"L"),
            (40,"XL"),
            (10,"X"),
            (9,"IX"),
            (5,"V"),
            (4,"IV"),
            (1,"I")]
        res = []
        for value, symbol in list1:
            while num>= value:
                num = num-value
                res.append(symbol)
        return "".join(res)
        # 先写为list【】再转化为string "".join(res)
        #O(1)
        #外层最多 13 次，内层是 n 次，
        # 为什么不是 O(n)，而是 O(1)？
        # 而且还新建了 res，为什么空间也是 O(1)？范围：1 ≤ num ≤ 3999 
        # 👉 输入规模是“被严格限制的常数” 所以空间复杂度是：
        # O(常数) = O(1)

# #一个“面试官级”的对比理解（非常重要）
# 如果题目改成这样👇

# 给你一个 任意大的整数（100 万位），转成罗马数字

# 那会变成：

# 时间：O(n)

# 空间：O(n)

# 👉 是题目约束决定复杂度，不是代码长相
            
        
