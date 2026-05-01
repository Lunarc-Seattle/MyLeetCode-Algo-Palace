class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #为什么用 2D list？因为我们要同时看：word1 用到第几个字符 word2 用到第几个字符
        m = len(word1)
        n = len(word2)

        dp = [[0]*(n+1) for _ in range(m+1)]
        #注意这里的行列顺序
        # m 管行，n 管列
        #word1 = "horse" word2 = "ros"
        #            r   o   s
        #    n  0    1   2   3
#       h       1
#       o       2
#       r       3
#       s       4
#     m e       5
#          初始化的是这一列
        
        #2. 初始化“地基”
        #2.1行
        for i in range(m+1):
            dp[i][0] = i
        #2.2 列
        for j in range(n+1):
            dp[0][j] = j

        # 3 开始填表
        for i in range(1,m+1):
            for j in range(1,n+1):
                #注意这里i其实是i-1
                if word1[i-1] == word2[j-1]:
                    # 情况 A：如果末尾字母一模一样
                    # 意味着不需要任何操作，直接沿用“去掉这两个字母”之前的步数
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j]+1,
                        dp[i][j-1]+1,
                        dp[i-1][j-1]+1
                    )
                    #其实就是三种操作就对应左边、上边、斜上边。
                    # 情况 B：如果末尾字母不一样，我们要从三种操作里选最省力的
                    # 1. dp[i - 1][j] + 1     -> 删除 (Delete)
                    # 2. dp[i][j - 1] + 1     -> 插入 (Insert)
                    # 3. dp[i - 1][j - 1] + 1 -> 替换 (Replace)
        return dp[m][n]
                    


        #       j=0  j=1  j=2  j=3
        #""           r    o    s
#       i=0 ""   0    1    2    3
#       i=1 h    1    .    .    .
#       i=2 o    2    .    .    .
#       i=3 r    3    .    .    .
#       i=4 s    4    .    .    .
#       i=5 e    5    .    .    .
        
