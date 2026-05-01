class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)# 行
        n = len(matrix[0]) # 列
        
        memo = [[0]*n for _ in range(m)]
        # memo 要做成 m 行 n 列，和 matrix 一模一样

        dir = [(1,0),(-1,0),(0,-1),(0,1)]
        def dfs(i,j):
            # 如果之前算过，直接返回
            if memo[i][j] != 0:
                return memo[i][j]

            best = 1
            #自己这一个格子长度1

            for dx, dy in dir:
                ni = i+ dx
                nj = j+ dy

                if 0 <= ni < m and 0 <= nj < n:
                    if matrix[ni][nj] > matrix[i][j]:
                        # 这里分清楚 matrix还是memo
                        best = max(best, dfs(ni,nj)+1 )
            # 四个方向都检查完了，才保存
            memo[i][j] = best
            return best
                
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans,dfs(i,j))
        
        return ans
            
