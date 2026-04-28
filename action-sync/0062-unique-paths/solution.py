class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for _ in range(m)]

        for i in range(1,m): #包左不包右[1,m) 
        # 0行就是第一行，m-1行就是m行
        #从1到m-1
            for j in range(1,n):
                dp[i][j] = dp[i][j-1] +  dp[i-1][j]
        return dp[m-1][n-1]
        # 这道题都要考虑-1
       
        
            
                

        
            
        
