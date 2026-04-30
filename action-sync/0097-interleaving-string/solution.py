class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #s1 自己内部顺序不能乱，s2 自己内部顺序也不能乱
        # 但是它们可以互相穿插
        #dp[i][j] 表示：s1 的前 i 个字符和 s2 的前 j 个字符 能不能拼出 s3 的前 i + j 个字符。
        if len(s1) + len(s2) != len(s3):
            return False
        m = len(s1) 
        n = len(s2)
        #i 是行
        #j 是列
        
        dp = [[False] * (n+1) for _ in range(m+1)]
        #所以注意这里的 mn顺序
        dp[0][0] = True
        #记得初始化
        for i in range(m+1):
            for j in range(n+1):
                # 情况1：当前字符来自 s1
                if i>0 and dp[i-1][j] and s1[i-1] == s3[i+j-1]:
                #！！这里很重要 要判断i-1>0
                #而n + 1 是因为 DP 表要多一格：表示“用了 0 个字符”的情况。
                    dp[i][j] = True
                # 情况2：当前字符来自 s2
                if j>0 and dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = True
        return dp[m][n]
    #     print("      " + "  ".join(f"{j:3}" for j in range(len(dp[0]))))
    #     for idx, row in enumerate(dp):
    # # 将 True/False 转为 1/0 看起来更直观
    #         formatted_row = [1 if cell else 0 for cell in row]
    #         print(f"Row {idx}: {formatted_row}")
        
