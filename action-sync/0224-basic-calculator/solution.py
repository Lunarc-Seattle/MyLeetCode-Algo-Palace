class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        num = 0
        stack = []
        sign = 1

        for c in s:
            if c.isdigit():
                num = num*10+ int(c)
            elif c =='+' or c =='-':
                res = res+num*sign
                num = 0
                sign = 1 if c=='+' else -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res = res + sign*num  # 先处理当前括号里的最后一个数
                num =0
                prevSign = stack.pop()
                prevRes = stack.pop()
                res = prevRes + prevSign*res
        if num:
            res = res + sign*num 
        return res


        
