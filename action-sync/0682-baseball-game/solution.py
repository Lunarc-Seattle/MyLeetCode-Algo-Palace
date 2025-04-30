class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for e in operations:
            if e == "+":
                res.append(res[-1]+res[-2])
            elif e == "C":
                res.pop()
            elif e =="D":
                res.append(2*res[-1])
            else:
                res.append(int(e))
                #转换int
        return sum(res)
    ##：为什么 if ... if ... if ... else 会错？
    #因为它会每个 if 都检查（除非你用 elif）

    #if... elif... elif... else... 是只跑第一个成立的分支，适合这种“互斥规则”。
