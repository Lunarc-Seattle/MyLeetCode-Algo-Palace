class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat),len(mat[0])
        
        row = [0]*m
        clo = [0]*n

        for i in range(m):
            for c in range(n):
                if mat[i][c] == 1:
                    row[i] += 1
                    clo[c] += 1
        
        ans = 0
        for i in range(m):
            for c in range(n):
                if mat[i][c] == 1 and row[i]==1 and clo[c]==1:
                    ans+=1
        return ans
