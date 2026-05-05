class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack (path, open, close ):
            if len(path) == 2*n:
                res.append("".join(path))
                return

            #一开始必须先放左括号 
            if  open < n:
                path.append('(')
                backtrack(path, open+1 , close)
                path.pop()

            if close<open:
                path.append(')')
                backtrack(path, open , close+1)

                path.pop()
                # 会一直退到 open = 3 close = 0这一层
                # 然后也没有新选择了，继续退。"(((" 退到 "((" -- open = 2 close = 0这一层
                #因为这个 open = 2 的这一层，第一个 if 早就执行过了
                # 现在是从第一个 if 的递归里回来，回来之后代码位置已经走到第一个 if 后面了，所以接着执行第二个 if。
        backtrack([], 0, 0)
        return res
        
