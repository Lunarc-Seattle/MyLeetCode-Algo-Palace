class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #i 看的是 s j 看的是 t
        m = len(s)
        n = len(t)

        dp = [[0]*(n+1) for _ in range(m+1)]
        # 注意这里的mn顺序 
        # m(行)： 代表源字符串 s 的长度
        # n (列)： 代表目标字符串 t 的长度

        #初始化
        # 用 s 的前 i 个字符，组成空字符串，有 1 种方法:全都不要
        for i in range(m+1):
            dp[i][0] = 1
            #dp的第一列全部是1
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                #s[i - 1] 表示：s 的前 i 个字符里的最后一个字符
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                    # dp[i-1][j-1]: 用这个 b 
                    # + 
                    # dp[i-1][j]: 不用 s 当前这个 b，用 s 的前 i-1 个字符，继续组成 t 的前 j 个字符
                else:
                    dp[i][j] = dp[i-1][j]
                    # dp[i-1][j]代表：彻底放弃 s 的当前第 i 个字符，看前面的字符能不能直接凑出目标
        return dp[m][n]
