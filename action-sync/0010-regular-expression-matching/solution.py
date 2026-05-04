class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p) 

        dp = [[False]*(n+1) for _ in range(m+1)]
        #注意这里的 m,n

        dp[0][0] = True
        # 空字符串匹配空 pattern

        #如果 s 是空的，p 有没有办法也变成空？
        # 比如：s = "" ， p = "a*"
        # a* 可以表示 0 个 a，所以它可以消失：
        # s 是空字符串，p 可能是 a* / a*b* / c*a*b* 这种可以全部消掉的 pattern
        for j in range(2,n+1): # j = 1的时候不可能，因为不是*开头
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        #问题1: 它只处理这一行：它只填 第 0 行。
        #但下面填表的时候 所以它处理的是：dp[1][j]
        #dp[2][j]
        #dp[3][j] ...
        # 它不会再处理 dp[0][j]。
        #为什么必须先填第 0 行？
        #因为后面算某些格子时，会依赖它。

        #————以上初始化dp[0][i]结束

        #填表
        for i in range(1, m+1):
            for j in range(1, n+1):
                # 情况 1：当前 pattern 字符是普通字符，或者是 .
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                
                # 情况 2：当前 pattern 字符是 *
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    #先假设 x* 这一组完全不要了，把 x* 一起去掉

                    # 这里看x* 到底能吃多少个 x
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                        # dp[i][j] 获得 dp[i][j] or dp[i][j-2]的结果
                        #dp[i][j] = 0 个方案能不能成功 or 多吃 1 个方案能不能成功
                        # 因为前面已经算过一条路了：dp[i][j] = dp[i][j - 2]
                        # 只要 a 和 c 里面有一个是 True，新的 a 就是 True
        
        
        return dp[m][n]



        
