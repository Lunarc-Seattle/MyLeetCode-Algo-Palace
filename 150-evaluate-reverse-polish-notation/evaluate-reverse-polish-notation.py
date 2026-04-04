class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c =="+":
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(temp1+temp2)
            elif c == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
                # 这里注意先后 
                #栈是“后进先出”（LIFO）
            elif c == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            elif c =="/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            #除法要这样写 int(a / b)
            #因为 Python 默认：-3 // 2 = -2 ❌（向下取整）
            #但题目要：-3 / 2 = -1 ✔️（向0取整）
            else:
                stack.append(int(c))
        return stack[0]